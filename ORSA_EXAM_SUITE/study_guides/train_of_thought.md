# Step-by-Step Calculation Templates (Train of Thought)
This file provides step-by-step templates and calculations for the mathematical tasks in the ORSA exam, ensuring you avoid calculations errors.

---

## 📈 1. Linear Programming (Topic 1)

### A. Simplex Sensitivity Report (Excel Solver)
You will be given a Simplex Sensitivity Report in Excel. You must read and interpret it:

#### Interpretation Checklist
* **Allowable Increase / Allowable Decrease**:
  * **Objective Coefficient (Prices)**: The range of optimality for the profit/price coefficients where the current optimal corner point remains unchanged.
    * *Optimality Range*: $[\text{Objective Coefficient} - \text{Decrease}, \text{Objective Coefficient} + \text{Increase}]$
    * If a price changes within this range, the optimal quantities ($x_1, x_2, \dots$) remain **exactly the same**, but the total profit changes by:
      $$\Delta \text{Profit} = \Delta \text{Price} \times \text{Final Value of variable}$$
  * **R.H. Side (Resources)**: The range of feasibility for resource constraints where the current shadow prices remain valid.
    * *Feasibility Range*: $[\text{RHS} - \text{Decrease}, \text{RHS} + \text{Increase}]$
* **Shadow Price**:
  * The rate of change in the objective function (e.g. Profit) per 1-unit increase in the resource (RHS).
  * If a resource $i$ changes by $\Delta \text{RHS}_i$ (within the Feasibility Range), the new profit is:
    $$\text{New Profit} = \text{Old Profit} + (\text{Shadow Price}_i \times \Delta \text{RHS}_i)$$
  * **Crucial Rule**:
    * If a constraint is **not binding** (Slack > 0), its Shadow Price is **always 0**.
    * If a constraint is **binding** (Slack = 0), it restricts production and has a non-zero Shadow Price.

> [!WARNING]
> **Excel Solver Constraint Setup**: When grading Excel solver sheets, the teacher checks whether constraints are entered as active Excel formulas (e.g. using `=SUMPRODUCT(decision_variables, resource_coefficients)`) in the Left Hand Side (LHS) cells. Never hardcode LHS values, or you will lose points!

***

### B. Simplex Solver Excel Layout Template
Based on the course screenshots (`WhatsApp Image 2026-06-03 at 11.28.13 (7).jpeg`), this is the exact layout required for Simplex Solver setup:

| Row/Col | B | C | D | E | F | G | Note |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **8** | | | **elephants** | **girafes** | **ponies** | | |
| **9** | | **Prices ci** | 6 | 7 | 4 | | |
| **10** | | **xn** | *[0]* | *[0]* | *[0]* | | *(Yellow decision cells)* |
| **11** | | | | | | **LHS** | **RHS** | |
| **12** | | **wood** | 200 | 300 | 500 | **=SUMPRODUCT(C10:E10, C12:E12)** | 240 | *(Constraint 1)* |
| **13** | | **giraffes** | 0 | 0 | 1 | **=SUMPRODUCT(C10:E10, C13:E13)** | 0.2 | *(Constraint 2)* |
| **14** | | **total cap.** | 1 | 1 | 1 | **=SUMPRODUCT(C10:E10, C14:E14)** | 1 | *(Constraint 3)* |
| **15** | | | | | | | | |
| **16** | | **Profit** | | | | **=SUMPRODUCT(C10:E10, C9:E9)** | | *(Yellow formula cell)* |

> [!IMPORTANT]
> **LHS & Profit Formula Rule**: 
> * The **LHS** column cells (F12, F13, F14) **MUST** contain equations (e.g. `=SUMPRODUCT(C$10:E$10, C12:E12)`).
> * The **Profit** cell (F16) **MUST** contain the formula `=SUMPRODUCT(C10:E10, C9:E9)`.
> * Running Solver: In Excel, go to Data ➔ Solver:
>   * Set Objective: `$F$16` (Max)
>   * By Changing Variable Cells: `$C$10:$E$10`
>   * Subject to the Constraints:
>     * `$F$12 <= $G$12`
>     * `$F$13 >= $G$13`
>     * `$F$14 <= $G$14`
>   * Select Solving Method: **Simplex LP**
>   * Check box: **Make Unconstrained Variables Non-Negative**

***

### C. Solved Example: "Mixing a Drink"
**Problem Statement**: A bartender wants to create a 10 dl cocktail maximizing taste.
* **Ingredient A (Rum)**: 40% alcohol, 5g sugar/dl, taste score 6 points/dl.
* **Ingredient B (Juice)**: 0% alcohol, 12g sugar/dl, taste score 9 points/dl.
* **Constraints**:
  1. Total volume must be exactly 10 dl.
  2. Total drink must contain at least 20% alcohol.
  3. Total sugar must not exceed 90g.
  4. Fruit juice must represent at least 40% of total volume.

#### Step-by-Step Solution:
1. **Define Decision Variables**:
   * $x$: deciliters of rum (Ingredient A)
   * $y$: deciliters of juice (Ingredient B)
2. **Formulate LP model**:
   * $\max Z = 6x + 9y$ (Objective: Maximize Taste)
   * Constraints:
     1. $x + y = 10$ (Total volume)
     2. $0.40x \ge 0.20(x+y) \implies 0.40x \ge 2.0 \implies x \ge 5$ (Alcohol limit)
     3. $5x + 12y \le 90$ (Sugar limit)
     4. $y \ge 0.40(x+y) \implies y \ge 4.0 \implies y \ge 4$ (Juice limit)
     5. Non-negativity: $x \ge 0, y \ge 0$
3. **Solve via Substitution** ($y = 10 - x$):
   * Substitute into sugar constraint: $5x + 12(10 - x) \le 90 \implies 5x + 120 - 12x \le 90 \implies -7x \le -30 \implies x \ge 4.286$
   * Substitute into juice constraint: $10 - x \ge 4 \implies x \le 6$
   * From alcohol constraint: $x \ge 5$
   * Combined feasible range for rum: $5 \le x \le 6$
4. **Find Optimal Point**:
   * Objective function in terms of $x$: $Z = 6x + 9(10 - x) = 90 - 3x$
   * To maximize $Z$, we must **minimize** $x$.
   * The minimum value in $5 \le x \le 6$ is $x = 5$.
   * Optimal solution: **$x = 5$ dl, $y = 5$ dl**.
   * Max taste: **$Z = 6(5) + 9(5) = 75$ points**.
   * Bindings: The alcohol constraint ($x \ge 5$) is binding. The sugar constraint is non-binding (Slack = $90 - 85 = 5$ g).

---

## 🏢 2. Wassily Leontief Input-Output Analysis (Topic 3)

### A. Completing the Table
An Input-Output table must balance:
* **Row Sums (Output)**: Total output of industry $i$ ($X_i$) is the sum of its intermediate deliveries ($z_{ij}$) plus final demand ($Y_i$):
  $$X_i = \sum_{j} z_{ij} + Y_i$$
* **Column Sums (Input)**: Total inputs of industry $j$ ($X_j$) is the sum of its intermediate purchases ($z_{ij}$) plus primary inputs (Wages, Material, EBIT, etc.):
  $$X_j = \sum_{i} z_{ij} + \text{Primary Inputs}_j$$
* **Identity Rule**: Total output of sector $k$ **must equal** total input of sector $k$:
  $$X_k (\text{Row } k) = X_k (\text{Column } k)$$

***

### B. Solved Example: "Gluttony Ltd."
You are given a partially blank table with sectors: Brewery ($B$), Butcher ($Bu$), Greengrocer ($G$), Restaurant ($R$). Total outputs are: $X_B = 100$, $X_{Bu} = 80$, $X_G = 30$, $X_R = 200$.

#### 1. Complete the blank intermediate deliveries and inputs:
* **Brewery row**: $10 + 5 + 2 + z_{BR} + 23 = 100 \implies z_{BR} = 60$
* **Butcher row**: Since total input of Butcher $X_{Bu} = 80$, total output must also be $80$. So:
  $z_{Bu, B} + 10 + 2 + 45 + 18 = 80 \implies z_{Bu, B} = 5$
* **Greengrocer row**: $2 + z_{G, Bu} + z_{G, G} + 15 + 5 = 30 \implies z_{G, Bu} + z_{G, G} = 8$. From the solution files: $z_{G, Bu} = 2$, $z_{G, G} = 6$.
* **Restaurant row**: $5 + z_{R, Bu} + 1 + 5 + 184 = 200 \implies z_{R, Bu} = 5$
* **Wages row**: wages for Butcher = 4.
* **Material inputs row**: material inputs for Brewery = 20.

#### Completed Transactions Matrix ($Z$) and Primary Inputs:
| Sector | Brewery | Butcher | Greengrocer | Restaurant | Final Demand ($y$) | Total Output ($X$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Brewery** | 10 | 5 | 2 | 60 | 23 | **100** |
| **Butcher** | 5 | 10 | 2 | 45 | 18 | **80** |
| **Greengrocer** | 2 | 2 | 6 | 15 | 5 | **30** |
| **Restaurant** | 5 | 5 | 1 | 5 | 184 | **200** |
| **Wages** | 5 | 4 | 3 | 4 | | |
| **Material** | 20 | 15 | 3 | 15 | | |
| **EBIT** | 53 | 39 | 13 | 56 | | |
| **Total Inputs** | **100** | **80** | **30** | **200** | | |

#### 2. Construct Technical Coefficients Matrix ($A$):
Divide each column cell of $Z$ by that column's total output $X_j$:
$$A = \begin{pmatrix} 10/100 & 5/80 & 2/30 & 60/200 \\ 5/100 & 10/80 & 2/30 & 45/200 \\ 2/100 & 2/80 & 6/30 & 15/200 \\ 5/100 & 5/80 & 1/30 & 5/200 \end{pmatrix} = \begin{pmatrix} 0.1 & 0.0625 & 0.0667 & 0.3 \\ 0.05 & 0.125 & 0.0667 & 0.225 \\ 0.02 & 0.025 & 0.2 & 0.075 \\ 0.05 & 0.0625 & 0.0333 & 0.025 \end{pmatrix}$$

#### 3. Output change from Sales extension:
Suppose final demand for Butcher increases from 18 to 35. What are the new total outputs?
* New final demand vector: $y' = [23, 35, 5, 184]^T$.
* In Excel, compute $(I - A)^{-1}$ using `=MINVERSE()` and then `=MMULT(inverse, y')`.
* The resulting new total output vector is:
  $$x' = [101.91, 99.96, 30.80, 201.41]^T$$

#### 4. Price Index adjustments:
Suppose material input costs increase by 10% for Greengrocer ($Im_G = 1.1$) and 20% for Restaurant ($Im_R = 1.2$). Wages and EBIT prices remain unchanged ($I_w = I_e = [1, 1, 1, 1]^T$).
* Material price index vector: $I_m = [1.0, 1.0, 1.1, 1.2]^T$.
* Calculate the **Sum Vector**:
  $$\text{Sum Vector} = W I_w + M I_m + E I_e$$
  * Brewery: $5(1) + 20(1) + 53(1) = 78$
  * Butcher: $4(1) + 15(1) + 39(1) = 58$
  * Greengrocer: $3(1) + 3(1.1) + 13(1) = 19.3$
  * Restaurant: $4(1) + 15(1.2) + 56(1) = 78$
  * $\text{Sum Vector} = [78.0, 58.0, 19.3, 78.0]^T$
* Compute Output Price Index vector $Ip$:
  $$Ip = (I - A^T)^{-1} \hat{X}^{-1} (\text{Sum Vector})$$
  In Excel:
  * Transpose matrix $A$ to get $A^T$.
  * Subtract from Identity to get $(I - A^T)$.
  * Invert to get $(I - A^T)^{-1}$.
  * Construct the diagonalized output inverse matrix $\hat{X}^{-1}$ (elements are $1/X_j$, i.e., $1/100$, $1/80$, $1/30$, $1/200$).
  * Multiply: $Ip = \text{MMULT}((I - A^T)^{-1}, \text{MMULT}(\hat{X}^{-1}, \text{Sum Vector}))$.
  * Result:
    $$Ip = [1.00135, 1.00171, 1.01347, 1.01723]^T$$
    * *Interpretation*: Brewery prices rise by 0.135%, Butcher by 0.171%, Greengrocer by 1.347%, Restaurant by 1.723%.

***

### C. Solved Example: Two-sector Economy Worksheet
An economy has two sectors: Agriculture ($A$) and Industry ($I$).
* $z_{AA} = 20$, $z_{AI} = 30$, $y_A = 50$.
* $z_{II} = 40$, $y_I = 50$, $x_I = 100$.

#### Step-by-Step Solution:
1. **Solve for missing values**:
   * Total output of Industry: $x_I = z_{IA} + z_{II} + y_I \implies 100 = z_{IA} + 40 + 50 \implies z_{IA} = 10$.
   * Total output of Agriculture: $x_A = z_{AA} + z_{AI} + y_A = 20 + 30 + 50 = 100$.
2. **Technical coefficients matrix $A$**:
   * $a_{AA} = 20/100 = 0.2$, $a_{AI} = 30/100 = 0.3$.
   * $a_{IA} = 10/100 = 0.1$, $a_{II} = 40/100 = 0.4$.
   * $A = \begin{pmatrix} 0.2 & 0.3 \\ 0.1 & 0.4 \end{pmatrix}$.
3. **Leontief Inverse Matrix $(I-A)^{-1}$**:
   * $I - A = \begin{pmatrix} 0.8 & -0.3 \\ -0.1 & 0.6 \end{pmatrix}$.
   * Determinant: $\det(I-A) = 0.8(0.6) - (-0.3)(-0.1) = 0.48 - 0.03 = 0.45$.
   * Inverse: $(I-A)^{-1} = \frac{1}{0.45} \begin{pmatrix} 0.6 & 0.3 \\ 0.1 & 0.8 \end{pmatrix} = \begin{pmatrix} 1.333 & 0.667 \\ 0.222 & 1.778 \end{pmatrix}$.
4. **Demand change**:
   * Suppose final demand for Agriculture rises by 10 ($\Delta y_A = 10$, $\Delta y_I = 0$).
   * New outputs increase:
     * $\Delta x_A = 1.333 \times 10 = 13.33$ million CZK.
     * $\Delta x_I = 0.222 \times 10 = 2.22$ million CZK.

---

## 🎲 3. Binomial Distribution & Queuing Theory (Topic 4)

### A. Binomial Distribution Tasks
Formula: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$, where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

#### Task 1: Pass MCQ Quiz by guessing
A quiz has 10 questions ($n=10$), each with 5 choices (only 1 correct, so $p=0.2$). Pass threshold is at least 6 correct answers ($k \ge 6$).
* We need $P(X \ge 6) = P(X=6) + P(X=7) + P(X=8) + P(X=9) + P(X=10)$
* $P(X=6) = \binom{10}{6} 0.2^6 0.8^4 = 210 \times 0.000064 \times 0.4096 \approx 0.005505$
* $P(X=7) = \binom{10}{7} 0.2^7 0.8^3 = 120 \times 0.0000128 \times 0.512 \approx 0.000786$
* $P(X=8) = \binom{10}{8} 0.2^8 0.8^2 = 45 \times 0.00000256 \times 0.64 \approx 0.000074$
* Summing these up gives: **$P(X \ge 6) \approx 0.00637$ or $0.637\%$**.

#### Task 2: Dice rolls
Roll a fair 6-sided dice 3 times ($n=3$). Find probability of rolling a "6" exactly once ($k=1$, $p=1/6 \approx 0.1667$).
* $P(X=1) = \binom{3}{1} (1/6)^1 (5/6)^2 = 3 \times \frac{1}{6} \times \frac{25}{36} = \frac{25}{72} \approx 0.3472$ or **$34.72\%$**.

#### Task 3: Coin toss
Toss a coin 10 times ($n=10$). Find probability of getting exactly 6 heads ($k=6$, $p=0.5$).
* $P(X=6) = \binom{10}{6} 0.5^6 0.5^4 = 210 \times 0.00097656 \approx 0.2051$ or **$20.51\%$**.

***

### B. Queuing Theory Tasks (M/M/1)

#### Task 1: Elite EU Officer
* Officer signs resolutions at average rate of 40 per hour ($\mu = 40$).
* Request for signing arrives every 2 minutes. (Arrival rate $\lambda = 60 / 2 = 30$ requests per hour).
1. **Average length of queue ($L_q$)**:
   * Utilization: $\rho = \lambda / \mu = 30 / 40 = 0.75$ (or 75%).
   * $L_q = \frac{\rho^2}{1 - \rho} = \frac{0.75^2}{1 - 0.75} = \frac{0.5625}{0.25} = 2.25$ requests.
2. **Probability that request will not wait ($P_0$)**:
   * $P_0 = 1 - \rho = 1 - 0.75 = 0.25$ (or 25%).
3. **Interpretation**:
   * Server utilization is 75%, which is a safe, efficient loading. It provides a stable buffer without causing infinite queues.

#### Task 2: Flower Shop
* 1 shop assistant. Service of 1 customer takes 5 minutes on average ($\mu = 60 / 5 = 12$ customers/hour).
* Average of 9 customers enter per hour ($\lambda = 9$).
1. **Goal: probability customer doesn't wait is 0.5. Find average service time**:
   * $P_0 = 1 - \rho = 1 - \lambda / \mu = 0.5 \implies 1 - 9/\mu = 0.5 \implies \mu = 18$ customers/hour.
   * Average service time = $60 / 18 = 3.33$ minutes.
2. **Goal: desired time in system $W = 10$ minutes ($1/6$ hour). Find service rate $\mu$**:
   * $W = \frac{1}{\mu - \lambda} \implies \frac{1}{6} = \frac{1}{\mu - 9} \implies \mu - 9 = 6 \implies \mu = 15$ customers/hour.

---

## 🎲 4. Markov Chains (Topic 5)

### A. Weather Forecast 3-state system
States: Sunny ($S$), Cloudy ($C$), Rainy ($R$).
$$P = \begin{pmatrix} 0.7 & 0.1 & 0.2 \\ 0.5 & 0.25 & 0.25 \\ 0.4 & 0.3 & 0.3 \end{pmatrix}$$
* **Problem**: Today is Rainy. Calculate the probability of a rainy day for the day after tomorrow.
* **Step 0**: Initial vector is $\pi^{(0)} = [0, 0, 1]$ (Rainy today).
* **Step 1 (Tomorrow)**: $\pi^{(1)} = \pi^{(0)} P = [0.4, 0.3, 0.3]$.
* **Step 2 (Day after tomorrow)**: $\pi^{(2)} = \pi^{(1)} P$.
  We need the Rainy index (3rd element):
  $$\pi^{(2)}_R = \pi^{(1)}_S P_{SR} + \pi^{(1)}_C P_{CR} + \pi^{(1)}_R P_{RR} = 0.4(0.2) + 0.3(0.25) + 0.3(0.3) = 0.08 + 0.075 + 0.09 = 0.245$$
  * *Answer*: The probability is **0.245 or 24.5%**.

***

### B. Scared Frog Absorbing Chain
Water lilies: $A, B, C$. Frog starts at $A$. Stork is at $C$ (C is absorbing state, frog gets eaten). Scared frog jumps randomly (50:50) to another lily.
$$P = \begin{pmatrix} 0 & 0.5 & 0.5 \\ 0.5 & 0 & 0.5 \\ 0 & 0 & 1 \end{pmatrix}$$
* **Problem**: Frog starts at A. Find probability that stork is still hungry (frog is not eaten, i.e., in state A or B) after 5 hours (5 transitions/steps).
* **Step 0**: $\pi^{(0)} = [1, 0, 0]$ (starts at A)
* **Step 1**: $\pi^{(1)} = [0, 0.5, 0.5]$
* **Step 2**: $\pi^{(2)} = \pi^{(1)} P = [0.5(0.5), 0, 0.5(0.5) + 0.5(1.0)] = [0.25, 0, 0.75]$
* **Step 3**: $\pi^{(3)} = \pi^{(2)} P = [0, 0.125, 0.875]$
* **Step 4**: $\pi^{(4)} = \pi^{(3)} P = [0.0625, 0, 0.9375]$
* **Step 5**: $\pi^{(5)} = \pi^{(4)} P = [0, 0.03125, 0.96875]$
* Probability stork is still hungry: $\pi^{(5)}_A + \pi^{(5)}_B = 0 + 0.03125 = 0.03125$.
* *Answer*: **0.03125 or 3.125%**.

***

### C. 3x3 Stationary Distribution $\pi$
Solve $\pi P = \pi$ and $\sum \pi_i = 1$ for matrix:
$$P = \begin{pmatrix} 0.6 & 0.3 & 0.1 \\ 0.2 & 0.5 & 0.3 \\ 0.3 & 0.3 & 0.4 \end{pmatrix}$$
1. **Set up system of linear equations**:
   * State A: $0.6\pi_A + 0.2\pi_B + 0.3\pi_C = \pi_A \implies -0.4\pi_A + 0.2\pi_B + 0.3\pi_C = 0$
   * State B: $0.3\pi_A + 0.5\pi_B + 0.3\pi_C = \pi_B \implies 0.3\pi_A - 0.5\pi_B + 0.3\pi_C = 0$
   * State C: $0.1\pi_A + 0.3\pi_B + 0.4\pi_C = \pi_C \implies 0.1\pi_A + 0.3\pi_B - 0.6\pi_C = 0$ (linearly dependent)
2. **Substitute $\pi_C = 1 - \pi_A - \pi_B$ into State A & B equations**:
   * State A: $-0.4\pi_A + 0.2\pi_B + 0.3(1 - \pi_A - \pi_B) = 0 \implies -0.7\pi_A - 0.1\pi_B = -0.3 \implies 7\pi_A + \pi_B = 3 \implies \pi_B = 3 - 7\pi_A$
   * State B: $0.3\pi_A - 0.5\pi_B + 0.3(1 - \pi_A - \pi_B) = 0 \implies -0.8\pi_B = -0.3 \implies \pi_B = 0.375$
3. **Solve for $\pi_A$ and $\pi_C$**:
   * Since $\pi_B = 0.375$:
     $3 - 7\pi_A = 0.375 \implies 7\pi_A = 2.625 \implies \pi_A = 0.375$.
   * Since $\pi_C = 1 - \pi_A - \pi_B$:
     $\pi_C = 1 - 0.375 - 0.375 = 0.25$.
   * *Answer*: The stationary distribution vector is:
     $$\pi = [0.375, 0.375, 0.25] \quad \text{or} \quad \pi = \left[ \frac{3}{8}, \frac{3}{8}, \frac{1}{4} \right]$$
