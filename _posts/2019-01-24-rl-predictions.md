---
title: 'Predictions in Reinforcement Learning'
date: 2018-12-01
permalink: /posts/2019/01/rl-prediction/
tags:
  - Reinforcement learning
---

<b>Setting:</b> No access to the transition probabilities and on-policy.

<b>Goal:</b> Find estimates of the value function:
1. Monte Carlo based
  - Stochastic approximations:
  - MC Learning
2. Temporal differences: quite useful in dealin with non Markovian processes
  - $TD(0)$
  - $TD(\lambda)$

Necessarily need to interact to get some sense of the environment.

<b>On policy / off policy?</b>
- <u>On policy:</u> the control policy is the same as the one to preduct
- <u>Off policy:</u> the control policy can be different to the one to estimate

Today: on policy

Input: No p yet a simulator and a policy \pi
Output: a prediction. How can we estimate $v^{\pi}$

We allow to play as much episodes as necessary

Large lookup tables.

## Stochastic aproximation

Convergence almost surely:
$$\mathbb{P}(lim_{n\rightarrow \infty} X_{n} = X) = 1$$



where we note $X$

Monte Carlo methods: Sample some random variables to get an estimate of some expectation. Using MC variations, we will estimate the Q-funtion.

Goal of stochastic approximations:

$$f(\theta^{*}) = 0$$

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

### Stochastic approximations of fixed points

Let /mathcal{T} be a contraction with fixed point V^{*}

Assume we have access to a noisy estimates of \mathcal{T}V = \mathcal{T}V + b

and let \mathcal{F}_{n} = {V0, ..., b0, ...bn}

Consider V_{n+1} = (1-\mu_{n})V_{n}

Three assumptions: \Rightarrow V_{n} \rightarrow_{n \rightarrow \infty} V

Goal: Design of the sequences.

### Monte-Carlo Learning

Works in sequential and finite episode setting. An episode is said to be finite when a terminal state is reached? It's possible to have $\gamma = 1$

Monte-Carlo has no bias but variance.


Any episode is a sub-episode

We do kind of a bootstrapping

First visit MC: Use only the first sub-episode to visit a state (no bias but variance)

N is a counter that helps average the expected score

Every visit MC

### Temporal difference learning

### TD(0)

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


### $TD(\lambda)$

MC TD(0) TABLE

Can we get a trade off of the two? Yes! It is $TD(\lambda)$

<u>\mathcal{T}_{\lambda}^{\pi} = (1- \lambda) \sum_{m\geq 0}\lambda^{m
(\mathcal{T}^{\pi})^{m+1

Stochastic approximation theorem

This algorithm converges to a fixed point (DEMO)

Implementation with trace:

##### Useful inequality

------
