---
title: 'Optimizing Deep Learning'
date: 2018-12-01
permalink: /posts/2018/11/optimize-dl/
tags:
  - Deep Learning
---

First-order methods: gradient descent and variants.

# Topology

<b>Saddle Points:</b> In high dimensions, saddle points are more likely than local minima as some eigenvalues are positive, some are negative.

For $\theta^{*}$ to be a local minimum, we need:
- \mid\mid \frac{\partial J}{\partial \theta} (\theta^{*}) \mid\mid = 0
- All eigenvalues of $\frac{\partial^{2}J}{\partial \theta^{2}}(\theta^{*})$ are positive

For random functions in n dimensions, the probability for all the eigenvalues to be all negative is $1 / n$.

# Gradient descent

## Back propagation

## Stochastic Gradient Descent

## Momentum

## Adagrad

## RMSProp

## Adam



------
