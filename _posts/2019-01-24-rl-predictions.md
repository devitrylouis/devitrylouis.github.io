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

Goal of stochastic approximations: $$f(\theta^{*}) = 0$$

But we only have an estimate of $f: \mathbb{E}[F(\theta)] = f(\theta)$

Stochstic approximation consists in finding $G$:

$$
\theta_{n+1} = G(\theta_{n}) \Rightarrow \theta_{n} \rightarrow \theta^{*}
$$

with $\theta_{n}$ being a random variables.

Examples:
- Incremental means
- Stochastic gradient descent

Robbins Monro conditions:

A step size $\mu_{n} \geq 0$ is said to satisfy the RobbinsMonro conditions if:

$$
\sum_{n=0}^{\infty}
$$

### 1.1. Stochastic approximations of fixed points

Let /mathcal{T} be a contraction with fixed point V^{*}

Assume we have access to a noisy estimates of \mathcal{T}V = \mathcal{T}V + b

and let \mathcal{F}_{n} = {V0, ..., b0, ...bn}

Consider V_{n+1} = (1-\mu_{n})V_{n}

Three assumptions: \Rightarrow V_{n} \rightarrow_{n \rightarrow \infty} V

Goal: Design of the sequences.

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
