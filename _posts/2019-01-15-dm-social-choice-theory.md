---
title: 'Social choice theory'
date: 2018-12-01
permalink: /posts/2019/01/dm-social-choice-theory/
tags:
  - Decision Modeling
---

Social choice theory is an established field and a cornerstone of countless others: Economics, Political science, Computer science, Applied mathematics, Operational Research. As for AI applications, it turns out to be really useful for developing Multiple Agents systems.

In the past Decision Modeling blogposts, we've introduced and studied how should an individual model can take efficient decisions based on single and multiple criterias. However, we sometimes need to describe how a group would choose among several alternatives. This is the purpose of this blospost.

First, we will remind the basics behind the abstract theory (section 1). Then, we will review some key types of elections (section 2). Finally, we will explain important theorems...

We will use a specific vocabulary in this post, by considering the problem as:

> <b>Central problem:</b> Study of election situations in which a society is to make a decision concerning several candidates

## 1. Introductions to elections

### 1.1. Generalities

The decision definition is of course subject to the group itself (size, nature, ...) and in the context of elections, this dependence can be translated by the following political questions, who are worth the time to ponder on:
- <u>Is it a direct/indirect democracy?</u> USA is an indirect democracy.
- <u>What is the role of political parties and opinion polls?</u>
- <u>Who can vote?</u> Most countries demands an age threshold to vote.
- <u>Who can candidate?</u> There is an age limit in the USA.
- How is the election campaign organized?

While democracy elections are oftenly guided by majority, the set of candidates needs additional precisions in the context of a group.

First, beside North Korea, most countries have at least two candidates and have special rules as to how votes are processed. And these rules are subject to high variations. These rules vary a lot between countries (see section 1.1).

Furthermore, the system is overall much more complex because the choice of a candidate impact not only an individual decision model but all the society. This should definitely be accounted for.

Finally, one should keep in mind that non-trivial questions arise when there strictly more than two candidates (with possible undesirable effects).

### 1.2. General Taxonomy of elections

Election results derive from two criteria:
- <b>Types of ballot:</b> There is high diversity in the required ballot. While most countries demand an uninominal ballot (France), others require a ranking (Ireland). There are also cases like grading ().
- <b>Organisational method:</b> How the ballots are counted and how the votes occurs (are the votes private or publicly shared).

These different factors result in an abundant types of election possible. We will cover the most common ones.

## 2. One and two round votes

## 2.1. One round vote

One-round vote is the simplest case: votes are uninominal and the winning candidate is the one with most votes. While ex-aequos cases can happen, we can safely neglect them due to their unlikeliness. Nontheless, some rules designed to deal with such Black swans in practice: the Queen chooses the winner in the UK, or the younger one is chosen! Even a random draw has been chosen.

While most implementations of this system have two candidates, those with more may violate the will of a majority of voters! For instance, imagine an election with 10 candidates. If all but one have 9% of the votes, the winning one gets 18%. This can be quite quite problematic for the 82% of the society. One way to solve this issue is to introduce multiple rounds to reduce the pool of candidates (two in most cases).

## 2.2. Two-round vote

This kind of vote has the same underlying principiles: uninominal ballots and the number of votes are discriminant. The only point of the rounds is to get back to the one-round vote; the first round selects the two candidates with the most votes. However, this introduces biases and problems as the vote is easily manipulable.

> A voting system is <u>manipulable</u> is some voters do not act in their best interests.

Another improtant property of the two-round vote is its monotonicity.

> A ranked voting system is <u>monotonic</u> if it is neither possible to prevent the election of a candidate by ranking them higher on some of the ballots, nor possible to elect an otherwise unelected candidate by ranking them lower on some of the ballots (while nothing else is altered on any ballot).

<u>Participation:</u>
<u>Separability:</u>

## 3. Condorcet and variations: Schartz, Copeland and Borda

### 3.1. Condorcet

<b>Principles:</b> The candidates are compared pairwise: $a$ is “socially preferred” to b if there is (strictly) more voters preferring a to b. The unique elected candidate - called a Condorcet Winner - is the one preferred to all others.

<b>Remarks:</b>
- One-round and two-round votes violate Condorcet principle
- Single-round vote may elect a Condorcet loser
- The Condorcet principle does not solve the problem of the “dictatorship of majority”
- CW is not necessarily ranked high by voters (see range voting)

<u>Condorcet paradox:</u> For a large number of voters and of candidates, curcuits tend to for. For instance, when there are 7 cendidates, circuits occur with 40% probability.

To solve this issue, one can weaken the conditions but there is no existence and uniqueness results. Some of these variations are described in the sections below.

### 3.2. Schartz rule

The social preferences are built “`a la Condorcet”. Then compute the transitive closure and its corresponding pre-order. Finally, take the maximum elements of the resulting pre-order.

### 3.3. Copeland rule

The social preferences are built “`a la Condorcet”. We then compute the Copeland score for each pair $(a, b)$ which is the number of candidates (s)he beats minus the number of candidates which beats him/her. Formally, this translates to:

The winning candidate is the one with the larger Copeland score.

### 3.4. Borda rule

<b>Principle:</b> Voters provide an ordered list of candidates and we rank candidates according to the sum of ranks over all voters.

It is a simple, efficient, monotone, separable and encourages participation.

## 4. Arrow theorem

### 4.1. Introduction
In social choice theory, Arrow's impossibility theorem, the general possibility theorem or Arrow's paradox is an impossibility theorem stating that when voters have three or more distinct alternatives (options), no ranked voting electoral system can convert the ranked preferences of individuals into a community-wide (complete and transitive) ranking while also meeting a specified set of criteria: unrestricted domain, non-dictatorship, Pareto efficiency, and independence of irrelevant alternatives.

### 4.2. Mathematical reminder

Each agent $i$ provides a weak-order $\succeq_{i}$ on the set of candidates $A$
We denote WO(A) the set of weak-orders on $A$:

$$WO(A) = \{\succeq_{i}, \ \forall i\in A \}$$

A profile $\Pi$ is defined by the weak orders provided by each agent $\Pi = (\succeq_{1}, ..., \succeq_{n})$

An aggregation function is a mapping $\Phi$ that associates to any profile $Π$ a weak order on A representing the social preference

$$
\begin{align}
\Phi: WO(A)^{n} &\mapsto WO(A)\\
(\succeq_{1}, ..., \succeq_{n}) &\rightarrow \succeq
\end{align}
$$

### 4.3.Arrow Theorem [1963]

1. <u>Universality:</u> any set of $n$ weak-orders on $A$ is admissible.
2. <u>Independence:</u> The relative position of two candidates in the collective ranking only depends on their relative position in the individual rankings.
3. <u>Unanimity:</u> The outcome of the aggregation function may
not contradict the voters when they vote unanimously.
4. <u>No dictatorship:</u> there is no dictator


## Sources
- This blogpost is heavily inspired from [Vincent Mousseau](https://www.researchgate.net/profile/Vincent_Mousseau) lectures, my professor at Centrale-Supélec.
- [Layman intuition video](https://www.youtube.com/watch?v=e3GFG0sXIig)

------
