---
title: 'Link prediction'
date: 2018-11-16
permalink: /posts/2019/01/link-prediction/
tags:
  - Network science
comments: true
---

# Link prediction

In this lecture, we learn the basics of how to perform unsupervised link prediction and supervised ling prediction. We will overview the following techniques:

<b>Motivation</b>
- Recommending new friends in online social networks
- Suggesting interactions between the members of a company/
organization that are external to the hierarchical structure of the
organization itself
- Suggesting collaborations between researchers based on coauthorship
- Predicting connections between members of terrorist organizations
who have not been directly observed to work together
- Overcoming the data-sparsity problem in recommender systems
using collaborative filtering


## Problem formulation

<b>The link prediction task:</b> Given $G[t_{0}, t_{0'}]$ a graph on edges up to time $t_{0'}$, output a ranked list $L$ of links (not in $G[t_{0}, t_{0'}]$) that are predicted to appear in $G[t_{1}, t_{1'}]$

<u>Evaluation:</u> (see [Liben-Nowell and Kleinberg '03])
– $n=|E_{new}|$: number of news edges that appear during the test period $[t_{1}, t_{1'}]$!
– Take top $n$ elements of list $L$ and count the correct edges

<b>Considerations:</b> Networks evolve over time and therefore only predict only edges whose endpoints appear in both the training and test intervals.

<u>Usually:</u> Predict new edges between the nodes in Core (a subset of nodes). Here, the core is all nodes that are incident to at least $k_{training}$ edges in $G[t_{0}, t_{'0}]$, and at least $k_{test}$ edges in $G[t_{1}, t_{'1}]$

<b>Goal:</b> Predict $E_{new}$, the missing edges in the core at test time.

## Link Prediction - Evaluation

1. For each pair of nodes $(x, y)$, compute score $c(x, y)$ (# of common neighbors of x and y)
2. Sort pairs $(x, y)$ by the decreasing score $c(x, y)$ (only consider/predict edges where both endpoints are in the core)
3. Predict the top $n$ pairs of new links
4. See which of those links actually appear in $G[t_{1}, t_{'1}]$

## Methods of Link Prediction

<b>Big question:</b> How to assign score $c(x, y)$ between two nodes $x$ and $y$?

We should use some form of similarity or node proximity of $x$ and $y$ based solely on graph features. There are many different ways to formalize this but we will focus on two categories of methods:
1. <u>Neighborhood-based:</u> Number of shared neighbors
2. <u>Network proximity-based methods:</u> Paths between $x$ and $y$

| Neighborhood-based | Proximity-based |
|:------------------------:|:-----------------------------:|
| Common neighbors overlap | Shortest path length |
| Jaccard coefficient | $\text{Katz}_{\beta}$ measure |
| Adamic/Adar index | RW: Hitting and commute time |
| Preferential attachment | RW:PageRank and SimRank |

### Neighborhood-based Methods

<b>Intuition:</b> The larger the overlap of the neighbors of two nodes, the more likely the nodes to be linked in the future.

Let $\Gamma(x)$ be the set of neighbors of $x$ in G_{old}.

<u>Common neighbors:</u> Number of common neighbors
$$c(x, y) = \mid \Gamma(x) \cap \Gamma(y) \mid$$

<u>Jaccard coefficient:</u> The probability that both $x$ and $y$
have common neighbors:$c(x, y) = \frac{\mid \Gamma(x) \cap \Gamma(y) \mid}{\mid \Gamma(x) \cup \Gamma(y) \mid}$

<u>Adamic/Adar:</u> Assigns large weights to common neighbors $z$ of $x$ and $y$ which themselves have few neighbors (weight rare features more heavily) $$c(x, y) = \sum_{z\in\Gamma(x) \cap \Gamma(y)} \frac{1}{\text{log}\mid\Gamma(z)\mid}$$

<u>Preferential attachment:</u> Based on the intuition that the probability that a new edge has node $x$ as its endpoint is proportional to $|\Gamma(x)|$, i.e., nodes prefer to form ties with 'popular' nodes:
$$ c(x, y) = \mid\Gamma(x)\mid\cdot\mid\Gamma(y)\mid $$

<i>Note:</i> The number of kneighbors $\mid \Gamma(x) \mid$ is the degree of $x$.

### Proximity-based Methods

#### Ensemble of All Paths

<b>Intuition:</b> The “closer” two nodes are in the network, the more likely is to be linked in the future

<u>Shortest Path-Based:</u>
$$c(x, y) = - d(x, y)
$$

<i>In practice:</i> (?)
Some further normalization may needed
If there are more than $n$ pairs of nodes at the shortest path length $l$, order them at random

<u>\text{Katz}_{\beta} measure:</u> We denote by $l$ the set of all paths of length $l$ from $x$ to $y$
$$
c(x, y) = \sum_{l=1}^{\infty}\beta^{l}\cdot\mid\text{paths}_{x, y}^{\langle l \rangle}\mid
$$

<i>Note:</i> The measure can be expressed with the adjacency matrix because $\beta^{l}\cdot\mid\text{paths}_{x, y}^{\langle l \rangle}\mid = \beta^{l} A_{xy}^{l}$

<u>Closed form solution:</u> Because of this , the matrix of scores
$$
C = (I-\beta A)^{-1} - I
$$

<i>Note:</i> For a weighted graph, we replace use the weighted adjacency matrix (at least for step one).

<i>In practice:</i>
- $0 < \beta < 1$ is a parameter of the predictor, exponentially damped to count short paths more heavily
- Small $\beta$ yields predictions much like common neighbors

#### Random Walk-based Methods

Consider a random walk on $G_{old}$ that starts at $x$ and iteratively moves to a neighbor of $x$ chosen uniformly at random from $\Gamma(x)$.

<u>Hitting time:</u> $H_{x,y}$ (from $x$ to $y$): the expected number of steps it takes for the random walk starting at $x$ to reach $$
$$c(x, y) = - H_{x,y}$$

<u>Commute time:</u> $Comm(x, y)$ (from $x$ to $y$): the expected number of steps to travel from $x$ to $y$ and from $y$ to $x$
$$c(x, y) = - (H_{x,y} + H_{y,x})$$

### SimRank

## Evaluation
### Evaluation and results
### How to Evaluate the Prediction?
### Evaluation: Baseline Predictor
### Relative Average Performance

## Additional Materiam
### Discussion and Extensions
### Features
### Experimental Results

# Supervised random walks for link prediction
## Motivation
## Overview
## Supervised Link prediction
## Supervised Random Walks
## SRW: Prediction
## Personalized PageRank
The Optimization Problem
Making Constraints “Soft”
Solving the Problem: Intuition
Data: Facebook
Experimental Setting
Experimental Results – Facebook (1/2)

Experimental Results - Co-Authorship

Arxiv Hep-Ph collaboration network
– Poor performance of unsupervised methods
– SRW gives a boost of 25%

------
