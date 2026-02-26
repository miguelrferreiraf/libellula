import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path


def setup(
    csv_path,
    target_col="Price",
    horizon=1,
    train_ratio=0.7,
    val_ratio=0.15,
    save_artifacts=True,
    artifacts_path="../../data/artifacts/",
    processed_path="../../data/processed/"
):
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

    if "Change %" in df.columns:
        df["Change %"] = (
            df["Change %"]
            .str.replace("%", "", regex=False)
            .astype(float) / 100
        )

    df = df.sort_values("Date").reset_index(drop=True)

    df["target_return"] = df[target_col].pct_change(horizon).shift(-horizon)
    df["target_direction"] = (df["target_return"] > 0).astype(int)

    df = df.dropna().reset_index(drop=True)

    feature_cols = [col for col in df.columns if col not in [
        "Date",
        "target_return",
        "target_direction"
    ]]

    X = df[feature_cols]
    y = df["target_return"]

    n = len(df)
    train_end = int(n * train_ratio)
    val_end = int(n * (train_ratio + val_ratio))

    X_train, X_val, X_test = (
        X.iloc[:train_end],
        X.iloc[train_end:val_end],
        X.iloc[val_end:]
    )

    y_train, y_val, y_test = (
        y.iloc[:train_end],
        y.iloc[train_end:val_end],
        y.iloc[val_end:]
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    if save_artifacts:
        artifacts_dir = Path(artifacts_path)
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        joblib.dump(scaler, artifacts_dir / "feature_scaler.pkl")

        processed_dir = Path(processed_path)
        processed_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(processed_dir / "dataset_processed.csv", index=False)

    return {
        "X_train": X_train_scaled,
        "X_val": X_val_scaled,
        "X_test": X_test_scaled,
        "y_train": y_train.values,
        "y_val": y_val.values,
        "y_test": y_test.values,
        "feature_columns": feature_cols
    }