# Libellula  
## A Stochastic Control Architecture for Probabilistic Capital Management

---

## 1. Formal Problem Statement

Let:

- \( X_t \in \mathbb{R}^n \) be the multivariate market state at time \( t \)  
- \( r_{t+1} \) be the future return  
- \( \mathcal{F}_t \) the information set available at time \( t \)  
- \( W_t \) the capital (wealth process)  

We seek a policy \( \pi_\theta \) such that:

\[
a_t = \pi_\theta(s_t)
\]

Where:

- \( s_t \) is a probabilistic state representation of the market  
- \( a_t \) defines allocation decisions (position size, stop level, exposure adjustment)  

The objective is to optimize a risk-aware utility functional:

\[
\max_\pi \; \mathbb{E}\left[ \sum_{t=0}^{T} \gamma^t \, U(W_t) \right]
\]

Subject to:

\[
W_{t+1} = W_t \cdot (1 + a_t \cdot r_{t+1})
\]

Under stochastic dynamics:

\[
r_{t+1} \sim P(r_{t+1} \mid \mathcal{F}_t)
\]

Libellula models and expands this conditional distribution before optimizing capital allocation.

---

## 2. Architectural Overview

Libellula is structured as a four-layer stochastic decision pipeline:

1. Conditional Forecasting  
2. Risk Envelope Modeling  
3. State-Conditional Monte Carlo Expansion  
4. Reinforcement Learning Capital Control  

The system reframes systematic trading as a **sequential stochastic control problem** rather than a pure prediction task.

---

## 3. Layer I — Conditional Forecasting (TFT)

### Model
Temporal Fusion Transformer (TFT)

### Function

Approximate:

\[
\hat{P}(r_{t+1} \mid X_t)
\]

Rather than generating a deterministic point forecast, the model ideally outputs:

- Conditional mean \( \mathbb{E}[r_{t+1} \mid X_t] \)
- Conditional quantiles
- Distributional uncertainty estimates

### Role in System

The predictive layer provides directional bias and probabilistic expectation.  
It does **not** generate trading decisions.

---

## 4. Layer II — Risk Envelope

The Risk Envelope transforms predictive and structural signals into a probabilistic state representation.

It may include:

- Conditional volatility estimation \( \sigma_t \)
- Tail-risk estimation (CVaR, EVT-based metrics)
- Drawdown probability estimation
- Regime classification
- Exposure sensitivity metrics

Let:

\[
z_t = f(X_t, \hat{P}(r_{t+1}), \sigma_t, \text{tail metrics}, \text{regime state})
\]

Where \( z_t \in \mathbb{R}^m \) is the enriched probabilistic state vector.

This layer models uncertainty explicitly and encodes structural risk factors.

---

## 5. Layer III — State-Conditional Monte Carlo Expansion

Given the probabilistic state \( z_t \), we generate synthetic trajectories:

\[
\{ r_{t+1}^{(i)}, r_{t+2}^{(i)}, ..., r_{t+H}^{(i)} \}_{i=1}^N
\]

Where:

- \( N \) = number of simulated scenarios  
- \( H \) = horizon  

The simulation must be:

- Regime-sensitive  
- Volatility-conditioned  
- Non-Gaussian (heavy-tail aware)  

The goal is to approximate the empirical distribution:

\[
\tilde{P}(r_{t:t+H} \mid z_t)
\]

This expanded scenario space reduces overconfidence and improves robustness of policy learning.

---

## 6. Layer IV — Reinforcement Learning Capital Controller

### State

\[
s_t = g(z_t, \tilde{P})
\]

Where \( s_t \) encodes probabilistic scenario information.

### Action Space

\[
a_t = (\text{position size}, \text{stop level}, \text{exposure modifier})
\]

### Wealth Dynamics

\[
W_{t+1} = W_t \cdot (1 + a_t \cdot r_{t+1})
\]

### Reward Design (examples)

**Log-utility maximization**
\[
R_t = \log(W_{t+1})
\]

**Risk-adjusted objective**
\[
R_t = r_t - \lambda \cdot \text{Drawdown}_t
\]

**CVaR-penalized objective**
\[
R_t = \mathbb{E}[r_t] - \lambda \cdot \text{CVaR}_\alpha
\]

**Ruin-constrained objective**
\[
\min \; \mathbb{P}(W_t \leq W_{\min})
\]

The reward function determines system behavior (aggressive growth vs robustness).

---

## 7. Theoretical Foundations

Libellula integrates:

- Stochastic control theory  
- Reinforcement learning (policy optimization)  
- Monte Carlo simulation  
- Distributional forecasting  
- Risk-of-ruin mathematics  
- Heavy-tail modeling  
- Non-stationary time-series modeling  

The system operates under the assumption that:

- Markets are non-stationary  
- Returns exhibit volatility clustering  
- Extreme events dominate long-term capital dynamics  

---

## 8. Key Design Principles

1. Prediction is conditional information, not certainty.  
2. Allocation is the primary control variable.  
3. Risk is modeled explicitly and probabilistically.  
4. Scenario expansion reduces deterministic bias.  
5. Survival constraints dominate long-term growth.

---

## 9. High-Level Data Flow
