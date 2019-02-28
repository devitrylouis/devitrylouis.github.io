---
title: 'Unconstrained optimization'
date: 2018-10-01
permalink: /posts/2018/11/optimization-unconstrained/
tags:
  - Optimization
---

<b>Main assumption:</b> $f: \mathbb{R}^{n} \rightarrow \mathbb{R}$  is $\mathcal{C}^{1}$ or $\mathcal{C}^{2}$.

<b>Theorem (Existence of a local minimizer):</b> Given $\mathcal{U}$ a closed subset of $\mathbb{R}^{n}$ and a continuous function $f: \mathcal{U} \subset \mathbb{R}^{n} \rightarrow \mathbb{R}$
- If $\mathcal{U}$ is bounded
- Or if $lim_{\mid\mid x \mid\mid \rightarrow \infty \text{ and }x \in \mathcal{U}} f(x) = + \infty$

then $f$ admits a local minimum on $\mathcal{U}$.

# Searching minimum

## Line search strategy

To update an iterative algorithm and move from $x_{k}$ to $x_{k+1}$, we use available informations and:
1. Choose a direction $d_{k}$ .
2. Solve (approximately) the 1D minimization problem:
$$
min_{t>0} f(x_{k} + td_{k})
$$
3. Set $x_{k+1} = x_{k}+ td_{k}$

## Feasible direction

$d$ is a feasible direction at $x \in \mathcal{D}$ if:

$$
\exists A > 0, \forall t \in [0, A], x + td \in \mathcal{D}
$$

## Descent direction

- $d$ is a descent direction of $f$ at $x \in \mathcal{D}$ if

$$
\exists A > 0, \forall t \in [0, A], x + td \in \mathcal{D}
$$

- First order Taylor expansion:

$$
f(x + td) = f(x) + td^{T}\nabla  f(x) + o(t)
$$

- $d$ is a descent direction  $\Leftrightarrow d^{T}\nabla  f(x) < 0$ (half space of descent directions)

<b>Level sets:</b> $\mathcal{L}_{z} = \{ x \in \mathbb{R}^{n}: f(x) = z \}$

## Derivatives

First order Taylor expansion:

$$f(x + td) = f(x) + td^{T} \nabla f(x) + o(t)$$

Second order Taylor expansion:

$$
\begin{align}
f(x + h) &= f(x) + h^{T} \nabla f(x) + \frac{1}{2}h^{T}H(x)h + o(\mid\mid h \mid\mid_{2}^{2})\\
f(x + td) &= f(x) + td^{T} \nabla f(x) + \frac{t^{2}}{2}d^{T}H(x)d + o(t^{2})
\end{align}
$$

Directional derivative in the direction d:

$$
\begin{align}
f'(x;d) &= lim_{t \rightarrow 0} \frac{f(x+td) - f(x)}{t}\\
&=d^{T}\nabla f(x)
\end{align}
$$

If $d$ is tangent to the level set, then $f'(x; d) = d^{T} \nabla f(x) = 0$. (WHY?)

## Necessary condition for a local minimizer

<b>Problem:</b> Find $x^{*} \in \text{arg min}_{x \in \mathbb{R}^{n}} f(x)$

<b>Theorem:</b> If f admits a local minimum at $x^{*}$, then $\nabla f(x^{*}) = 0.$

<i>Remark.</i> The condition is necessary but not sufficient.

## Sufficient condition for a local minimizer

<b>Definition (Positive definiteness)</b> $H(x^{*}) > 0 \Leftrightarrow \forall d \neq 0, d^{T}H(x^{*})d > 0$

<b>Theorem:</b> If $\nabla f(x^{*}) = 0$ and $H(x^{*}) > 0$, then $f$ admits a local minimum at $x^{*}$.

# Descent algorithms

## Blueprint

The basic idea is to:
1. Choose $x_{0}$, and then for $k \geq 0$,
    * <b>Unimodal criterion:</b> any value of $x_{0}$ should work (theoretically...)
2. Find a <b>descent direction</b> $d_{k}$
    * <b>Constant step:</b> $t_{k} = t, ∀k$.
    * <b>1D minimisation:</b> $t_{k} =argmin_{t>0} f(x_{k} + td_{k})$.
3. Find a <b>step</b> $t_{k} >0$.
4. Compute $x_{k+1} = x_{k} +t_{k}d_{k}$.

As for the descent, we require: $\forall k \text{ } f(x_{k+1}) < f(x_{k})$

Furhermore, we impose stopping conditions to avoid "getting stuck":
- $f(x_{k}) - f(x_{k+1}) < \epsilon_{1}$
- $\mid\mid x_{k} - x_{k+1}\mid\mid < \epsilon_{2}$
- $\mid\mid \nabla f(x_{k})\mid\mid < \epsilon_{3}$
- $k = K_{max}$

## Gradient based algorithms

Simply choose $d_{k} := \nabla f(x_{k})$

If the step is chosen as

$$
t_{k} = \text{arg min}_{t>0} f(x_{k}-t\nabla f(x_{k}))
$$

then $\nabla f(x_{k})$ and $\nabla f(x_{k+1})$ are orthogonal, which implies slow (linear) convergence.

Typically, for the choice of descent direction we impose that:

$$
\mid Angle(d_{k}, \nabla f(x_{k})) \mid \frac{\pi}{2} - \mu
$$

## Line minimization

How to compute:
$$
t_{k} = \text{arg min}_{t>0} f(x_{k}-t\nabla f(x_{k}))
$$

- Steepest descent: exact minimization.
- Constant step $t_{k} = t$.
    * Risk of small steps.
    * Does not guarantee that $f(x_{k} + td_{k})<f(x_{k}) \forall k$.
    * Reajust $t = t/2$.
- Dichotomy, golden section.
- Quadratic approximation of $\phi:t→f(x_{k} +td_{k})$.
- Quadratic or cubic approximation of $\phi$ from the knowledge of $\phi'(0)$.
- Armijo and Wolfe’s rules: ensure that $t$ is “acceptable” (sufficient decrease of $f$, sufficiently large step $t$).

## Step selection: Armijo’s rule

Choose $t$ such that $f(x_{k} +td_{k}) \leq f(x_{k})+ c_{1} t f′(x_{k};d_{k})\text{ with }0< c_{1} <1$.

Let $\phi(t) := f(x_{k}+t d_{k})$ then the rule rewrites as:

$$
\phi(t) = \phi(0) + c_{1}t\phi'(0)
$$

with $\phi'(0) = \nabla f(x_{k})^{T} d_{k}$

## Step selection: Wolfe’s rule

Choose t such that:

$$
\begin{cases}
\phi(t) \leq \phi(0) + c_{1}t\phi'(0) \\
\phi'(t) \geq c_{2} \phi'(0) \text{ with } 0 < c_{2} < c_{1} < 1
\end{cases}
$$

## Convergence of Gradient Descent

Gradient descent converges under very mild assumptions. For example, it is possible to prove a convergence rate with the only a smoothness assumption (not even convexity). We will assume $f$ is differentiable and its gradient is $L$-Lipschitz.

Then
$$
min_{0\leq t \leq T} \mid\mid \nabla f(x_{t}) \mid\mid \leq \frac{L(f(x_{0}) - f(x^{*})}{\sqrt{T+1}}
$$

## Conjugate gradient algorithm

The conjugate Gradient algorithm:
- Choose $x_{0}$
- For $k \geq 0$, do $x_{k+1} \leftarrow x_{k} - t_{k} \nabla f(x_{k}) + beta_{k}(x_{k}-x_{k-1})$
- The convergence rate is much faster

For $k \geq 0$,

$$
x_{k+1} \leftarrow x_{k} + \beta_{k} d_{k}\text{ with }d_{k} = - \nabla f(x_{k}) + \beta_{k}d_{k-1}
$$

- <b>Fletcher-Reeves:</b> $\beta_{k}^{FR} = \frac{\mid\mid \nabla f(x_{k}) \mid\mid^{2}}{\mid\mid \nabla f(x_{k-1}) \mid\mid^{2}}$

- <b>Polak-Ribière:</b> $\beta_{k}^{PR} = \frac{[\nabla f(x_{k})]^{T}(\nabla f(x_{k}) - \nabla f(x_{k-1}))}{\mid\mid \nabla f(x_{k-1}) \mid\mid^{2}}$

Subspace optimization (memory gradient).

$$d_{k} = - \nabla f(x_{k}) + \sum_{l = 1}^{m}\omega_{k}d_{k-l}$$

------
