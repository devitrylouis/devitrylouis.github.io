---
title: 'Statistics basics'
date: 2018-12-01
permalink: /posts/2019/01/statistics-basics/
tags:
  - Statistics
---

## 1. Convergence of random variables

### 1. What is a random variable?

Random variables are central objects in statistics and probabilities because they are applications $X: \Omega \to E$, where the codomain $\Omega$ is the set of eventualities and the codomain $E$ is a measurable space. Usually $X$ is real-valued (i.e. $E=\mathbb{R}$).

<b>Probability / distribution of a RV:</b> Depending on the type of $X$, wa can equip it with a probability distribution:
- <u>Discrete:</u> $P(X = x)$ or $P_{\theta}(X =x)$
- <u>Continuous:</u> $f(x)$ or $f_{\theta}(x)$

<b>Mean / variance of a RV:</b> $\mathbb{E}[X]$ or $E_{\theta}[X]$ (resp. $V[X] / V_{\theta}[X]$) stands for the statistical expectation (resp. the variance)

<b>What are i.i.d. RV?</b> Independent and Identically Distributed means that $X$ and $Y$ come from the same distribution. We note this $X ⊥ Y$ and a criterion to check whether $X ⊥ Y$ is: for any measurable functions $h$ and $$,

$$ \mathbb{E}[g(X)h(Y)]=\mathbb{E}[g(X)]\mathbb{E}[h(Y)] $$

<i>Additional terminology</i> PDF, CDF and iff resp. means Probability Density Function, Cumulative Distribution Function and “if and only if’’

### 1.2. Convergences of the multivariate case

Let $(x_{n})_{n\in\mathbb{N}} \in \mathbb{R}^{d}$ a sequence of r.V. and $\textbf{x} \in \mathbb{R}^{d}$:

<b>Almost sure convergence:</b> This is the type of stochastic convergence that is most similar to pointwise convergence known from elementary real analysis.

$$x_{n} \xrightarrow[]{\text{a.s.}} x \Leftrightarrow \exists N \in \mathcal{A} \text{ such that } P(N) = 0, \forall \omega \in N^{c}, \text{lim} x_{n}(\omega) = x(\omega)$$

This means that the values of $n$ approach the value of $X$, in the sense (see almost surely) that events for which $X_{n}$ does not converge to $X$ have probability $0$. Using the probability space $(\Omega ,\mathcal {F}, \text{P})$ and the concept of the random variable as a function from $\Omega \text{ to } \mathbb{R}$, this is equivalent to the statement

$$ \operatorname{P}\Big( \omega \in \Omega : \lim_{n \to \infty} X_n(\omega) = X(\omega) \Big) = 1.$$

<b>Convergence in probability:</b> The probability of an unusual outcome gets smaller as $n$ increases. Mathematically, this translates to:

$$
x_{n} \xrightarrow[]{P} x \Leftrightarrow \forall \epsilon > 0 \text{lim}_{n\rightarrow \infty} \mathbb{P}(|| x_{n} - x || \geq \epsilon)
$$

<b>Convergence in $L^{p}$:</b> if the expectation of the $L^{p}$ norm converges towards 0.

$$
x_{n} \xrightarrow[]{\mathcal{L}^{p}} x \Leftrightarrow \mathbb{E}\big[ || x_{n} - x ||^{p} \big] \rightarrow 0
$$

<b>Convergene in distribution:</b> A sequence of random variables converges in distribution if for any continuous and bounded functions $g$, one has:

$$
\text{lim}_{n/rightarrow \infty} \mathbb{E}[g(x_{n})] = \mathbb{E}[g(x)]
$$

<i>Note:</i> The CV in distribution of a sequence of r.V. is stronger than the CV of each component!

## 2. Cornerstone results

### 2.1. Convergence characterization

How to characterise the CV in distribution?

> TODO: <u>Characteristic fonction:</u>

<b>Theorem (Levy continuity Theorem)</b> Let $\phi_{n}(u) = \mathbb{E}(\text{exp}(iu^{t}x_{n}))$ and $\phi(u) = \mathbb{E}(\text{exp}(iu^{t}x)$ the characteristic functions of $x_{n}$ and $x$. Then:

$$
x_{n} \xrightarrow[dist]{} x \Leftrightarrow \phi_{n}(u) \rightarrow \phi(u) \forall u \in \mathbb{R}^{d}
$$

<b>Proposition (a.s., P, dist. convergences)</b> If $x_{n} \rightarrow x$ then $h(x_{n})\rightarrow h(x)$ if $h$ is a continuous function.

### 3.2. SLLN and CLT

<b>Theorem</b> Let $(x_{n})$ a sequence of iid rV in $\mathbb{R}^{d}$ such that $\mathbb{E}[|x_{1}|] < +\infty$. Let $\mu = \mathbb{E}[X_{1}]$ the expectation of $x_{1}$. Then:

$$
\hat{x_{n}} = \frac{1}{n} \sum_{i=1}^{n} x_{i} \xrightarrow[a.s.]{} \mu
$$

<b>Central limit theorem:</b> Let $x_{n}$ a sequence of iid rV in $R^{d}$ s.t. $\mathbb{E}[|x_{1}|^{2}] < \infty$. Let $\mu = \mathbb{E}[x_{1}]$ and $\sigma = \mathbb{E}[x_{1}^{t}x_{1}] - \mathbb{E}[x_{1}]\mathbb{E}[x_{1}]$ the convariance matrix of $x_{1}$. If we let $\hat{x_{n}} = \frac{1}{n}\sum_{x_{i}}$ the empirical mean then we obtain:

$$
\sqrt{n}(\hat{x_{n}} - \mu) \xrightarrow[]{\text{dist}} \mathcal{N} (0, \Sigma)
$$

### 3.2. Slutsky theorem

In probability theory, Slutsky's theorem extends some properties of algebraic operations on convergent sequences of real numbers to sequences of random variables.

<b>Slutsky theorem:</b> Let $(x_{n})_{n\in \mathbb{N}^{\text{*}}}$ a sequence of r.V. in $\mathbb{R}^{d}$ that converges in distribution to $x$. Let $(y_{n})_{n\in \mathbb{N}^{\text{*}}}$ a
sequence of r.V. in $\mathbb{R}^{m}$ (defined on the same proba. space as $(x_{n})_{n\in \mathbb{N}^{\text{*}}}$ that
converges almost surely (or in P, or in dist.) towards a constant a. Thus, the sequence
dist . $(x_{n},y_{n})_{n\in \mathbb{N}^{\text{*}}}$ converges in distribution towards $(x,a)$:

$$ (x_{n},y_{n})\xrightarrow[]{dist}(x,a)$$

<b>Important applications of Slutsky theorem:</b>
- <u>Sum:</u> $x_{n} + y_{n} \xrightarrow[]{dist} x + a \text{ if } m=d$
- <u>Product:</u> $x_{n} \cdot y_{n} \xrightarrow[]{dist} x \cdot a \text{ if } m=1$
- <u>Division:</u> $x_{n}/y_{n} \xrightarrow[]{dist} x/a \text{ if } m=1 \text{ and } a \neq 0$

### 3.4. Delta method

<b>Delta method:</b> The delta method is a general method for deriving the variance of a function of asymptotically normal random variables with known variance.

Let $(x_{n})_{n\in \mathbb{N}^{\text{*}}}$ a sequence of r.V. in $\mathbb{R}^{d}$ and $\theta$ a deterministic vector of $\mathbb{R}^{d}$. Let $h:\mathbb{R}^{d} \mapsto \mathbb{R}^{m}$ a function that is differentiable (at least) at point $\theta$.

Let us denote $\frac{\partial h}{\partial \theta^{t}}$ the $m \times d$ matrix such that:

$$
\big(\frac{\partial h_{i}}{\partial \theta_{j}}(\theta)\Big)_{1 \leq i \leq m\, \ 1 \leq j \leq d}
\text{ and }
\frac{\partial h^{t}}{\partial\theta} = (\frac{\partial h}{\partial\theta^{t} })^{t}
$$

<u>Assumption:</u>
$$ \sqrt{n}(x_{n} - \theta) \xrightarrow[]{dist}x $$

<b>Result:</b>

$$
\sqrt{n}(h(x_{n}) - h(\theta)) \xrightarrow[]{dist}\frac{\partial h}{\partial \theta^{t}}(\theta)x
$$

<i>Note:</i> There is a particular case if $x \sim N(0, \Sigma)$ then
$$
\sqrt{n}(h(x_{n}) - h(\theta)) \xrightarrow[]{dist} N(0, \frac{\partial h}{\partial \theta^{t}} \Sigma \frac{\partial h^{t}}{\partial \theta})
$$

## 4. Gaussian related distributions

### 4.1. Gamma and Beta distribution

------
