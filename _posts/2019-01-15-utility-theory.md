---
title: 'Utility  theory'
date: 2018-12-01
permalink: /posts/2018/11/utility-theory/
tags:
  - Decision Modeling
---

In many decision situations, informations to be taken into account are not known in advance. We will states the principles of utility theory, which find roots in neoclassical economics (dominates modern economic theory today).

<b>Predictible situations:<b>
- <i>Deterministic situations:</i> Data are known in advance (classical O.R., Lin. Prog., Graph theory, ...),
- <i>Situation stochastic situation:</i> Data are not known in advance, but probability distributions can be hypothetized
- <i>Situation competitive situation:</i> Data involved in the decision depend on exogenous actions (game theory, ...)
- <i>Complete uncertainty:</i> Data of the decision problem are not known in advance, and no probability distribution can be determined.

A first framework to <b>formalize this problem</b> is the following
- <u>States of nature:</u> $\Theta = \{ \theta_{1}, ..., \theta_{n} \}$
- <u>Possible decisions:</u> $\mathcal{D} = \{ d_{1}, ..., d_{n} \}$
- <u>Outcome matrix:</u> $r(d_{i} \mid \theta_{j})$: outcome of decision $d_{i}$ if the state of nature $\theta_{j}$ intervenes.

<b>Criteria for choice under uncertainty:</b> The outcome matrix can be computed with several criterions, the most common being cited in the table below

| Laplace criterion | Wald criterion | Savage criterion |
|:--------------------------------------------------------------------------:|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| $\text{Max}_{d_{i} \in \mathcal{D}} \sum_{j=1}^{n}r(d_{i}\mid \theta_{j})$ | $\text{Max}_{d_{i}\in \mathcal{D}} \text{ Min}_{\theta_{j}} r(d_{i}\mid \theta_{j})$ | $\text{Max}_{d_{i}\in \mathcal{D}} \text{ Min}_{\theta_{j}} regret(d_{i}, \theta_{j})$ |
| Equiprobability of states | Max Min prudence | Min Max regret |

where $regret(d_{i}, \theta_{j})$ is the regret of decision $d_{i}$ for the state of nature $\theta_{j}$, i.e. the difference of outcome between the best decision for $\theta_{j}$ and $r(d_{i}, \theta_{j})$.

<U>Utility theory</U> is a central model for decision under uncertainty. It works by considering the notion of risk through objects (lotteries) evaluated by a distribution of outcome.

## Utility theory - comparing lotteries

<b>Definition (Lotteries):</b> The central objects under study are distributions of outcome, later evaluated.

<i>Note:</i> The question becomes: given two lotteries, how do we compare them.

### The von Neumann–Morgenstern axioms

Utility theory is grounded on the following set of axioms, which aims to define a rational decision maker.

1. <b>Completeness $A_{1}$:</b> assumes that an individual has well defined preferences and can always decide between any two alternatives. The preferences are expressed by the relation $A\succeq B$ where A and B are two preferences. (what about $I$ and $P$?)

2. <b>Transitivity $A_{2}$:</b> If $A\succeq B$ and $B\succeq C$ then $A\succeq C$

3. <b>Independence $A_{3}$:</b> Assumes that two gambles mixed with an irrelevant third one will maintain the same order of preference as when the two are presented independently of the third one. It is the most controversial axiom. Let $A$, $B$ and $C$ be three lotteries with $A\succeq B$ and let $t$ be the probability that a third choice is present ($t\in [0,1]$). If $tA + (1-t)B \succeq tB + (1-t)C$ then the order of preference for $A$ before $B$ holds, independently of the presence of irrelevant choice $C$.

4. <b>Continuity $A_{4}$:</b> Let $A$, $B$ and $C$ be lotteries with $A\succeq B\succeq C$ then there exists a probability $p$ such that $B$ is equally good as $pA+(1-p)C$.

<i>Weak order on the lotteries:</i> 1. and 2. are valid

### Fundamental results

<u>Expected utility:</u> the expected utility of the outcomes of a lottery $L$ defines the utility of $L$:
$$u(L) = \sum_{i = 1}^{n} p_{i}u(x_{i})$$

<b>Existence:</b> If axioms are fulfilled by a decision model, there exists a utility function $u$ representing the decision model prefrences using the expected utility criterion.

<b>Unicity</b> This utility function u is unique up to a affine transformation $(\alpha u + \beta)$, such that:
$$ L\succeq L' ⇔ u(L) > u(L') $$

### Utility function

A utility function codomain is an interval of possible outcomes $[x, x^{*}]$ with $u(x^{*}) = 0$ and $u(x^{*}) = 1$. Any utility function is set to be monotonically increasing.

Interpretation of decision models concerns the link between risk attitudes and the form of utility functions. Specifically, a DM is risk averse if it prefer any expected
outcome of a lottery to this lottery:

<b>Theorems:</b>
- DM is risk averse $\Leftrightarrow u$ concave
- DM is risk prone $\Leftrightarrow u$ convex
- DM is risk neutral $\Leftrightarrow u$ linear

![Risk concerns](https://media.springernature.com/full/nature-static/assets/v1/image-assets/nn0905-1129-F1.gif)

### Intensity of risk aversion

The expected utility theory takes into account that individuals may be risk-averse, meaning that the individual would refuse a fair gamble (a fair gamble has an expected value of zero). Thus yielding a concave utility function.

Let $L$ be a lottery with $(x_{i}, p_{i})_{i=1}^{n}$ and $L'$ a lottery judged indifferent to $L$ by the decision model ($z < \sum p_{i}x_{i}$)

The <u>risky component</u> of $L$ is $RC(L) = \sum p_{i}x_{i} - z$

The more intense the decision model risk aversion, the higher RC(L).

## Elicitation of utility functions

To understand and modelize the utility functions, we commonly refer to this set of teechniques:

| Point-wise techniques | Analytics techniques |
|:-----------------------------:|:--------------------------------------------------------------:|
| 50/50 lottery technique | $u(x) = (\frac{x-x^{*}}{x^{*}-x^{**}})^{\alpha}, \alpha > 0$ |
| Probability lottery technique | $u(x) = 1- e^{-\frac{x}{p}}, p > 0$ |

### Point-wise techniques

#### 50/50 lottery technique

<b>TL; DR:</b> Specify a point of the utility function by asking a 50/50 question to the decision model.

Specifically, we give a 50/50 lottery $L = (\{ a, b \}, \{ 0.5, 0.5 \})$ to the decision model and ask him to find the certain lottery $L' = (\{ y \}, \{ 1\})$ so that $L$ and $L'$ are indifferent (i.e. $L \succeq L'$)

$$
\begin{align}
L \succeq L' &\Leftrightarrow u(L) > u(L')\\
&\Leftrightarrow (a+b)/2 \geq u(y)
\end{align}
$$

However, instead of asking the decision model to return $y$, we use dichotomic search for each question $(a, b)$.

<b>Dichotomic algorithm to find $y$</b>

1. <u>Initialization:</u>
    - <i>Allocate list of lotteries</i>
    $(L_{i})_{i=0}^{n}$ with $L_{i} = (\{ y_{i} \}, \{ 1\})$ with $n$ large enough.
    - Set $L_{0} = (\{ a+b/2 \}, \{ 1\})$

2. <u>For $i$ in $\{1, ..., n\}$</u>
    - $y_{i} = u(L_{i}) > u(L) \Rightarrow y_{i+1} < y_{i}$
    - $y_{i} = u(L_{i}) < u(L) \Rightarrow y_{i+1} > y_{i}$

<b>Adding more points to $u$</b>

We can add more points to the curve by adding question with different $a$ and $b$.

#### Variable probability techniques

The framework is identical to the one above except that this time, $y$ is fixed and $p$ is to determine where $L = (\{a, b\}, \{1-p, p\})$. To find p, we proceed similarly than above.

### Analytic techniques : with different analytic forms

<b>Principes:</b>
1. Postulate a parametric form for the utility function.
2. Pose questions aiming at setting the values for the parameters
(of the parametric form).

#### A first parametric function

A frequently used parametric function is

$$u(x) = (\frac{x-x^{*}}{x^{*} - x^{**}})^{\alpha}$$

with $\alpha > 0$ and $x \in [x^{*}, x^{**}]$. As usual, $u(x^{*}) = 0$ and $u(x^{**}) = 1$

This parametric utility function can model risk averse and risk
prone behaviors.

![dm_parameteric_1](/images/dm_parameteric_1.png)


#### A second parametric function

Another common utility function is

$$
u(x) = 1 - e^{-\frac{x}{p}}
$$

This analytic form models risk averse behavior only.

![dm_second_parameteric](/images/dm_second_parameteric.png)

## Limits of utility theory

<b>Which criterion?</b> It is difficult to justify a decision criterion based on expected value for single shot decisions.

<b>Axioms</b> do not corresponds to actual decision behaviors.

<b>Empirical studies</b> show that decision models behavior are frequently:
- Risk averse for gains
- Risk prone for losses
- Risk-proneness is stronger in losses that risk-aversion in gains

# Sources

I wish to thank Vincent Mousseau, professor at Centrale-Supélec for his valuable teachings.

------
