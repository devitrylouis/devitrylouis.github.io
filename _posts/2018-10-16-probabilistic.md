---
title: 'Probabilistic classifiers'
date: 2018-10-16
permalink: /posts/2018/11/probabilistic/
tags:
  - Machine Learning
---
# Generative Learning algorithms

<b>Discriminative learning algorithms</b> Algorithms that try to learn p(y|x) directly (such as logistic regression), or algorithms that try to learn mappings directly from the space of inputs X to the labels {0, 1}, (such as the perceptron algorithm).

<b>Generative learning algorithms:</b> Algorithms that instead try to model p(x|y) (and p(y)).

<b>Bayes:</b> After modeling the <i>class priors</i> $p(y)$ and $p(x|y)$, our algorithm, we can then use Bayes rule to derive the posterior distribution on y$ given $x$

$$
p(y|x) = \frac{p(x|y)p(y)}{p(x)}$$

<i>Note:</i> $p(x) = p(x|y = 1)p(y = 1) + p(x|y = 0)p(y = 0)$

Actually, if were calculating $p(y|x)$ in order to make a prediction, then we don’t actually need to calculate the denominator:

$$
\begin{align}
\text{arg max}_{y}p(y\mid x) &= \text{arg max}_{y} \frac{p(x\mid y)p(y)}{p(x)}\\
&= \text{arg max}_{y} p(x\mid y)p(y)
\end{align}
$$

# Gaussian Discriminant Analysis

<b>Context:</b> $p(x|y)$ is distributed according to a multivariate normal distribution.

## The multivariate normal distribution

<b>Multivariate normal distribution</b> in $n$-dimensions is parameterized by a mean vector $\mu ∈ \mathbb{R}^{n}$ and a covariance matrix $\Sigma ∈ \mathbb{R}^{n\times n}$, where $\Sigma \geq 0$ is symmetric and positive semi-definite:

$$
p(x; \mu, \Sigma) = \frac{1}{(2\pi)^{n/2}\mid \Sigma\mid^{1/2}}exp(-\frac{1}{2}(x-\mu)^{T}\Sigma^{-1}(x-\mu))
$$

<b>Covariance:</b> of a vector-valued random variable $Z$ is defined as $Cov(Z) = E[(Z − E[Z])(Z − E[Z])^{T} ]$.

<i>Note:</i> Equivalently $Cov(Z) = E[ZZ^{T}] − (E[Z])(E[Z])^{T}$

<b>Takeway:</b> $X ∼ N (\mu, \Sigma) \Rightarrow Cov(X) = \Sigma$

## The Gaussian Discriminant Analysis model

Assume our data obey to the following:

$$
\begin{align}
y &\sim Bernoulli(\phi)\\
x\mid y=0 & \sim \mathcal{N}(\mu_{0},\Sigma)\\
x\mid y=1 & \sim \mathcal{N}(\mu_{1},\Sigma)
\end{align}
$$

<b>Best parameters (Log likelihod estimation)</b>

$$
\begin{align}
\phi &= \frac{1}{m}\sum_{i=1}^{m}1_{\{ y^{(i)}=1 \}}\\
\mu_{0} &= \frac{\sum_{i=1}^{m}1_{\{ y^{(i)}=0\}}x^{(i)}}{\sum_{i=1}^{m}1_{\{ y^{(i)}=0\}}}\\
\mu_{1} &= \frac{\sum_{i=1}^{m}1_{\{ y^{(i)}=1\}}x^{(i)}}{\sum_{i=1}^{m}1_{\{ y^{(i)}=1\}}}\\
\Sigma &= \frac{1}{m} \sum_{i=1}(x^{(i)}-\mu_{y^{(i)}})(x^{(i)}-\mu_{y^{(i)}})^{T}
\end{align}
$$

## Discussion: GDA and logistic regression

<b>Link to logistic regression</b> If we view the quantity $p(y = 1|x; \phi, \mu_{0}, \mu_{1}, \Sigma)$ as a function of x, then we find that:

$$
p(y = 1|x; \phi, \mu_{0}, \mu_{1}, \Sigma) = \frac{1}{1+exp(-\beta^{T}x)}
$$

where $\beta$ is some appropriate function of $\phi, \Sigma, \mu_{0}, \mu_{1}$.

<b>Result:</b> $p(x|y)$ is multivariate gaussian (with shared $\Sigma$) $\Rightarrow p(y|x)$ follows a logistic function.

<i>Notes:</i>
1. Assumptions:
    * GDA makes stronger modeling assumptions about the data than does logistic regression.
    * When these modeling assumptions are correct, GDA is [asymptotically efficient](https://www.encyclopediaofmath.org/index.php/Asymptotically-efficient_estimator).
    * Even for small training set sizes, we would generally expect GDA to better
    * With weaker assumptions, logistic regression is more robust.
2. Non-Gaussian data:
    * Logistic regression also work well on Poisson data like this.
    * GDA don't work well with non gaussian data.

------
