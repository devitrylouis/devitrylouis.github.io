---
title: 'Synthesis criterion'
date: 2018-12-01
permalink: /posts/2019/01/dm-synthesis-criterion/
tags:
  - Decision Modeling
---

## 1. Introduction

The multicriteria principle of synthesis criterion aims at building a function $g$ synthesizing all criteria:

$$g(a) = f(g_{1}(a),g_{2}(a),...,g_{n}(a))$$

Such approach allows for
- Pre-order on the set of alternatives $A$
- Compare alternatives
- Choose among them
- Rank them
- Assign them to classes

Nonetheless, building $g$ is often difficult and requires a big amount of preference information from the decision-maker.

In particular, we should focus on its two aspects:
1. Which properties should the decision-maker preferences possess so as to be representable by a $g$ function?
2. How to build $g$ and set the values to the parameters involved in the chosen parametric form?

### 1.1. Weighted sum

It is the simplest and the most used analytic form, The function g takes the following analytic form:

$$
g(a) = \sum_{i=1}^{n} w_{i}g_{i}(a)
$$

and the corresponding structure is:

$$
\begin{cases}
a \succeq b \Leftrightarrow g(a) > g(b)\\
a = b \Leftrightarrow g(a) = g(b)\\
\end{cases}
$$

### 1.2. Multi-attribute value model

This weighted sum can be generalized to non-linear operations for the preferences on a criteria. It is the role of the Multi-Attribute Value Theory, which takes the following form:

$$
\begin{cases}
a \succeq b \Leftrightarrow u(a) > u(b)\\
a = b \Leftrightarrow u(a) = u(b)\\
\end{cases}
$$
with  $u(a) = f(g_{1}(a),g_{2}(a),...,g_{n}(a))$.

A frequently encountered case is the additive form of the MAVT:

$$
u(a) = \sum_{i=1}^{n} w_{i} u_{i}(g_{i}(a))
$$

with $u_{i}(g_{i}^{\text{min}}) = 0$, $u_{i}(g_{i}^{\text{max}}) = 1$ and normalized weights.

## 2. Constructing value functions

To specify an additive MAVT model, one should elicit marginal value functions $u_{i}$, $\forall i \in F$ and “weights” $w_{i}$, $\forall i \in F$. In particular, we are interested in eliciting:
1. <u>Value function</u> $u_{i}$ (for each criterion).
2. <u>Weight vector</u> $w_{i}$.

### 2.1. Elicitation of value function $u_{i}$

<b>Method 1:</b> convenient when the evaluation scale $E_{i}$ is finite.
1. Rank elements of $E_{i}$
2. Rank differences between consecutive elements in the preceding ranking
3. Assign values compatible with the information obtained at step 1. and 2.

### 2.2. Eliciting importance coefficients $w_{i}$

Consider $b_{j}$ an alternative such that $g_{i}(b_{j}) = g_{i}^{\text{min}}$ , $\forall i \neq j$ and
$g_{j}(b_{j}) = g_{j}^{\text{max}}$.

1. Rank $b_{j}$ , $j \in F$ by order of preference,
2. Reorder criteria such that $b_{n} \succ . . . \succ b_{1}$, we induce that $w_{n} \geq ...\geq w_{1}$

Now consider $b_{j}^{n}$ such that $g_{i}(b_{j}^{n}) = g_{i}^{min}\ \forall i \neq n$ and $g_{i}(b_{j}^{n}) = x$.

3 Determine g_{n}(b_{n}(j)) such that $b_{1} \sim b_{n}^{j}$ to obtain:
$$ \sum_{i=1}^{n} u_{i} (b_{1}) = \sum_{i=1}^{n} u_{i}(b_{n}^{j}) $$

4. Finally, we obtain: $\frac{w_{1}}{w_{n}} = u_{n}(x)$ or $u_{n}(g_{n}(x))$

5. Repeat for all $g_{2}, ..., g_{n-1}$

Hence we obtain the ratios $\frac{w_{i}}{w_{n}},\ i = 1, ..., n−1$

> TODO: Revoir notations! Indices tout ca!

### 2.3. UTA

> TODO: Add image

The goal of UTA is to:
1. Define a ranking on a subset of alternatives $(a_{2} \succ a_{1} \succ a_{6} \succ a_{8})$.
2. Define a linear program which minimizes an error function and infers an additive value model compatible with the stated ranking.
3. Based on this inferred additive value model, rank order all alternatives.

## 3. Inferring a value function

Searched model: $u(a) =  \sum_{i=1}^{n} u_{i} (g_{i} (a))$ with $u_{i}$ piecewise linear marginal value function.

If $z ∈[g_{i}^{l}, g_{i}^{l+1}]$ then:

$$u_{i}(z_{i})=u_{i}(u_{i}^{l})+ \frac{z^{i}−g_{i}^{l}}{g_{i}^{l+1} - g_{i}^{l}}$$

$A'$ is a subset of alternative ranked by the decision-maker
Inferred value $u'$: $u'(a) = u(a) + \sigma(a), \forall a ∈ A'$ where $\sigma(a)$ is the error in the estimation of $u(a)$.

> TODO: Custom program

![Optimization program](/images/dm_inference.png)

------
