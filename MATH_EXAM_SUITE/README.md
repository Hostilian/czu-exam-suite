# 📐 MATH Exam Prep Suite — EAE57E
### CZU Prague · Mathematics (Calculus II/III Level)

---

## 🎯 Course Overview

| Field | Info |
|-------|------|
| **Course Code** | EAE57E |
| **Subject** | Mathematics — Calculus II/III Level |
| **University** | Czech University of Life Sciences (CZU) Prague |
| **Exam Duration** | 60 minutes |
| **Format** | 6 examples |
| **Tools Allowed** | Calculator + Formula Sheet |
| **Pass Mark** | ≥ 51% |

---

## 📁 Files in This Suite

| File | Description |
|------|-------------|
| `index.html` | Main dashboard with interactive study tools |
| `smart_cram_cards.html` | 3D flip flashcard app — 55 high-yield cards |
| `README.md` | This file |

**No installation required.** Open any `.html` file directly in a modern browser (Chrome, Firefox, Edge).

---

## 🚀 Quick Start

1. Open `index.html` in your browser for the full dashboard
2. Open `smart_cram_cards.html` for rapid flashcard review
3. Toggle between **Normal mode** (full solvers) and **Cram mode** (essentials only)
4. Use keyboard shortcuts on the cram cards:
   - `Space` — Flip card
   - `←` / `→` — Navigate
   - `1` — Mark for Review
   - `2` — Mark as Known

---

## 📚 Exam Topics Covered

### 1. Integration Methods
- Power Rule: `∫xⁿ dx = xⁿ⁺¹/(n+1) + C`
- Integration by Parts (IBP): `∫u dv = uv − ∫v du`
- U-Substitution technique
- Partial Fractions decomposition for rational functions
- Standard integrals: `eˣ`, `sin`, `cos`, `1/x`, `arctan`, `arcsin`

### 2. Applications of Integration
- **Area** between curves: `A = ∫ |f(x) − g(x)| dx`
- **Volume** — Disk method: `V = π∫[f(x)]² dx`
- **Volume** — Washer method: `V = π∫([R(x)]²−[r(x)]²) dx`
- **Volume** — Shell method: `V = 2π∫x·f(x) dx`
- **Arc Length**: `L = ∫√(1+[f′(x)]²) dx`
- **Surface Area** of revolution
- Average value of a function, work by variable force

### 3. Multivariable Calculus
- **Partial derivatives** ∂f/∂x, ∂f/∂y
- **Gradient** ∇f — direction of steepest ascent
- **Critical points**: solve ∇f = 0 system
- **Hessian matrix** test: D = f_xx·f_yy − (f_xy)²
  - D > 0, f_xx > 0 → Local minimum
  - D > 0, f_xx < 0 → Local maximum
  - D < 0 → Saddle point
- Chain rule, directional derivatives, Clairaut's Theorem

### 4. Infinite Series
- **Ratio Test**: L = lim|a_{n+1}/a_n|
- **Root Test**: L = lim|aₙ|^(1/n)
- **Comparison Test** and **Alternating Series Test**
- **p-series**: converges iff p > 1
- **Geometric series**: sum = a/(1−r) for |r| < 1
- **Taylor series**: f(x) = Σ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ
- **Maclaurin series**: eˣ, sin(x), cos(x), ln(1+x)

### 5. Ordinary Differential Equations (ODEs)
- **Separation of Variables**: dy/g(y) = f(x)dx
- **1st order linear**: dy/dx + P(x)y = Q(x), integrating factor μ = e^(∫P dx)
- **2nd order homogeneous**: characteristic equation r² + pr + q = 0
  - Distinct real roots → C₁e^(r₁x) + C₂e^(r₂x)
  - Repeated root → (C₁ + C₂x)e^(rx)
  - Complex roots α±βi → e^(αx)[C₁cos(βx) + C₂sin(βx)]
- **Variation of Parameters**: y_p using Wronskian W(y₁,y₂)

---

## 🃏 Flashcard Deck Breakdown

| Deck | Cards | Topics |
|------|-------|--------|
| 📐 Integrals | 14 | Power rule, IBP, substitution, partial fractions, standard integrals |
| 🔄 ODEs | 12 | Separation, integrating factor, characteristic eq, variation of params |
| 📊 Multivariable | 10 | Partial derivs, gradient, critical points, Hessian test, chain rule |
| ∑ Series | 12 | Ratio/root/comparison tests, Maclaurin series, p-series, geometric |
| 📏 Applications | 10 | Area, volume (disk/washer/shell), arc length, improper integrals |
| **Total** | **58** | All 5 exam topics |

---

## 🧮 Interactive Solvers (Normal Mode)

1. **∫ Integration Solver** — Parse and integrate polynomials step-by-step, definite or indefinite
2. **dy/dx ODE Solver** — Separation of variables for dy/dx = ky with IC y(x₀) = y₀
3. **∑ Taylor Series Visualizer** — First N terms of eˣ, sin(x), cos(x), ln(1+x) at any x
4. **∇² Hessian Classifier** — Input f_xx, f_xy, f_yy → compute D → classify critical point
5. **Ratio/Root Test Calculator** — Input L → classify convergence with explanation

---

## 💡 Exam Strategy Tips

> **60 minutes · 6 examples · Calculator allowed**

- Each example is worth ~10 minutes. Don't spend more than 12 on any single problem.
- **Integration problems**: always check if IBP or substitution applies before partial fractions
- **ODE problems**: identify order and linearity first, then choose the right method
- **Series problems**: try Ratio Test first (works for factorials/exponentials)
- **Multivariable**: always check ALL critical points and test each with the Hessian
- **51% to pass** = you only need ~3 of 6 examples solved correctly — prioritize your strongest topics!

---

## 🎨 Design

- Dark glassmorphic premium UI — background `#080a11`
- Accent colors: Amber Gold `#f59e0b` + Emerald Green `#10b981`
- Fonts: Outfit (UI) + JetBrains Mono (math/code)
- Fully self-contained HTML — no server, no dependencies
- LocalStorage persistence for flashcard ratings

---

*Built with ❤️ for CZU Prague Mathematics students · EAE57E*
