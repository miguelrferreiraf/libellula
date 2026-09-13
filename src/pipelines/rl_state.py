"""Construção do estado probabilístico consumido pelo futuro agente de RL."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _standardize_index(frame: pd.DataFrame, dataset_name: str) -> pd.DataFrame:
    frame = frame.copy()
    frame.index = pd.DatetimeIndex(pd.to_datetime(frame.index)).astype("datetime64[ns]")
    frame.index.name = "timestamp"
    frame = frame.sort_index()

    if frame.index.has_duplicates:
        raise ValueError(f"{dataset_name} possui timestamps duplicados.")
    if not frame.index.is_monotonic_increasing:
        raise ValueError(f"{dataset_name} não está em ordem temporal crescente.")
    if frame.isna().any().any():
        raise ValueError(f"{dataset_name} possui valores ausentes.")

    return frame


def build_rl_state(
    risk_path: str | Path,
    prediction_path: str | Path,
    output_path: str | Path,
) -> pd.DataFrame:
    """Combina, com alinhamento temporal estrito, risco e previsões do TFT.

    Além do Parquet de estado, grava um manifesto JSON contendo os hashes dos
    dois insumos e da saída para rastreabilidade do treinamento de RL.
    """
    risk_path = Path(risk_path)
    prediction_path = Path(prediction_path)
    output_path = Path(output_path)

    risk = _standardize_index(pd.read_parquet(risk_path), "risk_features")
    predictions = _standardize_index(pd.read_parquet(prediction_path), "tft_predictions")

    if not risk.index.equals(predictions.index):
        raise ValueError("risk_features e tft_predictions devem possuir o mesmo índice temporal.")

    state = risk.join(predictions)
    if state.columns.has_duplicates:
        raise ValueError("O estado de RL possui nomes de features duplicados.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    state.to_parquet(output_path)

    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "risk_features": {"path": str(risk_path), "sha256": _sha256(risk_path)},
        "tft_predictions": {"path": str(prediction_path), "sha256": _sha256(prediction_path)},
        "rl_state": {
            "path": str(output_path),
            "sha256": _sha256(output_path),
            "rows": len(state),
            "columns": list(state.columns),
            "start": state.index.min().isoformat(),
            "end": state.index.max().isoformat(),
        },
    }
    manifest_path = output_path.with_suffix(".metadata.json")
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    return state
