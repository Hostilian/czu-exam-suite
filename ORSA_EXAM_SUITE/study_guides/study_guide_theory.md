# Part 1: Theory & CLD Study Guide
This guide covers the theoretical concepts tested in **Part 1 of the ORSA Exam** (Max 50 points, 30-minute limit). It covers matching definitions, multiple-choice concepts, and causal loop diagrams.

---

## 🧩 1. System Science & Systems Thinking (Topic 2)
### Key Definitions
* **System**: A group of elements and relations between these elements. A system is an entity that maintains its existence through the mutual interaction of its parts. It is more than the sum of its parts.
* **System Classification**:
  * **Closed System**: Does not need to interact with the environment to maintain its existence. Examples: atoms, molecules.
  * **Open System**: Must interact with the environment to maintain its existence. Example: people, organizations.
* **Complex System**: A system composed of multiple interacting elements, where the behavior of the system as a whole cannot be explained solely by understanding the behavior of each of its individual parts.
* **5 Key Components of a Complex System**:
  1. **Self-Organization**: The ability to organize its structure or behavior without external control.
  2. **Emergence**: Behavior of the system as a whole cannot be fully predicted from the behavior of its individual parts.
  3. **Nonlinearity**: Small changes in one part of the system can have a significant, disproportionate effect on the system as a whole.
  4. **Adaptation**: The system can change its behavior or structure in response to changing environmental conditions.
  5. **Feedback Loops**: Outputs of the system are routed back as inputs, forming closed chains of cause-and-effect.
* **Entity**: A system that maintains its existence through the mutual interaction of its parts.
* **Model**: A simplified version of a real-world process or system. Created to understand, analyze, and optimize it. 
  * *Why model?* Trial-and-error on the original object is often impossible (e.g. non-ethical social experiments), and modeling is cheaper, faster, and reproducible.
* **Types of Models**:
  * **Normative vs. Descriptive**: Normative models describe what *should* be done (evaluation based on criteria), while descriptive models describe what is *actually* being done (no judgment).
  * **Static vs. Dynamic**: Static models represent a system at a specific point in time, whereas dynamic models account for changes over time.
  * **Deterministic vs. Stochastic**: Deterministic models assume all variables are known and can be precisely determined. Stochastic models account for randomness and uncertainty.
* **Hard vs. Soft Systems Thinking**:
  * **Hard Systems Thinking**: Optimizes design using defined performance criteria and selects the alternative which best meets the need and is feasible.
    * *Advantages*: Allows the use of powerful quantitative techniques.
    * *Disadvantages*: Requires professional experts; can focus too much on logical aspects and ignore personal/social dynamics.
  * **Soft Systems Thinking**: Improves the conceptual model by using soft systems applications (e.g., Soft Systems Methodology) to gain an understanding of the problem and negotiate a course of action.
    * *Advantages*: Available to both problem owners and experts; stays connected to the personal aspect of a problem.
    * *Disadvantages*: Does not produce final/optimal answers; accepts that the process of learning never stops.
* **Well-Structured Problem**: A problem where we know the procedures and methods of the solution, have all necessary information, or know how to obtain it (e.g., operational control).
* **Time**: In mathematical models, time is represented as a continuous variable or as discrete intervals.
* **Probability**: A mathematical concept used to quantify the likelihood of an event occurring, ranging from 0 (impossible) to 1 (certain).

---

## 🗺️ 2. Soft Systems Methodology - SSM (Topic 9)
Developed by **Peter Checkland** in the late 1960s at the University of Lancaster (UK). It is a learning and meaning development tool. Models in SSM do not represent the "real world" directly; they are conceptual holons used to structure thinking about the real world.
It is designed for situations characterized by **multiple goals, multiple perspectives, different assumptions, different logics, and high entanglement**.

### The Seven Stages of SSM Inquiry
SSM alternates between the real world and a conceptual systems world:
1. **Stage 1: The Problem Situation (Real World)**: Acknowledge and explore the problem area in an unstructured way, gathering data from surveys, interviews, and observations.
2. **Stage 2: Problem Situation Expressed - Rich Picture (Real World)**: Draw a cartoon-like diagram depicting the situation. A Rich Picture must include:
   * **Structures** (physical layout, departments)
   * **Processes** (information and material flows)
   * **Climate** (working environment, feelings)
   * **People** (stakeholders)
   * **Issues expressed by people** (complaints, concerns)
   * **Conflicts** (friction points between stakeholders)
3. **Stage 3: Root Definitions of Relevant Systems (Conceptual World)**: Formulate root definitions based on purposeful perspectives (**holons**). A root definition is structured as: *"A system to do X, by Y, in order to do Z."* Elements are defined using **CATWOE** or its political extension **BATWOVE**:
   * **C – Customers** (or **B – Beneficiaries** / **V – Victims**): Who benefits or suffers from the system's transformation.
   * **A – Actors**: Those who perform the transformation activities.
   * **T – Transformation**: The core process converting input to output (`Input ➔ Output`).
   * **W – Weltanschauung (Worldview)**: The underlying belief system that makes the transformation meaningful.
   * **O – Owners**: Those who can start, change, or stop the system.
   * **E – Environmental Constraints**: External limitations that the system must accept as given.
4. **Stage 4: Conceptual Model (Conceptual World)**: Build a logical diagram of activities (using verbs in the imperative, aiming for **$7 \pm 2$** activities) necessary to carry out the transformation. Define dependencies and ensure it meets 9 systems properties (purpose, performance measures, decision process, subsystems, interactions, environment, boundary, resources, continuity).
5. **Stage 5: Comparison of Model and Reality (Real World)**: Use a matrix to compare each activity with the real world, asking: *Does it exist? How does it behave? How is it measured? Is it any good?*
6. **Stage 6: Desirable and Feasible Changes (Real World)**: Identify interventions that are both systematically desirable and culturally/politically feasible. This is checked via:
   * **Owner Analysis** (who has authority to act)
   * **Social System Analysis** (roles, norms, values)
   * **Political Analysis** (how power is expressed)
7. **Stage 7: Action to Improve (Real World)**: Implement changes, which may trigger a new cycle of inquiry.

---

## 📈 3. Linear Programming Concepts (Topic 1)
* **Linear Programming**: A mathematical method to make the most of available resources to achieve a desired outcome, taking into account constraints. It seeks to maximize or minimize a linear objective function.
* **Objective Function**: A linear expression to be maximized (e.g., profit) or minimized (e.g., cost).
* **Decision Variables**: Unknown quantities ($x_1, x_2, \dots$) to be solved.
* **Constraints**: Linear equations or inequalities restricting decision variables (due to resource limits, capacity limits, contract requirements, etc.).
* **Non-Negativity Constraints**: Strict requirement that decision variables must be greater than or equal to zero ($x_i \ge 0$).
* **Feasible Region**: The set of all points satisfying all constraints.
* **Optimal Solution**: A point in the feasible region that yields the best objective value. It **always** lies at one of the corner points (vertices) of the feasible region.
* **Slack Variable**: Represents unused resources in a "$\le$" constraint.
* **Surplus Variable**: Represents the excess over a minimum requirement in a "$\ge$" constraint.
* **Simplex Method**: An algebraic algorithm that finds the optimal solution by moving systematically from corner point to corner point along the boundary of the feasible region.
* **Sensitivity Analysis**: Studying how changes in model parameters (coefficients of objective function or RHS values of constraints) affect the optimal solution.

---

## 🏢 4. Input-Output Analysis Concepts (Topic 3)
* **Input-Output Analysis**: A modeling technique used to analyze the relationships between different sectors of an economy. The basic idea is that every sector of the economy is both a supplier and consumer of goods and services.
* **Wassily Leontief**: Economist who won the Nobel Prize in 1973 for developing Input-Output (I-O) analysis.
* **Intermediate Consumption (Demand)**: Goods and services purchased by industries from each other as inputs for further production (represented by the transactions matrix $Z$).
* **Final Demand (Uses, $y$)**: Production sold to final consumers (households, government, export, investment).
* **Total Output ($x$)**: The total value of goods produced by a sector. It equals intermediate demand plus final demand.
* **Technical Coefficient ($a_{ij}$)**: The value of inputs from sector $i$ needed to produce 1 unit of output in sector $j$. Defined as:
  $$a_{ij} = \frac{z_{ij}}{X_j}$$
* **Leontief Matrix**: The matrix $(I - A)$, where $I$ is the identity matrix and $A$ is the technical coefficient matrix.
* **Leontief Inverse Matrix $(I - A)^{-1}$**: Also called the **multiplier matrix** ($M$). It represents both direct and indirect inputs required across all sectors to satisfy one unit of final demand.
* **Value Added (Primary Inputs)**: Production costs that are not purchased from other sectors (wages, depreciation, EBIT/profit, taxes on production, imports).
* **Price Indices**: Equations used to estimate output price adjustments in response to changes in primary input prices (e.g., wage increases or material cost hikes).

---

## 🎲 5. Stochastic Models & Markov Chains (Topics 4 & 5)
### Stochastic Processes (Basic)
* **Binomial Distribution**: Model for the number of successes ($k$) in a fixed number of independent trials ($n$), where each trial has a constant probability of success ($p$).
* **Poisson Process**: A continuous-time process where independent events occur at a constant average rate ($\lambda$). The number of arrivals in a fixed time interval follows a Poisson distribution, and the time between arrivals follows an exponential distribution.
* **Queuing Theory (Kendall's Notation - $M/M/s$)**:
  * **First M**: Markovian arrival process (Poisson arrivals, exponential inter-arrival times).
  * **Second M**: Markovian service times (exponential service times).
  * **s**: Number of parallel servers.
  * *Metrics*: $\rho$ (server utilization), $L$ (customers in system), $L_q$ (customers in queue), $W$ (time in system), $W_q$ (time in queue).

### Markov Chains
* **Markov Chain**: Describes a system moving from one state to another under a certain probabilistic rule.
* **Markov Property (Memorylessness)**: The probability distribution of the next state depends **only** on the current state and not on the sequence of events that preceded it.
* **Transition Matrix ($P$)**: A square matrix of conditional probabilities $P_{ij}$ showing the probability of moving from state $i$ to state $j$ in a single step. **Crucial Rule**: The sum of each row in $P$ must equal exactly 1.
* **State Vector ($\pi^{(t)}$)**: The probability distribution across all states at step $t$. Calculated as:
  $$\pi^{(t)} = \pi^{(0)} P^t$$
* **Trajectory Probability**: The probability of a specific sequence of states. Calculated by multiplying the initial state probability by each subsequent transition probability:
  $$P(s_0, s_1, s_2) = P(X_0=s_0) \cdot P_{s_0s_1} \cdot P_{s_1s_2}$$
* **Communicating Class**: A set of states where every state can eventually reach every other state in the set (and vice versa) over some number of steps ($i \leftrightarrow j$).
* **Closed Class**: A communicating class that cannot be left once entered.
* **Absorbing State**: A state that, once entered, cannot be left ($P_{ii} = 1$).
* **Transient State**: A type of state in a Markov chain where, once left, there is a positive probability that you will never return back to it.
* **Absorbing Markov Chain**: A Markov chain in which every state can reach an absorbing state.
* **Irreducible Markov Chain**: A chain where the entire state space is a single communicating class (you can get from any state to any other state).
* **Hitting Probability ($h_{iA}$)**: The probability of ever reaching a set of states $A$ starting from state $i$.
* **Expected Hitting Time ($m_{iA}$)**: The expected number of steps required to reach set $A$ starting from state $i$.

---

## 🔄 6. System Dynamics & Causal Loop Diagrams (Topic 6)
* **System Dynamics (SD)**: An approach to understanding the nonlinear behavior of complex systems over time using stocks, flows, internal feedback loops, table functions, and time delays.
* **Causal Link Polarity**:
  * **Positive link ($A \xrightarrow{+} B$ or $A \xrightarrow{S} B$)**: Variables change in the **same** direction. If $A$ increases, $B$ increases. If $A$ decreases, $B$ decreases.
  * **Negative link ($A \xrightarrow{-} B$ or $A \xrightarrow{O} B$)**: Variables change in the **opposite** direction. If $A$ increases, $B$ decreases. If $A$ decreases, $B$ increases.
* **Feedback Loop Polarity**:
  * **Reinforcing Loop (R / $+$)**: Amplifies change, leading to exponential growth or decay.
    * *Rule*: Contains an **even number** (or 0) of negative ($o$) links.
  * **Balancing Loop (B / $-$)**: Seeks goals, stability, or equilibrium. Opposes change.
    * *Rule*: Contains an **odd number** of negative ($o$) links.
* **Delay (Time Lag)**: Delayed feedback between cause and effect. Indicated on a causal link by a double line crossing the arrow.

---

## 🏛️ 7. System Archetypes (Topic 7)
System archetypes represent common structural patterns that recur in many different systems. (Structures matching the course slides):

### 1. Limits to Success / Limits to Growth
A reinforcing loop drives rapid growth, but eventually runs into a resource constraint, activating a balancing loop that slows and stops the growth.
* **Variables**: `Efforts`, `Performance`, `Limiting Action`, `Constraint`.
* **Causal Links**:
  * `Efforts` $\xrightarrow{s}$ `Performance`
  * `Performance` $\xrightarrow{s}$ `Efforts` (Loop **R1: Reinforcing**)
  * `Performance` $\xrightarrow{s}$ `Limiting Action`
  * `Constraint` $\xrightarrow{s}$ `Limiting Action`
  * `Limiting Action` $\xrightarrow{o}$ `Performance` (Loop **B2: Balancing**)

### 2. Tragedy of the Commons
Individuals share a common resource and act in their own self-interest, leading to overexploitation and eventual destruction of the resource for everyone.
* **Variables**: `A's Activity`, `B's Activity`, `Total Activity`, `Gain per Individual Activity`, `Net Gains for A`, `Net Gains for B`, `Resource Limit`.
* **Causal Links**:
  * `A's Activity` $\xrightarrow{s}$ `Net Gains for A` $\xrightarrow{s}$ `A's Activity` (Loop **R1: Reinforcing**)
  * `B's Activity` $\xrightarrow{s}$ `Net Gains for B` $\xrightarrow{s}$ `B's Activity` (Loop **R2: Reinforcing**)
  * `A's Activity` $\xrightarrow{s}$ `Total Activity`
  * `B's Activity` $\xrightarrow{s}$ `Total Activity`
  * `Total Activity` $\xrightarrow{o \text{ with delay}}$ `Gain per Individual Activity` (Delay marker `||`)
  * `Resource Limit` $\xrightarrow{s}$ `Gain per Individual Activity`
  * `Gain per Individual Activity` $\xrightarrow{s}$ `Net Gains for A`
  * `Gain per Individual Activity` $\xrightarrow{s}$ `Net Gains for B`
* **Additional Loops**:
  * `A's Activity` $\rightarrow$ `Total Activity` $\rightarrow$ `Gain per Individual` $\rightarrow$ `Net Gains for A` $\rightarrow$ `A's Activity` (Loop **B5: Balancing**)
  * `B's Activity` $\rightarrow$ `Total Activity` $\rightarrow$ `Gain per Individual` $\rightarrow$ `Net Gains for B` $\rightarrow$ `B's Activity` (Loop **B6: Balancing**)

### 3. Shifting the Burden
A quick, short-term "fix" (External Intervention) is used to solve a problem symptom, but it has delayed side effects that weaken the system's long-term capability to solve the root cause (Internal Solution), making the system dependent on the fix.
* **Variables**: `Problem Symptom`, `External Intervention`, `Internal Solution`, `Dependence on External Intervention`.
* **Causal Links**:
  * `Problem Symptom` $\xrightarrow{s}$ `External Intervention`
  * `External Intervention` $\xrightarrow{o}$ `Problem Symptom` (Loop **B1: Balancing**)
  * `Problem Symptom` $\xrightarrow{s}$ `Internal Solution`
  * `Internal Solution` $\xrightarrow{o \text{ with delay}}$ `Problem Symptom` (Loop **B2: Balancing**)
  * `External Intervention` $\xrightarrow{s}$ `Dependence on External Intervention`
  * `Dependence on External Intervention` $\xrightarrow{o \text{ with delay}}$ `Internal Solution` (Delay marker `||`)
* **Feedback Loop R3 (Reinforcing Side Effect)**: `External Intervention` $\rightarrow$ `Dependence` $\rightarrow$ `Internal Solution` $\rightarrow$ `Problem Symptom` $\rightarrow$ `External Intervention` (Contains two $o$ links, making it Reinforcing).

### 4. Escalation
Two competitors escalate their actions in response to perceived threats, creating a reinforcing loop of increasing defensive/aggressive measures.
* **Variables**: `Activity by A`, `A's Result`, `Quality of A's Position Relative to B's`, `Threat to A`, `Activity by B`, `B's Result`, `Threat to B`.
* **Causal Links**:
  * `Activity by A` $\xrightarrow{s}$ `A's Result` $\xrightarrow{s}$ `Quality of A's Position` $\xrightarrow{o}$ `Threat to A` $\xrightarrow{s}$ `Activity by A` (Loop **B1: Balancing**)
  * `Activity by B` $\xrightarrow{s}$ `B's Result` $\xrightarrow{o}$ `Quality of A's Position` $\xrightarrow{s}$ `Threat to B` $\xrightarrow{s}$ `Activity by B` (Loop **B2: Balancing**)
* **Result**: Together, B1 and B2 form a large reinforcing figure-8 of competitive escalation.

### 5. Fixes that Fail
A quick fix is applied to solve a symptom, but it triggers a delayed unintended consequence that makes the problem symptom worse.
* **Variables**: `Problem Symptom`, `Fix`, `Unintended Consequence`.
* **Causal Links**:
  * `Problem Symptom` $\xrightarrow{s}$ `Fix`
  * `Fix` $\xrightarrow{o}$ `Problem Symptom` (Loop **B1: Balancing**)
  * `Fix` $\xrightarrow{s \text{ with delay}}$ `Unintended Consequence` (Delay marker `||`)
  * `Unintended Consequence` $\xrightarrow{s}$ `Problem Symptom` (Loop **R2: Reinforcing**)

### 6. Growth and Underinvestment
Growth is limited by capacity, but capacity investment is avoided, leading to a drop in performance. This performance drop is then used to justify not investing.
* **Variables**: `Growth Effort`, `Demand`, `Performance`, `Performance Standard`, `Perceived Need to Invest`, `Investment in Capacity`, `Capacity`.
* **Causal Links**:
  * `Growth Effort` $\xrightarrow{s}$ `Demand` $\xrightarrow{s}$ `Growth Effort` (Loop **R1: Reinforcing**)
  * `Demand` $\xrightarrow{o}$ `Performance` $\xrightarrow{s}$ `Demand` (Loop **B2: Balancing**)
  * `Performance` $\xrightarrow{o}$ `Perceived Need to Invest`
  * `Performance Standard` $\xrightarrow{s}$ `Perceived Need to Invest`
  * `Perceived Need to Invest` $\xrightarrow{s \text{ with delay}}$ `Investment in Capacity`
  * `Investment in Capacity` $\xrightarrow{s \text{ with delay}}$ `Capacity`
  * `Capacity` $\xrightarrow{s}$ `Performance` (Loop **B3: Balancing with Delays**)

### 7. Drifting Goals / Eroding Goals
When performance fails to meet a target, instead of correcting performance, the goal is lowered to match actual performance.
* **Variables**: `Goal`, `Gap`, `Actual`, `Corrective Action`, `Pressure to Lower Goal`.
* **Causal Links**:
  * `Goal` $\xrightarrow{s}$ `Gap` $\xrightarrow{s}$ `Corrective Action` $\xrightarrow{s \text{ with delay}}$ `Actual` $\xrightarrow{o}$ `Gap` (Loop **B1: Balancing**)
  * `Goal` $\xrightarrow{s}$ `Gap` $\xrightarrow{s}$ `Pressure to Lower Goal` $\xrightarrow{o}$ `Goal` (Loop **B2: Balancing**)

### 8. Accidental Adversaries
Two partners start a cooperative relationship that is mutually beneficial. However, each partner takes local actions to optimize their own performance, which, after a delay, unintendedly undercuts the success of the other partner.
* **Variables**: `A's success`, `A's activity`, `B's success`, `B's activity`.
* **Causal Links**:
  * `A's success` $\leftrightarrow$ `A's activity` (Reinforcing loops)
  * `B's success` $\leftrightarrow$ `B's activity` (Reinforcing loops)
  * `A's success` $\xrightarrow{s}$ `B's success` $\xrightarrow{s}$ `A's success` (Outer Loop **R: Partnership Success**)
  * `A's activity` $\xrightarrow{o \text{ with delay}}$ `B's success` (Undercutting link `U`, delay `||`)
  * `B's activity` $\xrightarrow{o \text{ with delay}}$ `A's success` (Undercutting link `U`, delay `||`)

---

## 🖥️ 8. Simulation Theory (Topic 10)
* **Computer Simulation**: Imitation of real-world system processes over time to evaluate and improve performance. Used when analytical models are mathematically impossible or too complex.
* **Discrete Event Simulation (DES)**: Modeling a system where variables change state only at discrete, distinct points in time (events), such as customer arrivals at a bank.
* **Continuous Simulation**: Modeling a system where states change continuously over time, such as fluid moving through a pipeline.
* **Monte Carlo Simulation**: A simulation technique that uses repeated random sampling from probability distributions to model uncertainty and calculate probability distributions of outcomes.
* **Agent-Based Simulation (ABS)**: Models individual autonomous decision-making entities ("agents") that interact with each other and their environment, producing emergent system-level behavior.
