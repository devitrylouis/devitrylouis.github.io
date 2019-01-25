---
title: 'Introduction to dynamic programming'
date: 2018-12-01
permalink: /posts/2019/01/rl-dynamic-programming/
tags:
  - Reinforcement learning
---

<u>Dynamic Programming</u> is a method for solving a complex problem by <b>breaking it down into a collection of simpler subproblems</b>, solving (often recursively) each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).

![xkcd joke](/images/xkcd_functional.png)


As Jonathan Paulson puts it, Dynamic Programming is just a fancy way to say "remembering stuff to save time later".

Applied to Reinforcement Learning, Dynamic Programming provide a theoretically powerful model framework for:

- <b>Control:</b> Finding a policy $\pi^{*}$ that maximises the cumulated reward
- <b>Prediction:</b> Finding the value of each state $v^{\pi}$

In this blogpost, we will overview the fundamental role of Dynamic Programing in Reinforcement Learning. Most notably, we will:

- Provide a proof of the <u>optimal policy theorem</u>, which states that there exists (not necessarily unique) a deterministic policy $\pi^{*}$ that satisfies $v_{\pi}(s) \leq v_{\pi^{*}}(s),\ \forall \pi\ \forall s$
- Give an algorithm that find such a solution.

## Introduction to planning

<b>TL; DR:</b> Planning with Dynamic Programming requires a <u>transition</u> $p(s'\mid a, s)$ and a <u>reward function</u> $r(s, a)$. From there, it will iteratively compute a <u>value function</u> $q^{\pi}$ (also called $Q$-value) and its <u>corresponding policy</u> $\pi$; ultimately returning an <u>"optimal" policy</u> $\pi^{*}$. Overall, it involves a decision making process, which is possibly model based $p_{\theta}(s'\mid a, s))$.

#### The need of a Markov Decision Process

Mathematically speaking, a planning task consists in estimating $\pi^{*}$ or $v^{*}$ from a Markov Decision Process $\mathcal{X}$, defined by:
$$
\mathcal{X} = (\mathcal{S},\text{ } \mathcal{A}, \text{ }p(r, s' \mid s, a), \text{ }\gamma)
$$

where $\mathcal{S}$ and $\mathcal{A}$ are the state and actions space and $\gamma$ a discount factor.

If you are unfamiliar with the mathematical framework of reinforcement learning, you can refer to [this previous blogpost](_posts/2019/01/rl-introduction/), or a [more layman suited explanation]().

#### Hardness of the task

Recalling that $\pi: \mathcal{S} \times \mathcal{A} \mapsto \mathbb{R}_{+}$, the number of deterministic policies is $\mid\mathcal{A}\mid^{\mathcal{S}}$. It therefore becomes impractical for larger state set $\mathcal{S}$.

To mitigate this issue, we typically use look-up tables, which provide an efficient storage of the state and actions space. Each of the subproblem solutions is indexed in some way, typically based on the values of its input parameters, so as to facilitate its lookup. So the next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time. This technique of storing solutions to subproblems instead of recomputing them is called memoization.

## Task

<b>Optimal Policy theorem:</b> There exists (not necessarily unique) a deterministic policy $\pi^{*}$ that satisfies $v_{\pi}(s) \leq v_{\pi^{*}}(s),\ \forall \pi\ \forall s$

whose direct consequences are:

$$
\begin{cases}
v^{*}(s) &= v^{\pi^{*}}(s)\\
q^{*}(s, a) &= q^{\pi^{*}}(s, a)
\end{cases}
$$

#### Estimating Q-value with the expectancy over a policy?

The state-value function (or Q-function) is defined as:

$$
q^{\pi} (s, a) = \mathbb{E}_{\pi}\Big( \sum_{n\geq 0} \gamma^{n}R_{n} \mid S_{0} = s, A_{0} = a \Big)
$$

The meaning of the expectancy over a policy $E_{\pi}$ is more thoroughly described in [this previous blogpost](_posts/2019/01/rl-introduction/). As for the optimal $Q$-value, it is often denoted as:

$$
q^{*}(s, a) = \text{max}_{\pi}q^{\pi}(s, a)
$$

Probability distribution being hard to estimate as the dimensions of the problem increases (i.e. curse of dimensionality), it becomes challenging to compute the expectancy as is. To solve this problem, we turn to the fixed-point theorem.

## Fixed-point optimal value function

Let's recall the <b>Bellman equation</b>:

$$
v^{\pi}(s) = \sum_{a}\pi(a\mid s)r(s, a) + \gamma \sum_{s'}\pi(a\mid s)p(s'\mid, s, a)v^{\pi}(s')
$$

which can be written in a more readable fashion:

$$
v_{\pi} = r^{\pi} + \gamma P^{\pi}v^{\pi}
$$

Given this is a linear equation, that can be thought as a fixed point. Our goal is therefore to derive an optimal policy $v^{\pi^{*}}$ using the fixed-point theorem:

<b>Fixed-point theorem:</b> Let $(E, d)$ be a complete space, and $f:E \mapsto E$ which satisfies the <u>contraction property</u>:
$$
\exists \ 0 \leq \gamma < 1: \forall x, y, \ d(f(x), f(y)) \leq \gamma\ d(x, y)
$$

then $x_{n+1} = f(x_{n})$  converges to an unique $x^{*}$ with
$$d(x_{n}, x^{*}) \leq \frac{\gamma^{n}}{1 - \gamma}d(x_{n}, x_{0})$$

#### Bellman operators

We show in this section that the <u>Bellman equation satisfies the contraction property (i.e. the assumptions of the fixed-point theorem)</u>. To this end, we will consider the problem in terms of operators; an operator being a mapping that acts on elements of a space to produce other elements of the same space. Specifically, we will consider two, dercribed below:

1. The <b>linear operator $\mathcal{T}^{\pi}$</b> takes as input a present $Q$-function $v$ and a state, and output updated the immediat reward plus the $\gamma$ discounted sum of present $Q$-values $v(s')$, weighted by their corresponding transitions probabilities $p(s'\mid s, \pi(s))$.

$$\mathcal{T}^{\pi}v(s) = r(s,\ \pi(s)) + \gamma \sum_{s'}\ p(s'\mid s, \ \pi(s))\ v(s')$$

2. The <b>non-linear operator $\mathcal{T}^{*}$</b> basically retrieves the best reachable $Q$-value from present $Q$-values and the current state $s$:

$$
\mathcal{T}^{*}v(s) = max_{a\in \mathcal{A}} \Big(r(s, a) + \gamma \sum_{s'} p(s'\mid s, a)v(s') \Big)
$$

The <b>bellman operators</b> are <u>order preserving</u>:
$$
\begin{align}
v \leq \tilde{v} \Rightarrow \mathcal{T}^{\pi}v \leq \mathcal{T}^{\pi} \tilde{v}\\
v \leq \tilde{v} \Rightarrow \mathcal{T}^{*}v \leq \mathcal{T}^{*} \tilde{v}\\
\end{align}
$$

which can be thought of as an [isometry](http://mathworld.wolfram.com/Isometry.html) (the proportions are conserved). Using this, we can derive the <b>contraction property</b> easily:

$$
\begin{align}
\mid\mathcal{T}^{\pi}v(s) - \mathcal{T}^{\pi}v'(s)\mid &= \gamma \mid \sum_{s'}\ p(s'\mid s,\ \pi(s))(v(s')-v'(s))\mid\\
&\leq\gamma \sum_{s'}\ p(s'\mid s,\ \pi(s))\ \mid v(s')-v'(s)\mid\\
&\leq\gamma \sum_{s'}\ p(s'\mid s,\ \pi(s))\ \mid\mid v-v'\mid\mid_{\infty}\\
&=\ \mid\mid v - v' \mid\mid_{\infty}
\end{align}
$$

Using the <b>fixed-point theorem</b>, we obtain <b>two major results</b>:
1. It exists a unique $v^{*}$</b> such that $\mathcal{T}^{*}v^{*} = v^{*}$: This means that there is a solution for which we cannot obtain a better $Q$-value.
2. $\mathcal{T}^{\pi}v^{\pi} = v^{\pi}$ is the unique fixed point, which means that under the policy $\pi$, remaining in the state $s$ provide the best $Q$-value. It can be thought of as an eigenvector of the operator.

<b>Careful:</b> In our setting, we consider only deterministic policies.

---



<b>Definition:</b> A policy $\pi'$ is said to <u>act greedy</u> with respect to $\pi$ if:

$$
\pi'(s) = \text{arg max}_{a\in \mathcal{A}} q_{\pi}(s, a)
$$

<b>Greedy policy lemma:</b>
1. $v_{\pi} \leq v_{\pi'}$
1. $v_{\pi'}(s) = v_{\pi'}(s) \Leftrightarrow v_{\pi}(s) = v^{*}(s)$

This is a way to design a better policy from an existing policy, which will ultimately be used in an iterative manner.

<i>Proof of the lemma:</i> Recall that
$$\pi'(s) = \text{arg max}_{a\in \mathcal{A}} q^{\pi}(s, a)$$

Then:

$$
\begin{align}
v^{\pi}(s) &= \mathcal{T}^{\pi}v^{\pi}(s)\\
& = r(s , \pi(s)) + \sum_{s'} p(s'\mid s, \pi(s))v^{\pi}(s')\\
&\leq \text{max}_{a\in \mathcal{A}}\big( r(s, a) + \sum_{s'} p(s'\mid, s, a) v^{\pi}(s') \big)\\
&= \mathcal{T}^{\pi'}v^{\pi}(s) \\
&= \mathcal{T}^{*}v^{\pi}(s)
\end{align}
$$

thus yielding

$$(\mathcal{T}^{\pi'})^{k}v^{\pi} = (\mathcal{T}^{\pi'})^{k}\mathcal{T}^{\pi}v^{\pi} \leq (\mathcal{T}^{\pi'})^{k+1}v^{\pi}$$

which in turn implies for large $k\rightarrow\infty$

$$
v^{\pi} \leq \mathcal{T}^{*}v^{\pi}\leq v^{\pi'}
$$

#### Proof

The proof consists of exhibiting a <u>candidate policy</u> using the <u>Greedy policy lemma</u>.

Let us fix a policy $\pi_{0} = \pi$. At step $n$, we consider $\pi_{n+1}$ the greedy policy with respect to $\pi_{n}$ : $\pi_{n+1}(s) = \text{arg max}_{a}q^{\pi_{n}}(s)$

Using the greedy theorem, we obtain:
$$
v^{\pi_{n}} \leq \mathcal{T}^{*}v^{\pi_{n}} \leq v^{\pi_{n+1}}
$$

As $\mathcal{T}^{*}$ is continuous, there exists $\tilde{v}$ such that:

$$
lim_{n\rightarrow\infty}v^{\pi_{n}} = \mathcal{T}^{*}\tilde{v} = \tilde{v}
$$

Finally, $\tilde{v}$ is the unique fixed point of $\mathcal{T}^{*}$ and $v^{\pi} \leq \tilde{v}$.

Reminder: non-decreasing sequences are always convergent.

Yet, the set of policy $\{\pi_{1} , ..., \pi_{n} , ...\}$ is finite thus, $\exists N, \forall n \geq N, v^{\pi_{n}} = v^{\pi_{0}}$. Consequently, there must exist a policy $\pi^{*}$ in this set such that $v^{\pi^{*}} = \tilde{v}$. As $\pi_{0}$ was arbitrarily chosen, the result hold for all $\pi$:

$$
v^{\pi^{*}} \geq v^{\pi}, \forall \pi
$$

Finally:

$$
\begin{align}
q^{\pi^{*}}(s, a) &= r(s, a) + \sum_{s'}p(s'\mid s, a)v^{\pi^{*}}(s')\\
&= sup_{\pi}\big( r(s, a) + \sum_{s'} p(s'\mid s, a)v^{\pi}(s') \big)\\
&= sum_{\pi}q^{\pi}(s, a)
\end{align}
$$

Optimal bell man equation (1)

One can verify that (q^{*}, v^{*}) are optimal if and only if:

$$
\begin{cases}
v^{*}(s) = \text{sup}_{a\in \mathcal{A}}q^{*}(s, a)\\
q^{*}(s, a) = r(s, a) + \gamma \sum_{s'} p(s'\mid s, a)v^{*}(s')
\end{cases}
$$

Also, a policy is optimal if and only if:

$$
\sum_{a}\pi(a\mid s) q^{*}(s, a) = v^{*}(s)
$$

## DP algorithms

#### Prediction

How to obtain $v^{\pi}$ or $v^{*}$? Iterate an operator until convergence:

$$
lim_{k\rightarrow \infty} (V^{\pi})^{k} = v_{0} = v^{\pi}\\
lim_{k\rightarrow \infty} (V^{*})^{k} = v_{0} = v^{*}
$$

```python
def iterative_policy_evaluation(pi, max_iter):
    """
    Evaluate the rewards
    """
    # Initialize v to some suited structure (here QValue() by lack of a better name :) )
    v = QValue()
    # Apply
    for k in range(0, max_iter):
        v = linear_bellman_operator(pi, v)
    return(v)

def value_iteration(pi, max_iter):
    """
    Gives the best reachable Q-value
    """
    # Initialize v to some suited structure (here QValue() by lack of a better name :) )
    v = QValue()
    # Apply
    for k in range(0, max_iter):
        v = nonlinear_bellman_operator(pi, v)
    return(v)
```

<b>Convergence:</b> The error is in
$$\mathcal{O}\big(\frac{\gamma^{K}}{1-\gamma}\big)$$

<b>Complexity</b> The complexisty is mostly due to matrix multiplications of MDP:
$$\mathcal{O}(\mid \mathcal{A}\mid \cdot \mid \mathcal{S} \mid^{2})$$

<b>Memory:</b> Consists of the MDP storage and the value function storage
$$\mathcal{O}(\mid \mathcal{A}\mid \cdot \mid \mathcal{S} \mid^{2}) + \mathcal{O}(\mid \mathcal{S}\mid)$$

#### Two approaches for combining policy evaluation and value iteration

Synchronous algorithms

```python
def iterative_policy_evaluation(S, T_non_linear, max_iter):
    """
    Evaluate the rewards
    """
    # Initialize v to some suited structure (here QValue() by lack of a better name :) )
    v = QValue()
    # Apply
    for k in range(0, max_iter):
        for s in S:
            v_temp(s)
            v = linear_bellman_operator(pi, v)
    return(v)

def value_iteration(pi, max_iter):
    """
    Gives the best reachable Q-value
    """
    # Initialize v to some suited structure (here QValue() by lack of a better name :) )
    v = QValue()
    # Apply
    for k in range(0, max_iter):
        v = nonlinear_bellman_operator(pi, v)
    return(v)
```

<b>Theorem:</b> The asynchronous algorithm converges to $v^{*}$ if the algorithm visits infinitely often each state of the MDP.

Control
https://cs.stanford.edu/people/karpathy/reinforcejs/gridworld_dp.html
https://medium.com/@codingfreak/top-50-dynamic-programming-practice-problems-4208fed71aa3
https://www.quora.com/How-should-I-explain-dynamic-programming-to-a-4-year-old/answer/Jonathan-Paulson
https://medium.com/@curiousily/solving-an-mdp-with-q-learning-from-scratch-deep-reinforcement-learning-for-hackers-part-1-45d1d360c120
------
