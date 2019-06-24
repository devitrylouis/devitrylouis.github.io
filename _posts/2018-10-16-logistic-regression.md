---
title: 'Logistic Regression'
date: 2018-10-16
permalink: /posts/2018/11/logistic-regression/
tags:
  - Machine Learning
---

<b>TL; DR:</b> Logistic Regression is a simple but oftentimes efficient algorithm that tackles binary classification.

## 1. Logistic regression

Its basic principle is to cast the result of a [least square regressor](/posts/2018/11/ml-linear-regression/) $\beta^{T}x$ through a sigmoïd function $g$, which squash the values toward $[0, 1]$:

$$ g(z) = \frac{1}{1+e^{-\beta x}} $$

![Sigmoïd function](https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Logistic-curve.svg/1200px-Logistic-curve.svg.png)

<i>Note:</i> The derivative $g'(z) = g(z)(1-g(z))$ has the obvious advantage of being analytical, thereby making computations much faster.

> <b>Probabilistic framework:</b> We endow our classification model with a set of probabilistic assumptions.
>
> $$ p(y\mid x;\beta) = h_{\beta}^{y}(x)(1-h_{\beta}(x))^{1-y} $$

By maximizing the log-likelihood for $m$ training examples, we obtain:

$$\beta := \beta + \alpha\nabla_{\beta}l(\beta)$$

TODO:
- Add derivation problem + sol.
- Add vectorization of the computations
- Precise terminology used for the formula

<b>Stochastic gradient ascent rule:</b>

$$
\beta_{j} := \beta_{j} + \alpha(y^{(i)}-h_{\beta}(x^{(i)}))x_{j}^{(i)}
$$

<i>Notes:</i>
- The perceptron, is the logistic regression when you “force” its output values to be either $0$ or $1$ or exactly.

# Newton method

<b>Newton's algorithm:</b> For a function $f : \mathbb{R} \rightarrow \mathbb{R}$ we want to minimize at $\beta: f(\beta) = 0$, we start at an initial value $\beta$ and iterate:

$$ \beta := \beta - \frac{f(\beta)}{f'(\beta)} $$

<b>Key idea:</b> If we want to maximize some function, use Newton's algorithm with the derivates to find the maximum:

$$ \beta := \beta - \frac{l'(\beta)}{l''(\beta)} $$

<b>Newton-Raphson method (Multidimensional setting):</b>

$$
\beta := \beta - H^{-1}\nabla_{\beta}l(\beta)
$$

where $H$ is the [Hessian matrix matrix](https://en.wikipedia.org/wiki/Hessian_matrix).

<b>Notes:</b>
- Newton’s method typically enjoys faster convergence than (batch) gradient descent
- Because of the inverse Hessian, Newton Method is more expensive than gradient descent.
- When Newton’s method is applied to maximize the logistic regres- sion log likelihood function l(θ), the resulting method is also called Fisher scoring.


# Sources

- [CS229 Lecture notes by Andrew Ng](https://see.stanford.edu/materials/aimlcs229/cs229-notes1.pdf)
[C++ implementation](https://czep.net/stat/mlelr.pdf)

------
