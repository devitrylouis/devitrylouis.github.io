---
title: 'Introduction to optimization'
date: 2018-10-01
permalink: /posts/2018/11/optimization-basics/
tags:
  - Optimization
  - Basics
---

Gentle introduction to the convexity, derivatives and the taxonomy of problems in optimization.

## 1. Basic definitions

### 1.1. Minimizers

- $x^{text{*}} \in \mathcal{D}$ is a global minimizer of $f$ over $\mathcal{D}$ if $\forall x \in \mathcal{D}, f(x)\geq f(x^{text{*}})$
- $x \in \mathcal{D}$ is a local minimizer of $f$ over $\mathcal{D}$ if  there exists a Neighborhood $\mathcal{N}(x)$ of $x$ such that
$$\forall y \in \mathcal{N}(x) \cap \mathcal{D}, f(y) \geq f(x)$$
- The minimum of $f$ over $\mathcal{D}$ is the value $min_{x\in \mathcal{D}} f(x)$

### 1.2. Unimodality / multimodality

<b>Definitions:</b> $f$ is unimodal if $f$ possesses a unique local minimizer ($f$ is multimodal otherwise).

<b>Definition:</b> f is convex if $\forall x, y \in D$ and any $\lambda \in [0, 1]$:

$$ f(\lambda \cdot x + (1- \lambda) \cdot y) \leq \lambda \cdot f(x) + (1-\lambda)\cdot f(y) $$

<b>Definition:</b> $f$ is strictly convex if $\forall x, y \in D$ and any $\lambda \in [0, 1]$
$$
f(\lambda \cdot x + (1- \lambda) \cdot y) < \lambda \cdot f(x) + (1-\lambda)\cdot f(y)
$$

<b>Properties:</b>
- Strict convexity => Unimodality
- Convexity => All local minimizers are global minimizers

### 1.3. Convexity: specific spaces

<b>Linear programming:</b> $f(x) = c^{T}x$ is convex

<b>Quadratic programming:</b>
- $f(x) = \mid\mid y-Ax \mid\mid_{2}^{2}$ is convex
- $f(x) = \frac{1}{2}x^{T}Hx-b^{T}x$ is convex with H symmetric positive definite

To do this, the diagonal of H is the $x_{i}^{2}$ and the other are $1/2$ the interaction terms.

## 2. Gradient and Hessian matrix

### 2.1. Gradient

<b>Definition: (Gradient)</b> The gradient of our objective function is:

$$
\nabla f(x) = \begin{pmatrix}
\frac{\delta f}{\delta x_{1}}\\
\vdots \\
\frac{\delta f}{\delta x_{n}}
\end{pmatrix} \in \mathbb{R}
$$

<i>Note:</i> Intuitively, it is the direction in which the function increases.

### 2.2. Hessian matrix

The Hessian is one of the most useful tools for analyzing and understanding the optimization of neural networks, and there is a huge body of literature that uses it to derive many impressive results (including the effects of momentum and normalization).

Before going into the Hessian, we need to have a clear picture of what a gradient is. Here’s the formal definition: the gradient is the rate of change of some function (in deep learning, this is generally the loss function) in various directions.

<b>Definition: (Hessian)</b> The Hessian is defined by:

$$H = \begin{pmatrix}
  \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1\,\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1\,\partial x_n} \\[
  \dfrac{\partial^2 f}{\partial x_2\,\partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2\,\partial x_n} \\
  \vdots & \vdots & \ddots & \vdots \\
  \dfrac{\partial^2 f}{\partial x_n\,\partial x_1} & \dfrac{\partial^2 f}{\partial x_n\,\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}.$$

> <b>Geometric intuition of the hessian</b>
> The <u>eigenvectors</u> of M are vectors that do not change direction when multiplied with $M$
> The <u>eigenvalues</u> represent the change in length of the eigenvector when multiplied with $M$. In other words:
> $$M \cdot v_{i} = \lambda_{i} v_{i}$$
> where $v_{i}$  is an eigenvector and $\lambda_{i}$  is an eigenvalue. Each eigenvector has a single eigenvalue as a pair.
>
> In the case of the Hessian, the eigenvectors and eigenvalues have the following important properties:
> - Each eigenvector represents a direction where the curvature is independent of the other directions.
> - The curvature in the direction of the eigenvector is determined by the eigenvalue.
> - If the eigenvalue is larger, there is a larger curvature, and if it positive, the curvature will be positive, and vice-versa.
>
> <b>Hessian and conditioning</b>
> The speed of convergence of most optimization depend on the conditioning of our problem. A well conditioned problem is one in which the curvature is similar among any direction.

## 3. Linear and Quadratic programming

### 3.1. Theory

Canonical form:

$$
min_{c \in \mathbb{R}^{n}} c^{T}x \text{  s.t.  }
\begin{cases}
Ax=b \\
x \geq 0
\end{cases}
$$

Standard form:

$$
min_{c \in \mathbb{R}^{n}} c^{T}x \text{  s.t.  }  Ax \leq b
$$

<b>Remarks:</b>
- Standard form $x$ => Canonical form $z = b - Ax \geq 0$
- No closed form solutions

<b>Resolution:</b>
- The simplex algorithm
- Integer Linear Programming (discrete case)

### 3.2. Knapsack problem

<b>Problem:</b> We have N items with known usefullness $u_{i}$ and weights $w_{i}$. We want to maximize the usefullness of the bag with respect to its maximum capacity W.

$$
\begin{align}
\text{Min} - &\sum_{i=1}^{N} u_{i} \cdot x_{i}\\
\text{s.t.} &\sum_{i=1}^{N} w_{i} \cdot x_{i} \leq W\\
\end{align}
$$

### 3.3. Linear Least Squares

Given $y \in \mathbb{R}^{m}$ and $A \in \mathbb{R}$ find:

$$
x^{text{*}} \in argmin_{x} \mid\mid y-Ax \mid\mid_{2}^{2}
$$

Solution, is $m \geq n$ and $A$ is full column rank, then A is the full column rank:

$$
x^{text{*}} = (A^{T}A)^{-1}A^{T}y
$$

Otherwise:
- Infinity of solutions
- Generalized inverse: solution having the minimum l-2 norm (?)

### 3.4. Quadratic programming

Given $c \in \mathbb{R}^{n}$ , $H \in \mathbb{R}^{n\times n}, a \in \mathbb{R}^{p\times n}$:

$$
min_{c \in \mathbb{R}^{n}}\frac{1}{2}x^{T} H x +   c^{T}x \text{  s.t.  }  Ax \leq b
$$

where p is the number of constraints.

Depending on the struucture of the matrix, we have the following results:
- H is positive semi-definite $\Rightarrow$ strict convex problem
- H is positive definite $\Rightarrow$ convex problem

### 3.5. Iterative algorithms

<b>Definition:</b> Solve the minimization with an iterative algorithm which generates a sequence of iterates $x_{0}, x_{1}, ..., x_{n}$, which satisfy:

$$f(x^{k})<f(x^{k-1})<...<f(x^{0})$$

### 3.6. Convergence

The sequence of iterates $x_{n}$ converges to the solution $x^{text{*}}$ of the
minimization problem.
- Global convergence: valid for all $x_{0} ∈ \mathcal{D}$.
- Local convergence: valid for $x_{0}$ in a neighborhood of $x^{text{*}}$
- Rates of convergence


------
