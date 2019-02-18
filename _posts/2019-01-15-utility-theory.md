---
title: 'Utility  theory'
date: 2018-12-01
permalink: /posts/2019/01/utility-theory/
tags:
  - Decision Modeling
---

This blogpost is the first one of a series, whose aim is to both introduce what is Decision Modeling and build the corresponding mathematical framework. Decisions model are very important - particularly in business - as they reduce stress and deal with uncertainty. Supported by ever increasing amounts of data and sophisticated algorithms, their growing power have captured plenty of C-suite attention in the recent years. From very accurate predictions to guiding knotty optimization choices, decisions models are essential and worthy of interest.

## 1. Introduction

### 1.1. Uncertainty

In many decision situations, a part of the informations is not known in advance and to a various degree:
- <i>Deterministic situations:</i> Data are known in advance (classical O.R., Lin. Prog., Graph theory, ...),
- <i>Situation stochastic situation:</i> Data are not known in advance, but probability distributions can be hypothetized
- <i>Situation competitive situation:</i> Data involved in the decision depend on exogenous actions (game theory, ...)
- <i>Complete uncertainty:</i> Data of the decision problem are not known in advance, and no probability distribution can be determined.

As a palliative, we introduce in this blogpost the fundamental principles of utility theory:

> Utility theory bases its beliefs upon individuals’ preferences. It is a theory postulated in neo-classical economics to explain behavior of individuals based on the premise people can consistently rank order their choices depending upon their preferences.

### 1.2. criteria for choice under uncertainty

Before giving some criterions used to deal with uncertainty, let's model our problem with:
- <u>States of nature</u>: $\Theta = \{ \theta_{1}, ..., \theta_{n} \}$
- <u>Possible decisions</u>: $\mathcal{D} = \{ d_{1}, ..., d_{n} \}$

In simple settings, a basic approach to find a good decision consists of the prior computing of a matrix of all possible outcomes:

- <u>Outcome matrix</u>: $r(d_{i} \mid \theta_{j})$ outcome of decision $d_{i}$ if the state of nature $\theta_{j}$ intervenes.

Once this matrix is computed, we make use of the following criterions:

| Laplace criterion | Wald criterion | Savage criterion |
|:--------------------------------------------------------------------------:|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| $\text{Max}_{d_{i}\in\mathcal{D}}\sum_{j=1}^{n}r(d_{i}\mid \theta_{j})$ | $\text{Max}_{d_{i}\in \mathcal{D}}\text{ Min}_{\theta_{j}}r(d_{i}\mid\theta_{j})$ | $\text{Max}_{d_{i}\in \mathcal{D}}\text{Min}_{\theta_{j}}\text{regret}(d_{i},\theta_{j})$ |
| Equiprobability of states | Max Min prudence | Min Max regret |

where $regret(d_{i}, \theta_{j})$ is the regret of decision $d_{i}$ for the state of nature $\theta_{j}$, i.e. the difference of outcome between the best decision for $\theta_{j}$ and $r(d_{i}, \theta_{j})$.

## 2. Comparing lotteries

Utility theory is a cornerstone of decision modelling and was introduced by [Von Neuman, Morgenstern 1947]. It stipulates that one should manage the risk by constructing lotteries: a distribution of outcome evaluated by their utility.

The goal of this section is to address the properties of such lotteries. To do so, we will:
1. Define some axioms that gives a structure / order of the lotteries
2. Define the utility function and state its important properties
3. Describe how the utility function is related to risk

### 2.1. The von Neumann–Morgenstern axioms

Utility theory is grounded on the following set of axioms, which aims to define a rational decision maker.

1. <b>Completeness $A_{1}$:</b> assumes that an individual has well defined preferences and can always decide between any two alternatives. The preferences are expressed by the relation $A\succeq B$ where A and B are two preferences. (what about $I$ and $P$?)

2. <b>Transitivity $A_{2}$:</b> If $A\succeq B$ and $B\succeq C$ then $A\succeq C$

3. <b>Independence $A_{3}$:</b> Assumes that two gambles mixed with an irrelevant third one will maintain the same order of preference as when the two are presented independently of the third one. It is the most controversial axiom. Let $A$, $B$ and $C$ be three lotteries with $A\succeq B$ and let $t$ be the probability that a third choice is present ($t\in [0,1]$). If $tA + (1-t)B \succeq tB + (1-t)C$ then the order of preference for $A$ before $B$ holds, independently of the presence of irrelevant choice $C$.

4. <b>Continuity $A_{4}$:</b> Let $A$, $B$ and $C$ be lotteries with $A\succeq B\succeq C$ then there exists a probability $p$ such that $B$ is equally good as $pA+(1-p)C$.

Some of these assumptions are stronger than others (3. and 4.) and are therefore inapplicable for a given problem. Nonetheless, if the first two axioms are valid, we say that there is a weak order on the lotteries.

### 2.2. Utility function

The lotteries introduced above are rather abstract. A practical way to compare two lotteries A and B (i.e. figure out if $A\succeq B$) is to make use of the expected utility.

> <u>Expected utility:</u> The utility of a lottery $L$ is the expected utility of its outcomes: $$u(L) = \sum_{i = 1}^{n} p_{i}u(x_{i})$$
> where $u$ is the utility function.

Under the aforementionned axioms, one can show that there exists a function $u$ representing the decision model preferences and this function is unique up to an affine transformation $(\alpha u + \beta)$. This function is useful because it satisfy:

$$ L\succeq L' \Leftrightarrow u(L) > u(L') $$

### 2.3. Utility function and risk

A utility function $u:X \mapsto \mathbb{R}$ maps possible outcomes to a utility (the higher the better), so that the following is satisfied:
- Scaling: for $X = [x, x^{ * }]$, $u$ must verify $u(x) = 0$ and $u(x^{ * }) = 1$
- Monotonically increasing: $x < y \Leftrightarrow u(x) < u(y)$

As it turns out, depending on the "mindset" of the decision model (is he risk averse or risk prone), the utility function will ahbor different shapes. Specifically, a decision model is said to be risk averse if he prefers any expected outcome of a sure lottery $L_{\text{known}}$ to $L_{\text{unknown}}$. When this is the case, it will favor low outcomes by associating them higher utilities.

In general, one can show the following <b>theorem</b>:
- Decision Model is risk averse $\Leftrightarrow u$ concave
- Decision Model is risk prone $\Leftrightarrow u$ convex
- Decision Model is risk neutral $\Leftrightarrow u$ linear

Here is an illustration of this principle:

![Risk concerns](https://media.springernature.com/full/nature-static/assets/v1/image-assets/nn0905-1129-F1.gif)

The risk-aversion means that $u(L_{\text{known}}) > u(L_{\text{unknown}})$ and the bigger the gap between the two, the more averse to risk the DM is. This motivates the construction of the risky component $RC(L_{\text{unknown}})$:

$$RC(L_{\text{unknown}}) = u(L_{\text{known}}) > u(L_{\text{unknown}})$$

## 3. Elicitation of utility functions

Utility or preference elicitation is a process of assessing preferences and the attitude to risk of a decision maker or, more precisely, utility functions. During this stage, the decision analyst asks various queries in an attempt to model a utility function, specific for the decision maker's preferences.

| Point-wise techniques | Analytics techniques |
|:-----------------------------:|:--------------------------------------------------------------:|
| 50/50 lottery technique | $u(x) = (\frac{x-x^{ * }}{x^{ * }-x^{ ** }})^{\alpha},\alpha > 0$ |
| Probability lottery technique | $u(x)=1-e^{-\frac{x}{p}},p>0$ |

### 3.1. Point-wise techniques

In order to derive a utility function to represent the decision maker's attitude to risk, first we need to rank all the outcomes from the best to the worst and assign a utility of $1$ to the best and $0$ to the worst. According to von Neumann and Morgestern theory, the main idea is to have the decision maker stating preferences over lotteries, or gambles; then utilities are calculated reasoning backwards. In other words, if we find two gambles that are equally attractive, we can equalize the expected utilities. In this way, if two utilities are known, also the third will be known.

Point wise techniques leverage this by producing sequentially points on the utility functions.

<b>50/50 lottery technique</b>

<b>TL; DR:</b> Specify a point of the utility function by asking a 50/50 question to the decision model.

Specifically, we give a 50/50 lottery $L = (\{ a, b \}, \{ 0.5, 0.5 \})$ to the decision model and ask him to find the certain lottery $L' = (\{ y \}, \{ 1\})$ so that $L$ and $L'$ are indifferent (i.e. $L \succeq L'$)

$$
\begin{align}
L \succeq L' &\Leftrightarrow u(L) > u(L')\\
&\Leftrightarrow (a+b)/2 \geq y
\end{align}
$$

However, instead of asking the decision model to return $y$, we use the fact that $u$ is montone to perform dichotomic search for each question $(a, b)$.

<b>Find ONE point with Dichotomic algorithm</b>

1. <u>Initialization:</u>
    - <i>Allocate list of lotteries</i>
    $(L_{i})_{i=0}^{n}$ with $L_{i} = (\{ y_{i} \}, \{ 1\})$ with $n$ large enough.
    - Set $L_{0} = (\{ a+b/2 \}, \{ 1\})$

2. <u>For $i$ in $\{1, ..., n\}$</u>
    - $y_{i} = u(L_{i}) > u(L) \Rightarrow y_{i+1} < y_{i}$
    - $y_{i} = u(L_{i}) < u(L) \Rightarrow y_{i+1} > y_{i}$

To find <b>more points to $u$</b>, we repeat this with different values for question $(a, b)$.

<b>Variable probability techniques</b>

The framework is identical to the one above except that this time, $y$ is fixed and $p$ is to determine where $L = (\{a, b\}, \{1-p, p\})$. To find $p$, we proceed similarly than above.

### 3.2. Analytic techniques

The basic principle of analytical techniques is the following:
1. Postulate a parametric form for the utility function. The two must common are listed in the table below:

| Parametric function 	| $u_{\alpha}(x)=(\frac{x-x^{ * }}{x^{ ** }-x^{ * }})^{\alpha}$ 	| $u_{p}(x)=1-e^{-\frac{x}{p}}$ 	|
|:-------------------:	|:-------------------------------------------------------:	|:-----------------------------:	|
| Models 	| Risk prone and averse 	| Risk averse 	|
| Parameters 	| $\alpha>0$ 	| $p>0$ 	|

2. Pose questions aiming at setting the values for the parameters
of the parametric form. The proceeding is very similar to the point-wise technique.

## 4. Limits of utility theory

Despite the great properties presented in this blogpost, some issues arise:
- <b>Which criterion?</b> It is difficult to justify a decision criterion based on expected value for single shot decisions.
- <b>Axioms</b> sometimes do not corresponds to actual decision behaviors.
<b>Empirical studies</b> show that decision models behavior are frequently:
- Risk averse for gains
- Risk prone for losses
- Risk-proneness is stronger in losses that risk-aversion in gains

Some techniques exist to mitigate this issues. They will be presented in the upcoming blogpost.

# Sources

This blogpost is heavily inspired from [Vincent Mousseau](https://www.researchgate.net/profile/Vincent_Mousseau) lectures, my professor at Centrale-Supélec. 

Beside, the following ressources proved useful:

- [Utility](https://en.wikipedia.org/wiki/Utility)
- [Blogpost risk](https://saylordotorg.github.io/text_risk-management-for-enterprises-and-individuals/s07-03-choice-under-uncertainty-expec.html)
- [McKinsey report](https://www.mckinsey.com/business-functions/strategy-and-corporate-finance/our-insights/the-benefits-and-limits-of-decision-models)

------
