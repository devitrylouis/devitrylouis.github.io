---
title: 'Outranking methods'
date: 2018-12-01
permalink: /posts/2019/01/dm-outranking-method/
tags:
  - Decision Modeling
---

<b>A collective decision problem</b>

For a ranking vote like this one
- 5 voters : x ≻ y ≻ z ≻ t
- 2 voters : t ≻ y ≻ x ≻ z
- 8 voters : z ≻ y ≻ x ≻ t
- 4 voters : x ≻ z ≻ y ≻ t
- 6 voters : t ≻ y ≻ z ≻ x
- 2 voters : t ≻ z ≻ y ≻ x

there are many ways to elect a candidate:

- <u>Method 1:</u> Number of votes placing a candidate in the first rank:
    * $t$ is elected
- <u>Method 2:</u> Two round ballot.
    * $x$ is elected
- <u>Method 3:</u> Sum of ranks (Borda 1770)
    * $y$ iselected
- <u>Method 4:</u> Condorcet’s rule (1785) with pairwise comparisons of candidates
    * $z$ is elected

<b>Social choice vs Multicriteria decision</b>

<u>Social choice</u>
- Each voter gives a ranking on candidates.
- The elected candidate should account for the point of view of all voters.
- Each voter has the same voting power (one vote).

<u>Multicriteria decision</u>
- Each criterion evaluates/compares alternatives.
- The final decision results from the information on all criteria.
- Criteria might not have the same importance

<b>Multiple criteria Decision Analysis</b> With what we have seen so far, we constructed two families of multicriteria methods, whose specificities lie in the order of operations: Aggregate then compare vs compare then aggregate:

> TODO: Make table

- <u>Synthesis criterion:</u> Borda, multi-attribute value theory,...
    * aggregate then compare impose a strong structure on the preference model (difficult construction), simple exploitation.
- <u>Pairwise comparaison:</u> Condorcet, Outranking methods, ...
    * compare then aggregate
        * Do not impose structure on the preference model (easy construction),
        * Difficult exploitation.

> TODO: <b>Central problem:</b>

## 1. Outranking methods

### 1.1. Introduction

<b>History</b> Introduced by Bernard Roy et al. in the 1960s, outranking methods works in real application and prove useful in solving the difficulties encountered with a synthetic criterion (i.e. compensation and qualitative data).

> TODO: Many methods have been proposed since: ELECTRE, PROMETHEE, TACTIC, ...

<b>Decision problems tackled</b>
Let us consider a finite set of alternatives $A = \{ a_{1}, ..., a_{n} \}$ and a family $F = \{ g_{1}, ..., g_{p} \}$ of $p$ criteria. Then, we are interested in tackling:
- Selection / choice
- Ranking
- Sorting / classification

<b>Notion of pseudo-criterion</b>

A <u>pseudo criterion</u> $g_{j}:A \mapsto \mathbb{R}$ with two threshold:
1. An <u>indifference threshold</u> q_{j}
2. A <u>preference threshold</u> p_{j}

such that:

$$
\begin{cases}
a\succ_{j} b \Leftrightarrow g_{j}(a) - g_{j}(b) \geq p_{j}\\
a\sim_{j} b \Leftrightarrow |g_{j}(a) - g_{j}(b)| \leq q_{j}\\
a Q_{j} b \Leftrightarrow q_{j} < g_{j}(a) - g_{j}(b) < p_{j}\\
\end{cases}
$$

> TODO:
> - Give intuition + image
> - Precise special case:
>      * $p_{j} = q_{j}$
>      * $q_{j} = 0$
>      * $p_{j} = q_{j} = 0$


### 1.2. Formalism

<b>Concept of outranking relation</b>

- $a$ outranks $b$ ($a \succeq b$) is valid if the arguments in favor of the proposition “$a$ is at least as good as $b$” are sufficiently strong.
- Arguments in favor of $a\succeq b$ are grounded on:
    * Evaluation of $a$ and $b$
    * Information preferences of the DM (weights, threshold)
- If no argument can be found in favor of $a\succeq b$ nor $b \succeq a$ then there is incomparability.

<b>4 preference situations</b>

> TODO: Add image

<b>Structure of outranking methods</b>

The relation $\succeq$ has a few intersting properties:
- $a\Delta b \Rightarrow a \succeq b \forall a, b \in A$
- $\succeq$ is reflexive
- $\succeq$ is not necessarily transitive from Condorcet paradox

## 2. Contruction of outranking relations

<b>Construction of outranking relations</b>

$a \succeq b$ is valid iff two conditions are met:
- <u>Concordance condition (majority principe):</u> A majority of criteria should be in favor of $a \succeq  b$.
- <u>Non-discordance condition (respect of minorities):</u> No criterion should strongly contradict $a \succeq b$.

These principles can be implemented in different ways and can impose weak (or stronger) requirements.

## 2.1. Concordance condition / majority

<b>Concordance condition</b>

<u>Partial concordance:</u> we consider the contribution of each criterion to $a \succeq b$

The partial correspondance index $c_{j}(a, b) \in [0, 1]\  \forall j$ is defined as such:
- $c_{j}(a, b) = 0 \Leftrightarrow g_{j}$ is not in favor of $a \succeq b$
- $c_{j}(a, b) = 1 \Leftrightarrow g_{j}$ fully agrees with $a \succeq b$
- $c_{j}(a, b) \in (0, 1) \Leftrightarrow g_{j}$ partially agrees with $a \succeq b$

This can be implemented as follows:

$$ c_{j}(a, b) =
\begin{cases}
1 \text{ if } g_{j}(a) \geq g_{j}(b) - q_{j}\\
0 \text{ if } g_{j}(a) \leq g_{j}(b) - p_{j}\\
\frac{p_{j} - (g_{j}(a) - g_{j}(b))}{p_{j} - q_{j}} \text{ otherwise }\\
\end{cases}
$$

> TODO: Understand the example

<b>Overall concordance (majority)</b>

Overall concordance evaluates the level of majority of criteria in favor of $a \succeq b$

Overall concordance $C (a, b) \in [0, 1]$ is such that:
- $C(a,b) = 0$ when no criterion is in favor of $a \succeq b$
- C(a,b) = 1 when all criteria are in favor of $a \succeq b$
- $C (a, b) \in ]0, 1[$ when some criteria are in favor of $a \succeq b$

which mathematically translates to:

$$ C(a, b) = \sum_{j=1}^{p} w_{j}c_{j}(a, b) $$

with the weights being positive and normalized.

## 2.2. Non-discordance condition / veto

<b>Non-discordance condition/Veto</b>

Among criteria which disagree with $a \succeq b$, some can express a strong opposition, a veto which leads to invalidate $a \succeq b$.

On each criterion $g_{j}$, we define a veto threshold $v_{j}$ such that if $g_{j}(a)<g_{j}(b)−v_{j}$ for a given $j$, then $a \succeq b$ is invalidated (whatever the importance of the concordant coalition)

We define, on each criterion, a partial discordance index $d_{j} (a, b) \in [0, 1]$ such that:
- $d_{j}(a,b) = 0$ if $g_{j}$ does not oppose to $a \succeq b$.
- $d_{j}(a,b) = 1$ if $g_{j}$ fully opposes to $a \succeq b$.
- $d_{j}(a,b)\in]0,1[$ if $g_{j}$ partly opooses to $a \succeq b$.

<b>Outranking relation (integrating concordance and non-discordance)</b>

- In the Electre III method, a fuzzy outranking relation is defined: valued outranking $\sigma(a, b) \in [0, 1]$,
- If no discordant criterion exist $\sigma(a, b) = C (a, b)$,
- If one/several criteria is/are discordant $\sigma(a, b) < C (a, b)$,
- If $d_{j}(a,b) = 1$ for one criterion $\sigma(a,b) = 0$

We pose

$$
\simga(a, b) = C(a, b) \Pi_{j\in\overline{F}}\frac{1-d_{j}(a,b)}{1- C(a, b)} \in [0, 1]
$$

with $\overline{F} = \{ j \in F: d_{j}(a, b) > C(a, b) \}$

> TODO:
> - Taxonomy of ELECTRE algorithms
> - Outranking relation in Electre IS

<b>One/several outranking relation(s)</b>

According to the considered method, one can construct:
- A unique outranking relation grounded on a requirement level fixed a priori, (Electre I, Electre IS)
- A fuzzy outranking relation $\succeq^{\sigma}$ defined by a a fuzzy membership function $\sigma$ (Electre III, Electre Tri),
- A set of embedded outranking relations  $\succeq_{1}\subset \succeq_{2} \subset . . . \subset \succeq_{k}$ grounded on $k$ requirement levels fixed a priori (Electre II, Electre IV).

> TODO: Give intuition

<b>Representation of binary relations</b>

A binary outranking relation $\succeq$ represented by an outranking graph $G = (X,U)$ avec :

- $X = A = {a_{1},a_{2},...,a_{n}}$
- $U={(a_{i},a_{j})\in X\times X$ such that $a_{i}\succeq a_{j}}$.

<b>Valued outranking relation</b>

Valued (fuzzy) outranking relation $\succeq^{\sigma}$ represented by a graph $G_{\sigma} = (A,U)$ valued by $\sigma(a_{i},a_{j})$.

> TODO: Give intuition

<b>Nested outranking relations</b>

Several nested outranking relations $\succeq_{1},  \succeq_{2}, . . . ,  \succeq_{k}$ with $k$ graphs $G_{i} =(A, \succeq_{i})$, i =1,...,k:

- $\succeq_{1}\subseteq \succeq_{2}\subseteq ... \subseteq \succeq_{k}$
- The weaker the requirement level, the richer the relation.

<b>Nested relations $\succeq_{1}\subset \succeq_{2}\subset \succeq_{3}$</b>

> TODO: Add image

<b>Exploiting outranking relations</b>

According to the problem, we are looking to:
1. Select the smallest subset $A^{\text{*}} \subset A$ of best alternatives → Choice set $A^{\text{*}}$
2. Assign each alternative to a category by partitioning A:

$$ A_{1} ,A_{2} ,...,A_{k} A=\cup_{i=1}^{k} A_{i} \text{ and } A_{i}\neq A_{j},\forall i \neq j $$

3. Rank order the alternatives according to preferences on A pre-order (possibly partial) on A.

> TODO: What is a preorder?

## 3. Exploitation - building recommandations

<b>Construction de prescriptions</b>
<b>Building recommendations/prescriptions</b>

### 3.1. Exploitation for choice recommendation
### 3.2. Exploitation for sorting recommendation
### 3.3. Exploitation for ranking recommendation

## Sources
- This blogpost is heavily inspired from [Vincent Mousseau](https://www.researchgate.net/profile/Vincent_Mousseau) lectures, my professor at Centrale-Supélec.
- [Layman intuition video](https://www.youtube.com/watch?v=e3GFG0sXIig)

------
