# Libellula

**Probabilistic Risk-Control Architecture for Systematic Trading**

---

## 1. Objective

Libellula is a modular machine learning architecture designed to solve a capital allocation problem under structural uncertainty.

The system reframes systematic trading as a stochastic control problem.
Directional prediction is treated as conditional information.
Capital deployment is treated as the primary optimization target.

The central objective is:

* Maximize risk-adjusted capital growth
* Minimize probability of ruin
* Control drawdown under non-stationary regimes

---

## 2. Conceptual Framework

Financial markets exhibit:

* Non-stationarity
* Heavy-tailed return distributions
* Volatility clustering
* Regime shifts
* Structural uncertainty

Point prediction alone is insufficient to ensure long-term capital survival.
Libellula integrates predictive modeling with probabilistic risk modeling and reinforcement learning–based policy optimization.

The system architecture separates:

* Forecast generation
* Risk-state construction
* Scenario expansion
* Capital control

---

## 3. System Architecture

### 3.1 Predictive Layer — Temporal Fusion Transformer (TFT)

A multivariate Temporal Fusion Transformer models temporal dependencies across structured financial features.

Input:

* Multivariate price series
* Technical indicators
* Structural features
* Contextual macro features (optional)

Output:

* Conditional return forecast
* Directional bias
* Uncertainty proxies (preferred: quantiles or distributional outputs rather than point estimates only)

This layer generates probabilistic expectations but does not issue trade decisions.

---

### 3.2 Risk Envelope Layer

The Risk Envelope is a composite probabilistic modeling framework designed to quantify exposure and structural vulnerability.

Components may include:

* Conditional volatility estimation
* Tail-risk modeling
* Drawdown probability estimation
* Regime detection mechanisms
* Exposure sensitivity metrics
* Correlation structure analysis

Outputs are aggregated into a multivariate risk-state dataset containing:

* Predictive outputs from TFT
* Risk metrics
* Distributional statistics
* Regime indicators
* Structural exposure variables

This dataset represents a probabilistic snapshot of the current market configuration.

---

### 3.3 Monte Carlo Scenario Expansion

The risk-state dataset is expanded using state-conditional Monte Carlo simulation.

Purpose:

* Generate thousands of plausible trajectories
* Approximate empirical outcome distributions
* Stress-test capital allocation decisions
* Reduce deterministic bias

The simulation process is conditional on:

* Current volatility structure
* Estimated regime
* Tail characteristics

The result is a synthetic scenario dataset representing probabilistic future paths.

---

### 3.4 Capital Control Layer — Reinforcement Learning

The final layer is a reinforcement learning agent responsible exclusively for capital management.

Input:

* Monte Carlo–expanded scenario dataset
* Risk-state features
* Predictive outputs

Output:

* Position size
* Stop-loss parameters
* Exposure adjustments

The RL agent learns a policy mapping probabilistic state representations to allocation decisions.

---

## 4. Optimization Objective

The reinforcement learning agent is trained under an explicitly defined objective function.

Possible optimization targets include:

* Risk-adjusted return maximization
* Drawdown minimization
* Utility-based growth optimization
* Risk-of-ruin minimization
* Volatility targeting stability

The reward function is designed to penalize:

* Excessive drawdown
* Capital instability
* Tail exposure amplification

The system does not attempt to maximize raw directional accuracy.
It optimizes capital behavior under uncertainty.

---

## 5. Design Principles

1. Prediction is conditional input, not certainty.
2. Risk is modeled explicitly and structurally.
3. Scenario expansion improves policy robustness.
4. Allocation is optimized via learned policy control.
5. Survival precedes aggressive growth.

---

## 6. Methodological Constraints

To reduce structural overfitting and leakage:

* Training and validation pipelines are strictly segregated.
* Monte Carlo expansion is conditional and regime-aware.
* Reinforcement learning is trained on scenario distributions rather than single historical paths.
* Model stacking avoids circular dependency between predictive and risk layers.
* Backtesting incorporates transaction costs, slippage, and execution constraints.

---

## 7. High-Level Data Flow

Market Data
→ TFT Predictive Model
→ Risk Envelope Models
→ Multivariate Risk-State Dataset
→ Monte Carlo Scenario Expansion
→ Reinforcement Learning Capital Controller
→ Position Size and Risk Parameters

---

## 8. Research Directions

* Distributional forecasting instead of point forecasting
* Regime-aware Monte Carlo engines
* Tail-risk penalized reward shaping
* Multi-asset portfolio extension
* Dynamic leverage constraints
* Capital efficiency benchmarking

---

## 9. Development Status

* Predictive module: under development
* Risk envelope module: under development
* Monte Carlo expansion engine: conceptual design completed
* Reinforcement learning controller: architecture defined
* Reward function formalization: pending refinement

---

## 10. Positioning

Libellula is not a prediction engine.

It is a probabilistic capital control system built to operate under uncertainty, structural regime shifts, and heavy-tailed market dynamics.

Its goal is not to forecast certainty.

Its goal is to optimize capital behavior within probabilistic reality.
