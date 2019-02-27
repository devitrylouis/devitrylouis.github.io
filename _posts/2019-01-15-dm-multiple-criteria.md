---
title: 'Multiple criteria decision'
date: 2018-12-01
permalink: /posts/2019/01/dm-multiple-criteria/
tags:
  - Decision Modeling
---

Multiple-criteria decision analysis (MCDA) is a sub-discipline of operations research that explicitly evaluates multiple conflicting criteria in decision making (both in daily life and in settings such as business, government and medicine).

For instance, in purchasing a car, cost, comfort, safety, and fuel economy may be some of the main criteria we consider – it is unusual that the cheapest car is the most comfortable and the safest one.

Intuitively, we can think of the criterias as different point of views on the consequences of a decision. With this in mind, our goal is to encode this and structure it.

## 1. Notion of criterion

These alternative viewpoints are typically compared with a criterion $g:A\mapsto \mathbb{R}$ which satisfy:

$$g(a) > g(b) \Rightarrow a \succeq_{g} b, \forall a, b \in A$$

where the relation $\succeq_{g}$ means “at least as good as”.

Now that the definition of a criterion has been given, we will address the following in this section:
1. What is the difference between Mono-Criterion and Multi-Criteria framework?
2. What is a consistant family of criteria?
3. How to build ones?

### 1.1. What is the difference between Mono-Criterion and Multi-Criteria framework?

A majority of operational research problems are addressed using a mono-criterion approach, but this is rather restrictive by definition. To solve this, a multiple criteria approach proves useful. The <b>key idea</b> is to construct a <u>family of criterion</u>, with each criterion representing a “homogenous class of consequences".

Mathematically, this is defined as building $n ≥ 2$ criterion functions $(g_{1}, g_{2}, . . . , g_{n})$, with each $g_{i}$ accounting for a certain dimension of the problem. The evaluation of this criterion is straightforward for a given alternative $a \in A$:

$$
\begin{align}
g:A & \mapsto \mathbb{R}^{n}\\
a & \rightarrow (g_{1}(a), g_{2}(a), . . . , g_{n}(a))\\
\end{align}
$$

### 1.2. What is a consistant family of criteria?

It is now time to put some structure on the codomain of $g$ (see a sound basis). Our aim to construct a consistent family $F$ of criterion and as for what are the conditions of such families, there are three axioms that must hold:

> <b>Consistent axioms:</b>
> 1. <u>Exhausitivity:</u> Any distinct pair of alternatives $a$ and $b$ are different in the codomain fo $F$, and can thus be evaluated without loss of signification. Mathematically, if $\succeq$ is any of the operations  preference, indifference, incomparability, then:
> $$ \textbf{g}(a) = \textbf{g}(b) \Rightarrow \begin{cases}
c \succeq a \Rightarrow c \succeq b\\
a \succeq c \Rightarrow b \succeq c\\
\end{cases}, \forall c \in A $$
> 2. <u>Cohesion:</u> Ensures that there are some kind of local and consistent order. Specifically, if $a^{+}$ and $a^{-}$ are alternatives derived from $a\in A$, then:
> $$ \textbf{g}(a^{+}) \geq \textbf{g}(a) \geq \textbf{g}(a^{-}) $$
> 3. <u>Non-redundancy:</u> $F$ is the minimal family for which the first two axioms hold (i.e. delete at least one criterion and axiom 1 or 2 is invalidated).

In practice, checking the validity of these three axioms is a delicate matter.

### 1.3. How to build ones?

From his heavy use in critical parts of businesses, there are important requirements that must be met:
1. <u>Readability:</u> The family $F$ is of low dimension (see interpretable)
2. <u>Operational:</u> The more operational (simple, efficient...) a criterion is, the better.
3. <u>Accepted:</u> The concerned audience should aggree on the family $F$.

Just like Machine Learning operational case demands heavy preprocessing and validation, constructing family comes with its own set of challenges. While there are no go-to methods, heuristics exhist. The two more common ones are:
- <u>Top-down:</u> Divide and conquer
- <u>Bottom-up:</u> Agglomerative proceeding

One should nonetheless keep in mind that the problem is more generally described by:

1. <u>Choice:</u> Find the best subset of criterions.
2. <u>Sorting:</u> Partition the set of alternatives w.r.t. pre-existing norms.
3. <u>Ranking:</u> Rank alternatives in terms of desirability (from best to worst).

As for the types of criteria, the most encountered are:
1. <u>Natural criterias:</u> Most often, business problems aim to reduce overall costs and increase efficiency. Using the costs or the duration of a process as criterions are ideal in this settings.
2. <u>Proxy:</u> When the variable is intractable, a proxy attribute proves to be useful (measure [Velib](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design) use over months to quantify greener mode of transportations)
3. <u>Custom criteria</u>, generally made by aggregation of simpler criteria.

## 2. Dominance, efficience and preferential independence

### 2.1. Dominance and efficience

Now that multiple criteria families have been defined and structured, we are interested in using them to discriminate good alternatives from bad one. To this aim, we define a basic measure, called the <u>dominance</u>.

We say that $a$ dominates $b$ - and write $a\Delta b$ - if $ \textbf{g}(a) \geq \textbf{g}(b)$, with one strict inequality.

Despite being unable to compare all pairs of alternatives, the dominance relation $\Delta$ expresses uninamity toward one of the two alternatives and this can be used more globally by finding efficient alternatives.

An <u>efficient alternative</u> $a\in A$ is one that verify:

$$
\not\exists b \in A \text{ such that }b\Delta a
$$

Given the low dimensionaliy of most Decision Models (refer to the readability condition above), one can compute the efficient frontier, that offers the maximum expected returns for a given level of risk.

![Efficient grontier](https://cdn-images-1.medium.com/max/1280/1*4Ke6NhIUYPR12Sa2nrIpxw.jpeg)

The efficient frontier concept was introduced by Nobel Laureate Harry Markowitz in 1952 and is a cornerstone of modern portfolio theory.

<i>Note:</i> Because of the non-surjectivity of the family criterion $\textbf{g}$, there exists an ideal point $(z_{1}, ..., z_{n})$ that maximizes the criterion $\textbf{g}$:

$$ z_{j} = \text{max}_{a}g_{j}(a)$$

Bust most of the times, it does not match an existing alternative.

### 2.2. Preferential independence

In multiattribute utility theory, it is simpler to provide a simple form (additive / multiplicative) for the utility function. However, certain conditions must hold in order to use these two forms and the main one is definitely <u>preferential independence</u>.

An attribute is preferentially independent from all other attributes when changes in the rank ordering of preferences of other attributes does not change the preference order of the attribute.

Suppose we have 4 alternatives $a, b, c, d$ and a subset of criteria $J\subset F$ such that $a\succeq b \Leftrightarrow c \succeq d$ with:

- $g_{i}(a)=g_{i}(b),\forall i\not\in J$
- $g_{i}(c)=g_{i}(d),\forall i\not\in J$
- $g_{i}(a)=g_{i}(a),\forall i\in J$
- $g_{i}(b)=g_{i}(d),\forall i\in J$

Then $J$ is preferentially independent in $F$. This means that preferences on alternatives which differ only on $J$ are not dependent on common evaluations out of $J$.

For example, let's say the two attributes for a car are color (red/black) and style (sports car/SUV). Suppose the decision maker prefers a red sports car over a black sports car. If the decision maker also prefers a red SUV over a black SUV, then the color is preferentially independent of style: Red is preferred over black, regardless of style.

<i>Note:</i> In practice, one should group the subset of concerned criteria into a single criterion which is formally equivalent.

### 2.3. Notion of preference information

As stated above, the dominance relation $\Delta$ is by definition limited, but preferential independance bring a new piece of information and thus constitute a natural extension; it helps reduce the dimensionality of our problem.

We call this additional piece of information <u>preference information</u> and for the Decision Model, it refers to its value system opinions and convictions. Among those informations, one can distinguish:
- <u>Intra-criterion</u> which is bound to a unique criterion.
- <u>Inter-criteria</u> which span over several criterions.

### 2.4. Invariance w.r.t. a third alternative

The comparison of two alternatives $a_{i}\in A$ and $a_{j}\in A$ does not depend on the presence/absence of a third alternative $b$. This means that if $a_{i} \succeq a_{j}$ in $A$, then $a_{i} \succeq a_{j}$ in $A\cup \{ b \}$

## 3. Multiple Criteria Aggregation Procedure

The general framework in decision modeling is the following:

![framework](/images/dm_mcap.png)

There are several forms of MCAP, each with its pros and cons. We list commonly used ones in this section.

### 3.1. Weighted sum

This method is based on a weighted account of each criterion.

$$
\begin{cases}
a\succeq_{P} b \Leftrightarrow \sum_{i \in F} w_{i}g_{i}(a) > \sum_{i \in F} w_{i}g_{i}(b)\\
a\succeq_{I} b \Leftrightarrow \sum_{i \in F} w_{i}g_{i}(a) = \sum_{i \in F} w_{i}g_{i}(b)\\
\end{cases}
$$

Though it is basic of use, it requires to be able to compare units of criterion (i.e. what does one unit of $g_{1}$ mean in terms of $g_{2}$ units).

### 3.2. Lexicographic aggregation

The basic principle of this aggregator is to add an importance order $>>$ on the family $F$ so that if the $k$ first criterias discriminate two alternatives then the remaining one can be neglected. Formally:

$$
\begin{cases}
a\succeq_{P} b \Leftrightarrow \begin{cases}
\exists j \in F \text{ s.t. } g_{j}(a) > g_{j}(b)\\
g_{i}(a) = g_{i}(b), \forall i \text{ such that } g_{i}>>g_{j}
\end{cases}\\
a\succeq_{I}b \Leftrightarrow g_{i}(a) = g_{i}(b), \forall i \in F
\end{cases}
$$

And contrary to the weighted sum, this aggregator is non-compensoratory (see below for the definition of non-compensoratory).

### 3.3. Majority rule (condorcet)

Each criterion $g_{i}$ is given a "voting power" $w_{i}$ and its sum over all criteria discriminate two alternatives:

$$
\begin{cases}
a \succeq_{P}b \Leftrightarrow \sum_{j \in p(a, b)} w_{i} > \sum_{j \in p(b, a)} w_{i}\\
a \succeq_{I}b \Leftrightarrow a \not\succeq_{P}b \text{ and }b \not\succeq_{P}a
\end{cases}
$$

where $p(a, b) = \{ j \in F \text{ s.t. } a \succeq_{P} b \}$

Although powerful and suited to reflect on potentially real voting problems, this aggregator is [intransitive](https://en.wikipedia.org/wiki/Intransitivity) because of Condorcet paradox.

### 3.4. Sum of ranks (Borda rule)

The basic principle is to rank alternatives independently on each criterion and consider their sum:

$$
\begin{cases}
a \succeq_{P}b \Leftrightarrow \sum_{j \in F} r_{j}(a) > \sum_{j \in F} r_{j}(a)\\
a \succeq_{I}b \Leftrightarrow \sum_{j \in F} r_{j}(a) = \sum_{j \in F} r_{j}(a)\\
\end{cases}
$$

Much like the weighted sum, possibilities of compensation among criteria do exist.

<i>Note:</i> $r$ is not the actual ranking (the better is ranked first) but the other way around.

### 3.5. Compensatoriness

The compensatoriness of an aggregation procedure refers to the extend by which a disadvantage on a criterion can be balanced by an advantage on another criterion (lexicography, weighted sum).

Mathematically, an aggregation procedure is said to be <u>fully non-compensatory</u> if and only if:

$$
\forall a, b, c, d \text{ s.t. }p(a, b) = p(c, d) \text{ and } p(b, a)=p(d, c)
$$

The more an aggregation procedure breaks this property, the more it allows for compensation.

## Sources

This blogpost is heavily inspired from [Vincent Mousseau](https://www.researchgate.net/profile/Vincent_Mousseau) lectures, my professor at Centrale-Supélec. In particular, the image of the general MCAP framework is his.

- [Wikipedia MCDA](https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis)
[Top down](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design)
- [Investopedia - Efficient frontier](https://www.investopedia.com/terms/e/efficientfrontier.asp)
- [Medium - Efficient frontier](https://medium.com/python-data/effient-frontier-in-python-34b0c3043314)

------
