---
title: 'Constrained optimization'
date: 2018-10-01
permalink: /posts/2018/11/optimization-constrained/
tags:
  - Optimization
---
<b>Goal:</b> Make use of the Lagrangian and other methods to accomodate constraints.

# Formalism


$$
min_{c \in \mathbb{R}^{n}} f(x) \text{  s.t.  }
\begin{cases}
g_{i}(x) \leq 0, i= 1, ..., p \\
h_{j}(x) = 0, j= 1, ..., q \\
\end{cases}
$$

In matrix form, this translates to:

$$
min_{c \in \mathbb{R}^{n}} f(x) \text{  s.t.  }
\begin{cases}
Ax-b \leq 0_{p} \\
Cx-d = 0_{q}\\
\end{cases}
$$

<i>Notes:</i>
- $A, b, C, d$ are provided as inputs of `fmincon` and include the lower/upper bounds.
- Non-linear constraints need a special Matlab function returning $g$ and $h$.

<b>Existence of a minimizer:</b> Feasible set $\mathcal{D}$ is non-empty and bounded and $f, g_{i}, h_{i}$ differentiable $\Rightarrow \exists$ a minimizer

# Lagrangian

## Equality constraints: existence and optimality

<b>Definition (Lagrangian function):</b>
$$ \mathcal{L}(x, \lambda) = f(x) - \sum_{j=1}^{q} \lambda_{j}h_{j} $$

where $\lambda$ are the Lagrange multipliers

<b>First order optimality conditions:</b> $x_{⋆}$ is a local minimizer of $f \Rightarrow \exists \lambda_{⋆}$ such that:
$$ \begin{cases}
\nabla_{x} \mathcal{L}(x^{*}, \lambda^{*}) = 0_{n} \\
\nabla_{\lambda} \mathcal{L}(x^{*}, \lambda^{*}) = 0_{q}\\
\end{cases} $$

## Inequality constraints

<b>Definition (active / inactive):</b>
- The $i$-th constraint is active at $x$ if
- The $i$-th constraint is inactive at $x$ if $g_{i}(x) < 0$.

<i>Lagrange multipliers constraints:</i>
- $g(x) \leq 0 \Rightarrow \lambda \in \mathbb{R}_{-}^{p}$
- $g(x) \geq 0 \Rightarrow \lambda \in \mathbb{R}_{+}^{p}$

<b>Karush-Kuhn-Tucker (KKT) conditions:</b>

If $x^{⋆}$ is a local solution of $min_{x} f(x)$ s.t. $g(x)\geq 0_{p}$ then there exists $\lambda^{*}$ s.t.

$$ \begin{cases}
\nabla_{x} \mathcal{L}(x^{*}, \lambda^{*}) = 0_{n} \\
g_{i}(x^{*}) \geq 0\\
\lambda_{i} \leq 0\\
\lambda_{i}g_{i}(x^{*}) = 0
\end{cases} $$

<b>Inequality constraints:</b>

|                      | Inactive          | Weakly active     | Active            |
|----------------------|-------------------|-------------------|-------------------|
| Lagrange multipliers | $\lambda^{*} = 0$ | $\lambda^{*} = 0$ | $\lambda^{*} > 0$ |
| Contraint            | $g(x^{*}) > 0$    | $g(x^{*}) = 0$    | $g(x^{*}) = 0$    |

## Necessary condition for a local minimizer

<b>First order optimality condition:</b> $x^{*}$ is local minimizer $\Rightarrow x^{*}$ satisfies the KKT conditions.

<b>Second order optimality condition.</b>
- Let $A(x)$ denote the set of active constraints at $x$
- Let $F(x)$ denote the set of feasible directions at $x$.
- Let $C(x,\lambda)={w\in F(x)|[\nabla g_{i}(x)]^{T}w=0 \forall i\in A(x) \text{ with } \lambda_{i} >0.}$

If $x^{*}$ satisfies the KKT conditions and

$$\forall w \in  C(x^{*}, \lambda^{*})/\ \{0\}, w^{T}\cdot  \nabla_{xx}L(x^{*}, \mid \lambda^{*})\cdot w > 0$$

then $x^{*}$ is a strict local minimizer of the inequality constrained problem.

## General case: inequality and equality constraints

<b>Definition (Lagrangian function):</b>

$$\mathcal{L}(x, \lambda, \mu) = f(x) - \sum_{i=1}^{p}\lambda_{i}\nabla_{i} g_{i}(x) - \sum_{j=1}^{p}\mu_{j} h_{j}(x) $$

with $\lambda \leq 0_{p}$.

<b>KKT conditions:</b> If $x^{⋆}$ is a local minimizer, then there exists $λ^{⋆}$ and $μ^{⋆}$ such that:

$$ \begin{cases}
\nabla_{x} \mathcal{L}(x^{*}, \lambda^{*}, \mu^{*}) = 0_{n} \\
\forall i g_{i}(x^{*}) \geq 0\\
\forall j h_{j}(x^{*}) = 0\\
\lambda_{i} \geq 0\\
\lambda_{i}g_{i}(x^{*}) = 0
\end{cases} $$

# Other approaches

## Gradient projection algorithm

<b>Principle: </b>
1. Line minimization: $x_{k+1} =x_{k} +\alpha_{k}d_{k}$
2. Projection onto convex set: $x_{k+1} = proj(x_{k+1}, \mathcal{D})$

## Interior and exterior point approaches

<b>Method (Interior point approaches):</b> Constrained minimization is replaced by the unconstrainted
minimization of the augmented criterion.

<i>Examples:</i> Ridge regression and LASSO are both expressible under this form.
$$Replace min_{x\geq 0}f(x) by min_{x\geq 0}(f(x-\zeta)\sum_{i=1}^{n}log(x_{i}))$$

<b>Method (“Exterior” approaches):</b>
<i>Repeat:</i>
- Minimize $K$ with respect to $x$ (unconstrained).
- Minimize $K$ with respect to $p$ (easy): $pi = max(x_{i} , 0)$.

<i>Examples:</i> Quadratic penalty and ADMM:
$$Replace min_{x\geq 0}f(x) by min_{x, p\geq 0} (\mathcal{K}(x,p;\zeta ) = f(x) +\zeta\mid\mid x-p \mid\mid^{2})\text{ with }\zeta \rightarrow \infty $$

# Special case: linear programming

$$
min_{x \in \mathbb{R}^{n}} c^{T}x \text{  s.t.  }
\begin{cases}
Ax=b\\
x \geq 0\\
c \geq 0 \\
A\in \mathbb{R}^{m\times n} \text{ with } m\leq n
\end{cases}
$$

<b>Property (Orthogonal projection):</b> The solution $x^{⋆}$ has at least $(n − m)$ zero coordinates.

# Principle of the simplex algorithm

1. Decompose $A=[A_{B},A_{N}]$ with $A_{B}$ of size $m\times m$, and $A_{N}$ of size $m × (n − m) $.
2. Set $x^{B} = \begin{pmatrix} x_{B} \\ 0_{n-m} \end{pmatrix} \text{ with } x_{B} = A_{B}^{-1}b$
3. $x_{B}$ is a feasible point if $x_{B} ≥ 0_{m}$. The objective function is equal to $f(x_{B}) = c_{B}^{T} A_{B}^{−1}b$
4. The simplex algorithm searches for the best decomposition $A = [A_{B}, A_{N}]$. The subset $B$ is updated at each iteration in such a way that $f(x_{B})$ is decreasing.

# Special case: quadratic programming (QP)

$$
min_{x \in \mathbb{R}^{n}} \mathcal{Q}(x) = \frac{1}{2}x^{T}Hx + g^{T}(x) \text{  s.t.  }
\begin{cases}
a_{i}^{T}x = b_{i}, i \in \mathcal{E}\\
a_{i}^{T}x \geq b_{i}, i \in \mathcal{I}
\end{cases}
$$

|                        | Inactive | Weakly active | Active      |
|------------------------|----------|---------------|-------------|
| Symmetric              | Yes      | Yes           | Yes         |
| Positive               | No       | Yes           | Yes         |
| Positive semi-definite | No       | No            | Yes         |
| Minimizer              | No       | $\exists$     | $\exists !$ |

## QP with equality constraints

$$
min_{x \in \mathbb{R}^{n}} \mathcal{Q}(x) = \frac{1}{2}x^{T}Hx + g^{T}(x) \text{  s.t.  } Ax = b
$$

<b>Interior point approach:</b>
1. Assumption: $rank(A) = m$. Let $A = [A_{1}, A_{2}] \in \mathbb{R}^{m\times m}$ invertible and let $x = [x_{1}, x_{2}]$.
2. Incorporate the constraint: $x_{1} = A_{1}^{-1}(b-A_{2}x_{2})$
3. Solve the unconstrained problem $min_{x_{2}}\mathcal{Q}(A^{-1}(b-A_{2}x_{2}), x_{2})$

<b>KKT conditions:</b>

The Lagrangian function is:

$$
\mathcal{L}(x, \lambda) = \frac{1}{2}x^{T}Hx + l^{T}x
-\lambda^{T}(Ax-b)$$

Solve the system:

$$
\begin{cases}
Hx + l -A^{T}\lambda = 0\\
Ax = b
\end{cases}
\Leftrightarrow
\begin{pmatrix}
H & -A^{T}\\
A & 0\\
\end{pmatrix}
\begin{pmatrix}
x\\
\lambda\\
\end{pmatrix}=
\begin{pmatrix}
-l\\
b\\
\end{pmatrix}
$$

## QP with inequality constraints

$$
min_{x \in \mathbb{R}^{n}} \mathcal{Q}(x) = \frac{1}{2}x^{T}Hx + g^{T}(x) \text{  s.t.  } Ax \geq b
$$

<b>Principle of the active-set algorithm</b>
1. Solve a sequence of QP problems with equality constraints.
2. Use a mechanism to add or remove active constraints.

<b>Definition (Active set):</b> $A(x) = \{i : a_{i}^{T} x = b_{i\}$ is defined as the set of active constraints at x.

<b>Method:</b>
From a feasible point x_{k}:
1. Solve QP with equality constraints on $\mathcal{A}(x_{k})$ only. It yields $\tilde{x}_{k+1}$
2. If $\tilde{x}_{k+1}$ feasible:
    1. $x_{k+1} = \tilde{x}_{k+1}$
    2. Compute the Lagrange multipliers

# Sequential Quadratic Programming (SQP)

------
