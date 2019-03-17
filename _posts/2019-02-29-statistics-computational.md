---
title: 'Statistics basics'
date: 2018-12-01
permalink: /posts/2019/01/modeling-and-estimation/
tags:
  - Statistics
---

## 1. Simulations

### 1.1. Data generation

<b>TL; DR:</b> Based on two approaches
1. Inversion of CDF
1. Acceptance / Rejection method

### 1.2. Monte-Carlo methods

Based on SLLN + TCL and the main idea is to approximate $E[something]$ with a mean.

## 2. Gaussian mixture model

<b>Idea:</b> One aims at modelling the statistical behaviour from several populations, groups or classes.

<b>Notations:</b>
- $n$ observations of i.i.d. random variables/vectors, denoted $(X_{1},...,X_{n})$
- $K$ different clusters containing nk observations. Of course, $n = \sum_{k=1}^{K} n_{k}$
- $p_{k}$ the probability of belonging to the $k$th class and $f_{k}$ the PDF of r.v. in this class.

<b>Statistical modelling of a mixture:</b> with previous notations, one can defined the following PDF:

$$
\begin{align}
f(x) &= \sum_{k=1}^{K}p_{k}f_{k}(x)\\
&= \sum_{k=1}^{K}p_{k}\frac{1}{\srqt{2\pi\sigma_{k}^{2}} \text{exp}\Big( -\frac{(x-\mu_{k})^{2}}{2\sigma_{k}^{2}} \Big)\\
\end{align}
$$

But the problem is the estimation of many parameters: $\theta = (p_{k}, \mu_{k}, \sigma_{k})$ with $\sum p_{k} = 1$ and $\forall k \in \{1, ..., K \} \mu_{k} \in \mathbb{R}$ and $\sigma_{k} \in \mathbb{R}_{+}^{*}$

## 3. Gaussian mixture model simulation

We can simulate $f(x)$ using a latent variable $Z$ that corresponds to the class of the variable $X$. Now $(X, Z)$ is defined by:
- $Z$ follows a discrete distribution $(p_{1}, ..., p_{k})$ on $\{1, ..., K \}$ such that $\forall k$ one has

$$
P(Z = k) = p_{k}
$$

- $\forall k \in \{1, ..., K \}$, conditionally to $\{Z = k\}$, $X$ has a pdf $f_{k}$:

$$
\mathcal{L}(x \mid Z = k) = f_{k}(x)
$$

## 4. EM algorithm

<b>Theorem (ML estimates of $\theta$)</b> Let the observations (x_{i}, z_{i})_{i=1, ..., n} then $\forall k \in \{1, ..., K \}$ one has:

$$
\begin{align}
\hat{p}_{k} &= \frac{1}{n} \sum_{i=1}^{n}1_{z_{i} = k}\\
\hat{\mu}_{k} &= \frac{1}{n\hat{p}_{k}} \sum_{i \mid z_{i} = k} x_{i}\\
\hat{\sigma}_{k} &= \frac{1}{n\hat{p}_{k}} \sum_{i \mid z_{i} = k} (x_{i} - \hat{\mu}_{k})^{2}
\end{align}
$$

<b>General idea:</b> One only observes $(x_{1},...,x_{n})$ then analyse the log-likelihood but one can make assumptions of the unobserved data $(Z_{1}, ..., Z_{n})$

<b>Lemma (Conditional distribution of the Zi’s)</b> For $\theta \in \Theta, x \in \mathbb{R}$ and $k \in \{1, ..., K \}$ one has:

$$
P_{\theta}(Z=k\mid X = x) = \frac{p_{k}f_{k}(x)}{\sum_{l=1}^{K}p_{l}f_{l}(x)}
$$

There are several approaches to group the data:

1. [k-means] Assign a class to each $x_{i}$ according to

$$
z_{i} = \text{argmax}_{k} P_{\theta_{old}}(Z = k \mid X_{i} = x_{i})
$$

Natural approach but not flexible

2. [SEM] Randomly assign a class to each $x_{i}$ according to the distribution

3. [N-SEM] Randomly assign $N$ classes to each $x_{i}$

4. [EM] Limit of $N$ SEM when $N \rightarrow \infty$ Very flexible and robust!

###

------
