# Dynamic Stochastic Modeling in Economics 🌌📊

![GitHub stars](https://img.shields.io/github/stars/jadenfix/repo?style=social)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Economics](https://img.shields.io/badge/Economics-Macro%2FQuant-8A2BE2)

**A computational exploration of stochastic dynamics in economic systems**  
From foundational models to cutting-edge policy analysis, this repository bridges economic theory with numerical implementation.

---

## 🧠 Core Topics

### 1. **Foundational Models**
- Multiplier-accelerator framework
- Unit roots and AR(1) processes
- Linear stochastic difference equations  
*[Explore Samuelson Model](https://python.quantecon.org/samuelson.html)*

### 2. **Markov Processes**
- Finite state Markov chains
- Stationary distributions
- Ergodicity and convergence  
*[Markov Chains I](https://intro.quantecon.org/markov_chains_I.html) | [II](https://intro.quantecon.org/markov_chains_II.html)*

### 3. **Dynamic Programming**
- McCall job search model
- Value function iteration
- Career choice models  
*[McCall with Separation](https://python.quantecon.org/mccall_model_with_separation.html)*

### 4. **Optimal Growth**
- Cake-eating problem
- Coleman policy iteration
- Endogenous grid methods  
*[Optimal Growth Fast](https://python.quantecon.org/optgrowth_fast.html)*

### 5. **Asset Pricing**
- Markov-based pricing
- General equilibrium models
- Harrison-Kreps speculative bubbles  
*[Arrow Securities](https://python.quantecon.org/ge_arrow.html)*

### 6. **Policy Applications**
- SIR epidemiological modeling
- Economic impact of lockdowns
- Synthetic control methods  
*[SIR Model](https://python.quantecon.org/sir_model.html)*

---

## 💻 Technical Showcase

```python
# Optimal Growth Model with Endogenous Grid Method
import numpy as np
from quantecon import optimize

def egm_policy_iter(k_grid, β=0.96, α=0.65, δ=0.1):
    """
    Solves optimal growth model via EGM.
    """
    production = k_grid**α
    savings = β * (1 - δ + α * production**(α-1))
    return optimize.interp(k_grid, savings)
```
