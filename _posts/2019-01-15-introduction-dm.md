---
title: 'Introduction Decision Modeling'
date: 2018-12-01
permalink: /posts/2018/11/decision-modeling/
tags:
  - Decision Modeling
---

# Decision process

A <b>decision</b> is not an <b>instantaneous phenomenon</b>, but rather <b>impact point resulting</b> from a certain number of <b>steps</b>, namely, the <b>impact point of a process</b>.

Those <b>steps</b> (or highpoints) are defined by the <b>time of a decision process</b> which <b>marks a break with</b> respect to the <b>previous period</b>. Breaks are typically the arrival of a new information, an important event, or even the modification of the decision problem itself.

In this process, there is a progressive elaboration of options, which are fragments of decision.

# Participants, stakeholders, decision-maker

<b>An individual (group)</b> is a participant to a decision process if, through his/her value system, he/she influences (directly or indirectly) the outcome of the decision process.

For a <b>group of individuals</b> to be <b>identified as a single participant</b> to the decision process, the <b>value system</b> and <b>informational system</b> of the members of this group should be, if not identical, <b>sufficiently close</b>.

The <b>set of participants</b> to a decision process usually <b>evolve over time</b> (emergence/disappearance of participants).

# Decision aid / support

<b>Definition (Decision Aid):</b> Models to help a participant of a decision process to elaborate pieces of answers to questions he/she faces. It should increase the consistency between the evolution of the process and this participant objectives and value system.

# Example

<b>Example:</b> A dairy collects on a daily basis the milk produced in several farms, and wants to do so in an efficicent manner.

Taken litteraly, the problem is a Traveling Salesman Problem, with the set of options being hamiltonian circuits. This model is a caricature representation, usually solved with combinatorial solutions.

<i>Note:</i> The model is too simplitic as:
- Farms production varies and is not known in advance.
- Transportation time is variable (weather, trafic,...), timing for cows milking is subject to âtime windowsâ.
- There exists 3 Trucks â the problem changes in its nature,
- A single criterion? risk of uncollected milk, ...

The model can not be considered out of the context.

Building a decision model can contribute to modifying the formulation of the initial problem:
- Installation of a second dairy
- Policy for bying/renting trucks
- Subcontracting milk collection

<b>Load balancing problem:</b> Cover the load using a minimum staf

<b>Problem data:</b>
- $t = 1, 2, ..., T$ periods
- $C_{t}$ = load for period $t$, $t = 1, 2, ..., T$
- $h = 1, 2, ..., H$ working hours types
- $a_{ht} = \begin{cases}1& \text{if working hours type h covers period t}\\ 0 & \text{ otherwise}\end{cases}$

<b>Decision variables:</b> x_{h}, h = 1, .., H is the number of persons employed using working hours type h.

<b>Optimization model:</b>
$$
\begin{align}
Minimize & \sum_{h=1}^{H} x_{h}\\
s.t. & \begin{cases}
\sum_{h=1}^{H} x_{h} \geq C_{t} \forall t\\
x_{h}\geq 0, \forall h
\end{cases}
\end{align}
$$

<i>Note:</i> There can be additional constraints such as:

| Constraints      |   Adjustments   |  Practical  |
|------------------|:---------------:|:-----------:|
| Legal            |      Pauses     |     Who?    |
| Labor agreements | Illness + delay |    When?    |
| Habits           |     Strikes     | Assignment? |

<i>Work load curve ?</i> Usually rules like <i>type of airplane Ã destination Ã time</i>

# Alternatives, problem stat

The alternatives are typically the possible options (hamiltonian path for traveling salesman problem for instance).

<b>Types of alternatives:</b>

| Evolution | Solution(s) |
|-----------|:-----------:|
| Stable    | Fragmentary |
| Change    |   Holistic  |

<b>Decision problem statements:</b>
- Choice of the best alternative
- Rank from the best to the worst (ranking can be complete or partial)
- Rank from the best to the worst (ranking can be complete or partial)

<i>Note:</i> More decision problem statements

| "Chain" problem statements |        Beyond Choice-Sort-Rank       |
|:--------------------------:|:------------------------------------:|
|      Sorting + Choice      |                k-best                |
|      Sorting + Ranking     | Sorting with cardinality constraints |
|      Ranking + Sorting     |          Portfolio selection         |


------
