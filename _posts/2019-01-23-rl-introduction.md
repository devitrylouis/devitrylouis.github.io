---
title: 'Introduction to reinfocement learning'
date: 2018-12-01
permalink: /posts/2019/01/rl-introduction/
tags:
  - Reinforcement learning
---

Reinforcement learning find its roots in several scientific fields, such as Deep learning, Psychology, Control, Statistics (but not limited to!). It typically consists of taking suitable action to maximize reward in a particular situation. Below is a common illustration of its core idea:

![Rat experiment](https://www.verywellmind.com/thmb/_T61URUMhbbasb7_nbKa-WknH4o=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/2794863-operant-conditioning-a21-5b242abe8e1b6e0036fafff6.png)

## Supervised vs Evaluative Learning

Supervised learning paradigm reach its limit when it comes to improve upon the performance of the traning data (a supervised learning task trained with the best chess player will not be better at chess than the best player).

The main difference between supervised learning and reinforcement learning is whether the <u>feedback</u> received is <u>evaluative</u> or <u>instructive</u>.

<u>Instructive feedback</u> tells you how to achieve your goal, while <u>evaluative feedback</u> tells you how well you achieved your goal.

Supervised learning solves problems based on instructive feedback, and reinforcement learning solves them based on evaluative feedback.

ADD TABLE

### Framework

The typical formalization of reinforcement learning problems is based on the concepts of <u>agent</u> evolving in an <u>environment</u>, as described in the following diagram:

![diagram_framework](http://www.incompleteideas.net/book/ebook/figtmp7.png)

where an agent acts via a <u>policy</u> $\pi(s, a)$ on an <u>environment</u>, which in turn emits bach a <u>reward</u> $r(s, a)$ and a <u>new state</u> $s'$ (or an observation) to the agent. It should be noted that the behavior of both the environment and the agent is usually Markovian (details below).

<b>Notes:</b>
- Partial observation of the environment leads to partially observable Markov Devision Processes
- The interaction with the environment are usually divided into discrete episodes
- The environment can depend on a history of previous states

### Reward hypthesis

Each action $a$ allows to potentially obtain a reward so we are fundamentally interested to $r(s, a)$ for a given state $s$.

<b>Assumption:</b> All goals can be described by the maximisation of the expected cumulative reward.

Ex.: Score in a game.
Ex. 2: Typical image classification is not a RL task
EXAMPLE

### Taxonomy of Reinforcement Learning

Altough the previously discussed framework remains relatively unchanged accross RL problems, the goals and settings of the problems differ.

<b>What is the goal?</b>
- <u>Control:</u> Determining an optimal policy
- <u>Evaluation:</u> Evaluating a policy

<b>Is a model supporting the problem?</b>
- <u>Model free:</u> No model of the environment is learned / used and is instead planned directly from experience. (-> No speficic assumpion)
- <u>Model based:</u> Attempt to learn / exploit a model of the environment with the goal of using the model (models can vary in terms of efficience in design and speed)

<b>Should we encourage discovery of the problem or reward optimization?</b>
- <u>Exploration:</u> The agent discover new states, eventually making mistakes.
- <u>Exploitation:</u> The agent optimises its cumulated reward with the knowledge of prior discovery.
- <b>Fundamental trade-off:</b> Similarly to the bias-variance tradeoff in conventional Machine Learning, the agent needs to balance both exploration and exploitation phases to produce meaningful policies and avoid suboptimal results.

## Mathematical formalization

### States / Actions

<b>States:</b> We refer to a state $s$ as an element from $\mathcal{S}$ a countable set:
$$
\mathcal{S} = \{ s_{1}, ..., s_{n}, ... \}
$$

<i>Examples:</i>
1. Successive rounds of Tic Tac Toe.
2. Successive chess plays

<b>Actions:</b> We refer to an action a as an element from $\mathcal{A}$ a countable set.
$$
\mathcal{A} = \{ a_{1}, ..., a_{n}, ... \}
$$

<i>Examples:</i>
1. Nought or cross
2. Legal chess moves

### State-action transitions

To understand in-depth the incoming Mathematical concepts, the reader should be familiar with [Markov Random Processes](https://en.wikipedia.org/wiki/Markov_decision_process).

![markovian_rl](/images/markovian_rl.png)

In a nutshell, a Markov Decision Process (MDP) is a 4-plet $(\mathcal{S}, \mathcal{A}, p, \gamma)$ where:
- $\mathcal{S}$ is a discrete set of states
- $\mathcal{A}$ is a discrete set of actions
- $p$ is a discrete probability transition kernel
$$p: (\mathcal{P}(\mathcal{S}) \times \mathcal{B}(\mathbb{R})) \times (\mathcal{S} \times \mathcal{A}) \mapsto \mathbb{R}_{+}
$$
- $\gamma$ is a discount factor that  (similar to money value in finance)

The transition kernel models the probability to fo from a state $s \in \mathcal{S}$ with action $a \in \mathcal{A}$ to the state $\{s'\}\in \mathcal{P}(\mathcal{S})$ and reward $\{r\}\in \mathcal{P}(\mathcal{A})$. In terms of notation, the evaluation of this function will be denoted:

$$
p(\{s'\} \times \{r\} \mid (s, a))
$$

Two important results can be derived from the above defined kernel, namely:
1. <u>Probability measure:</u> $p(. \mid (s, a)) \text{, } \forall (s, a) \in (\mathcal{S} \times \mathcal{A})$
2. <u>Next state probability: </u> The expression below qualifies the probability of $s'$ realization under the policy $(s, a)$, noted as $s\mapsto^{a} s'$:

$$p(s', a, s) := p(\{s'\} \times \mathbb{R} , (s, a))$$

### Reward function

Let $(S, A)$ a state-action pair. Then, the next state $S’$ as well as the corresponding reward $R$ are given by:

$$
(S', R) \sim p(.\mid (S, A)) \Leftrightarrow \mathbb{P}((S', R) \in \mathcal{U}) = p(\mathcal{U}\mid (S, A))
$$

where $\mathcal{U}$ is the [borel set](https://en.wikipedia.org/wiki/Borel_set). Now that these probabilities are properly defined, we can naturally express the reward function as:

$$
r(s, a) = \mathbb{E}(R \mid S = s, A = a)
$$

<b>Cumulative reward:</b> For a given $\gamma \in ]0, 1]$ and a sequence of rewards $R_{1}, ..., R_{n}$ we define the return (cumulative reward) as:

$$
\sum_{n \geq 0}\gamma^{n}R_{n}
$$

which will prove useful in discounting intermediate rewards later on.

### Policy

We are interested in designing a policy which dictates to an agent what action to take given a particular state. It should be noted that the definition of the policies vary with the context (see tables below)

|  | Deterministic | Stochastic |
|:--------------:|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------:|
| <b>Stationary</b> | $\pi = (\pi_{1}, \pi_{1}, ...)$, with $\pi_{i}:\mathcal{S}\mapsto \mathcal{A}$ | $\pi = (\pi_{1}, \pi_{1}, ...)$, with $\pi_{i}:\mathcal{S} \times \mathcal{A} \mapsto \mathbb{R}_{+}$ |
| <b>Non-stationary</b> | $\pi = (\pi_{1}, \pi_{2}, ...)$, with $\pi_{i}:\mathcal{S}\mapsto \mathcal{A}$ | $\pi = (\pi_{1}, \pi_{2}, ...)$, with $\pi_{i}:\mathcal{S} \times \mathcal{A} \mapsto \mathbb{R}_{+}$ |

<i>Note:</i> The stochastic case $\pi_{i}:\mathcal{S} \times \mathcal{A} \mapsto \mathbb{R}_{+}$ verifies $\sum_{a} \pi(a\mid s) = 1$

<b>Interaction of the agent given a policy:</b> Given a policy, one can define a Markov chain via:

$$p(s' \mid s) = \sum_{a}p(s', a, s)\pi(a\mid s)$$

At each step $n$, the agent is at the state $S_{n}$ and following its policy $\pi$, performs the action $A_{n} = \pi(S_{n})$ reaches:

$$
S_{n+1}, R_{n+1} \sim p(., . \mid S_{n}, A_{n})
$$

Then, an episode is a sequence $S_{0}, A_{0}, R_{1}, S_{1}, A_{1}, R_{2}, S_{2}, A_{2}$


### State value function

In a stationary setting, the value function $v^{\pi}:\mathcal{S}\mapsto \mathbb{R}$ (of a state $s$) is the expected reward if you start at that state and continue to follow the policy $\pi$.

$$
v^{\pi}(s) = \mathbb{E}_{\pi}\Big( \sum_{n=0}^{\infty}\gamma^{n}R_{n}\mid S_{0} = S \Big)\text{, } \forall s \in S
$$

As for the meaning of the expectation $E_{\pi}$ under a policy $\pi$ and an initial distribution $\mu$ on the state, we write:

$$
\mathbb{E}_{\pi} [f(S_{0}, ..., S_{n})] = \sum_{(s_{0}, ..., s_{n})} \mu(s_{0})p(s_{0}\mid s_{1})...p(s_{n-1}\mid s_{n})f(s_{0}, ..., s_{n})
$$

where $p(s'\mid s) = \sum_{a}p(s', a, s)\pi(a\mid s)$.

<b>Key idea:</b> The expectation in that formula is over all the possible routes starting from state $s$. Usually, the routes or paths are decomposed into multiple steps, which are used to train value estimators. These steps can be represented by the tuple $(s,a,r,s′)$ (state, action, reward, next state)

<i>Note:</i> Even if the policy is deterministic, the reward function and the environment might not be. Nor the value function is not deterministic.

<b>Optimal value function:</b> A policy $\pi^{*}$ is called optimal if:

$$v^{\pi^{*}}(s) = \text{max}_{\pi}v^{\pi}(s) \text{, } \forall s \in \mathcal{S}$$

### Bellman equation

The Bellman equation is a necessary condition for the optimality associated with dynamic programming. It writes the value of a decision problem at a certain point in time in terms of the payoff from some initial choices and the value of the remaining decision problem that results from those initial choices. This breaks a dynamic optimization problem into a sequence of simpler subproblems, as Bellman's “principle of optimality” prescribes.[2]

It means Q-value(state) = reward + the discounted Q-value(state) easily reachable from state.

$$
\begin{align}
\mathcal{P}_{s', s}^{\pi} &= \sum_{a}\pi(a \mid s)\cdot p(s' \mid s, a)\\
r^{\pi}(s) &= \sum_{a}\pi(a \mid s)\cdot r(s, a)
\end{align}
$$

we can transform the value function into:

$$
v^{\pi} = r^{\pi} + \gamma \mathcal{P}^{\pi} v^{\pi} \Leftrightarrow (I-\gamma \mathcal{P}^{\pi})v^{\pi} = r^{\pi}
$$

Under the assumpion that $\gamma < 1$ and $\mid\mid\mathcal{P}^{\pi}\mid\mid\leq 1$ we obtain:

$$
v^{\pi} = (I-\gamma \mathcal{P}^{\pi})^{-1}r^{\pi}
$$

<b>Implementation notes:</b>
- The formula $(I-A)^{-1} = \sum_{k\geq 0} A^{k}$ is useful for inverse approximations.

## Sources:
https://stats.stackexc
https://joshgreaves.com/reinforcement-learning/introduction-to-reinforcement-learning/
------
