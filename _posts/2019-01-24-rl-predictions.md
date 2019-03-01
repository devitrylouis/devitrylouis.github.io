---
title: 'Predictions in Reinforcement Learning'
date: 2018-12-01
permalink: /posts/2019/01/rl-prediction/
tags:
  - Reinforcement learning
---

In a model-free setting, the transition probabilities are unknown and the agent must interact with the environment. An additional challenge is the possibility that the control policy is different to the one to estimate. This is called off-policy but we will focus on on-policy in this blogpost. We will leverage a simulator and a policy $\pi$ - coupled with our knowledge of $S, A, \gamma$ to run episodes and improve the latter from sampled data.

There are mainly four techniques, in increasing order of performance:
1. MC methods
    * Stochastic approximations
    * Monte Carlo learning
3. Temporal differences: quite useful in dealing with non Markovian processes
    * $TD(0)$
    * $TD(\lambda)$

In the previous blogposts, we went though the following topics:
- Dynamic Programming
- Solving explicitly MDPs via Tpi , T*

## 1. MC methods

The main principle behind MC method is to take simulations, record the value functions along the way and average estimates afterwards. Mathematically, we sample the samples $X_{1}, ..., X_{n}$ (those are our value functions) and we compute the expectancy over all samples:

$$ \mathbb{E}(X) \approx \frac{1}{n}\sum_{i=1}^{n}X_{i} $$

This is most valid when the assumptions that $X_{1}, ..., X_{n}$ are i.i.d. strong, as we obtain:

$$ \frac{1}{n}\sum_{i=1}^{n} X_{i} \rightarrow \mathbb{E}(X_{1}) \text{ a.s.} $$

where we used the notion of almost sure convergence:

$$\mathbb{P}(lim_{n\rightarrow \infty} X_{n} = X) = 1$$

I refer you to this [statistics blogpost](/posts/2019/01/statistics-basics/) for more details.

## 1.1. Stochastic approximation

> TODO: Goal of stochastic approximations: $$f(\theta^{*}) = 0$$

Some common methods used are incremental means and Stochastic Gradient Descent.

- <b>Incremental means:</b> is simply a running averaging on the i.i.d. sampled values $X_{1}, ..., X_{n}$:

$$ \mu_{n+1} = \big( 1 - \frac{1}{n+1} \big)\mu_{n} + \frac{1}{n+1}X_{n} $$

By assuming the stationarity and taking the expectation:
$$ \mathbb{E}[\mu_{n}] = \mathbb{E}[X_{n}]$$

- <b>SGD</b> is performed as such:
$$
\begin{align}
\theta_{n+1} &= \theta_{n} - \frac{1}{n} \nabla f(\theta_{n})\\
\theta_{n+1} &= (1- 1/n)\theta_{n} + \frac{1}{n} (\theta_{n} - \nabla f(\theta_{n}))\\
\end{align}
$$

And once again, stationarity is assumed and we obtain:

$$ f: \mathbb{E}[F(\theta)] = f(\theta) $$

### 1.2. Robbins Monro conditions

A step size $\eta_{n} \geq 0$ is said to satisfy the Robbins-Monro conditions if:

$$
\sum_{n=0}^{\infty} \eta_{n} = \infty \text{ but }\sum_{n=0}^{\infty} \eta_{n}^{2} < \infty
$$

which just means "large but not too large". In practice, the following ones are used:

- $\frac{1}{n^{\alpha}}$
- $\frac{1}{2}\leq \alpha \leq 1$

### 1.3. Stochastic approximations of fixed points

In our setting, we want to find the fixed point $V^{\text{*}}$ of the Bellman operator $\mathcal{T}$ (refer to past blogpost) using a noisy estimate $\hat{\mathcal{T}}V = \mathcal{T}V + b$. More precisely, we want to solve:

$$ V_{n+1} = (1-\eta_{n})V_{n} + \eta_{n}\hat{\mathcal{T}}V_{n} $$

To do so, let's consider the [filtration](https://en.wikipedia.org/wiki/Filtration_(mathematics)) $\mathcal{F} = \{ V_{0}, ..., V_{n}, b_{0}, b_{n} \}$ and the following assumptions:

1. <b>Noise is ok!</b> $\mathbb{E}[b_{n}| \mathcal{F}_{n}] = 0$
2. <b>Large noise is $\mathcal{O}(V_{n})$</b> $\exists K: \forall n, \mathbb{E}[||b_{n}||^{2} | \mathcal{F}_{n} ] < K(1+||V_{n}||)$
3. <b>Large but not too large:</b> $\{ \eta_{n} \}_{n\in \mathbb{N}}$ satisfies the Robbins-Monro conditions

With all of the above holding, we have our desired convergence:

$$
V_{n} \rightarrow V^{*} \text{ a.s. }
$$

## 2. Monte-Carlo Learning

Works in sequential and finite episode setting. An episode is said to be finite when a terminal state is reached? It's possible to have $\gamma = 1$

Monte-Carlo has no bias but variance.


Any episode is a sub-episode

We do kind of a bootstrapping

First visit MC: Use only the first sub-episode to visit a state (no bias but variance)

N is a counter that helps average the expected score

Every visit MC

## 3. Temporal difference learning

### 3.1. TD(0)

From epiosde $N$ to $N+1$

At each episode $N$, build $V_{N}$. At a state $k$, we compute the TD error:

$$
\delta_{k} = R_{k} + \gamma V_{n}(S_{k+1}) - V_{N}(S_{k})
$$

with V_{n}(S_{k+1}) is a biased estimate of the future reward.

Define $$V_{n+1}(S_{k}) = V_{n}(S_{k}) + \mu_{N}\delta_{k}$$

then

$$
V_{n} \rightarrow v^{\pi}
$$


### 3.1. $TD(\lambda)$

MC TD(0) TABLE

Can we get a trade off of the two? Yes! It is $TD(\lambda)$

<u>\mathcal{T}_{\lambda}^{\pi} = (1- \lambda) \sum_{m\geq 0}\lambda^{m
(\mathcal{T}^{\pi})^{m+1

Stochastic approximation theorem

This algorithm converges to a fixed point (DEMO)

Implementation with trace:

------
