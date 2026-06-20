# Statistics — ESE48E Exam Prep Suite
**CZU Prague | Applied Statistics for IT & Economics**

---

## 📦 Files

| File | Description |
|------|-------------|
| `index.html` | Main dashboard with interactive tools |
| `smart_cram_cards.html` | 3D flip flashcard study app (55 cards) |
| `README.md` | This file |

---

## 🚀 Quick Start

1. Open `index.html` in any modern browser (Chrome, Firefox, Edge)
2. Use **Normal Mode** for full solver access; **Cram Mode** for focused revision
3. Click **Flashcards** (top-right) to study with `smart_cram_cards.html`

> No server required — all files are self-contained HTML with embedded JavaScript.

---

## 📚 Course Overview

**Course Code:** ESE48E  
**Subject:** Statistics (Applied)  
**Program:** IT / Economics — CZU Prague  
**Assessment:** Written exam — multiple choice + calculation problems

---

## 🗺 Topic Coverage

### 1. Descriptive Statistics
- Measures of center: mean (μ, x̄), median, mode
- Measures of spread: variance (σ², s²), standard deviation (σ, s)
- Quartiles Q1, Q2, Q3 and Interquartile Range (IQR)
- Coefficient of Variation (CV), Z-scores
- Five-number summary, box plots, skewness

### 2. Probability
- Basic rules: addition, multiplication, complement
- Conditional probability P(A|B)
- Bayes Theorem
- Independence vs mutual exclusivity
- Permutations and combinations
- Law of Total Probability

### 3. Probability Distributions
- **Binomial B(n,p):** count of successes in n Bernoulli trials
- **Poisson Po(λ):** rare events in fixed time/space
- **Normal N(μ,σ²):** continuous bell curve, 68-95-99.7 rule
- **Standard Normal Z ~ N(0,1):** Z-table, Φ(z)
- t-distribution, χ² distribution
- Normal approximation to Binomial

### 4. Hypothesis Testing
- H₀ vs H₁, significance level α, p-value
- One-sample Z-test and t-test
- Two-sample t-test (Welch's)
- Chi-square test for independence
- Type I (α) and Type II (β) errors, Power = 1−β

### 5. Regression & Correlation
- Simple linear regression: ŷ = a + bx
- Least squares estimation: b = Sxy/Sxx, a = ȳ − b·x̄
- Pearson correlation coefficient r
- Coefficient of determination R²
- Residuals, SSE, Standard Error of Estimate (SEE)
- Correlation ≠ causation, extrapolation risk

### 6. Confidence Intervals
- For population mean: σ known (Z), σ unknown (t)
- For proportions
- Margin of error, interval width

### 7. Sampling
- Types: random, stratified, cluster, systematic
- Central Limit Theorem (CLT)
- Sampling distribution of x̄: N(μ, σ²/n)
- Standard Error SE = σ/√n

---

## 🛠 Features

### `index.html` — Dashboard
- **Cram / Normal mode toggle** (persisted in localStorage)
- **Definitions Matcher** — 8 pairs, shake on wrong, glow on correct
- **Key Formula Reference** — 8 formulas with one-click copy
- **Step-by-Step Solvers** (Normal mode only):
  - Tab 1: Normal Distribution — Z-score + percentile
  - Tab 2: Hypothesis Test Decision Maker — reject/fail interpretation
  - Tab 3: Binomial Calculator — P(X=k) with full working
  - Tab 4: Confidence Interval — CI with Z or t, margin of error
  - Tab 5: Linear Regression — b, a, r, R², SEE from raw data

### `smart_cram_cards.html` — Flashcards
- **55 high-yield cards** across 5 categories
- **3D perspective flip animation** (CSS preserve-3d)
- **Deck selector tabs:** All · Descriptive · Probability · Distributions · Hypothesis · Regression
- **Know it / Review rating** with localStorage persistence
- **Weak card checklist** — visual review list
- **Keyboard shortcuts:** Space=flip, ←→=navigate, 1=review, 2=know it
- **Stats row:** Total / Known / Review counts
- **Progress bar** tracking mastery

---

## ⌨ Keyboard Shortcuts (Flashcards)

| Key | Action |
|-----|--------|
| `Space` | Flip card |
| `←` | Previous card |
| `→` | Next card |
| `1` | Mark "Still Learning" |
| `2` | Mark "Know It!" |

---

## 🎨 Design

- **Background:** `#07090f` deep navy-black
- **Accent:** `#3b82f6` blue + `#a855f7` violet
- **Fonts:** Outfit (UI) + JetBrains Mono (code/formulas)
- Animated mesh gradient background
- Glassmorphic cards with backdrop-filter blur
- Hover lift effects + glow shadows
- Dark mode only — optimized for late-night study sessions

---

## ✅ Key Formulas Quick Reference

| Formula | Description |
|---------|-------------|
| x̄ = Σxᵢ/n | Sample mean |
| s² = Σ(xᵢ−x̄)²/(n−1) | Sample variance (Bessel's correction) |
| Z = (x̄−μ)/(σ/√n) | Z-score for sample mean |
| t = (x̄−μ)/(s/√n) | t-statistic, df=n−1 |
| P(A\|B) = P(A∩B)/P(B) | Conditional probability |
| P(B\|A) = P(A\|B)·P(B)/P(A) | Bayes Theorem |
| r = Sxy/√(Sxx·Syy) | Pearson correlation |
| b = r·(sᵧ/sₓ), a = ȳ−b·x̄ | Regression coefficients |

---

*Built for CZU Prague Statistics ESE48E — exam focused, mobile ready, no internet required after loading fonts.*
