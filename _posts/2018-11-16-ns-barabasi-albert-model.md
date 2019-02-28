---
title: 'Barabási-Albert Model'
date: 2018-11-16
permalink: /posts/2018/11/ns-barabasi-albert-model/
tags:
  - Network science
---
Hubs represent the most striking difference between a random and a scale-free network.

<b>Goal</b>: The very existence of these hubs and the related scale-free topology raises two fundamental questions:

- Why do so different systems as the WWW or the cell converge to a similar scale-free architecture?
- Why does the random network model of Erdős and Rényi fail to reproduce the hubs and the power laws observed in real networks?

<b>Topic:</b> Growth and Preferential Attachment the mechanisms responsible for the emergence of the scale-free property. This is the main topic of this chapter.

# Growth and Preferential Attachment

Hubs and power laws are absent in random networks because of two hidden assumptions of the Erdős-Rényi model, that are violated in real networks.

<b>Growth:</b>
- Random network model assumes that we have a fixed number of nodes $N$.
- Real networks the number of nodes continually grows thanks to the addition of new nodes.

We cannot resort to a static model and our approach must instead acknowledge that networks are the product of a steady growth process.

<b>Preferential attachment:</b>
- <i>Random networks:</i> The random network model assumes that we randomly choose the interaction partners of a node.
- <i>Real networks:</i> New nodes prefer to link to the more connected nodes, a process called preferential attachment.

# The Barabási-Albert Model

We start with $m_{0}$ nodes, the links between which are chosen arbitrarily, as long as each node has at least one link. The network develops following two steps

- <b>Growth:</b> At each timestep we add a new node with $m (\leq m_{0})$ links that connect the new node to $m$ nodes already in the network.
- <b>Preferential attachment:</b> The probability $\Pi (k)$ that a link of the new node connects to node $i$ depends on the degree $k_{i}$ as:
$$ \Pi (k_{i}) = \frac{k_{i}}{\sum_{j}k_{j}} $$

After $t$ timesteps the Barabási-Albert model generates a network with $N = t + m_{0}$ nodes and $m_{0} + m_{t}$ links

<b>Problems:</b> It does not specify
- <i>Initial configuration</i> of the first $m_{0}$ nodes.
- <i>Added one by one vs. simultaneously</i>

<b>The Linearized Chord Diagram (LCD): </b> version of the Barabási-Albert model amenable to exact mathematical calculations.

For $m=1$ we build a graph $G_{1}(t)$ as follows
- Start with $G_{1}(0)$, corresponding to an empty graph with no nodes.
- Given $G_{1}(t-1)$ generate $G_{1}(t)$ by adding the node $v_{t}$ and a single link between $v_{t}$ and $v_{i}$, where $v_{i}$ is chosen with probability
$$
p =
\begin{cases}
\frac{k_{i}}{2t-1} &\text{ if } 1 \leq i \leq t-1 \\
\frac{1}{2t-1} &\text{ if } i=t
\end{cases}
$$

That is, we place a link from the new node $v_{t}$ to node $v_{i}$ with probability $k_{i}/(2t-1)$, where the new link already contributes to the degree of $v_{t}$. Consequently node $v_{t}$ can also link to itself with probability $1/(2t - 1)$, the second term in. Note also that the model permits self-loops and multi-links. Yet, their number becomes negligible in the $t→∞$ limit.

For $m > 1$ we build $G_{m}(t)$ by adding $m$ links from the new node $v_{t}$ one by one, in each step allowing the outward half of the newly added link to contribute to the degrees.

# Degree Dynamics

<b>Time evolution of the Barabási-Albert model:</b> an existing node can increase its degree each time a new node enters the network.

<b>Key idea:</b> approximate $k_{i}$ with a continuous real variable, representing its expectation value over many realizations of the growth process.

</b>Rate of node connecting to $i$:<b>
$$
\begin{align}
\frac{dk_{i}}{dt} &= m \Pi (k_{i})\\
&=m\frac{k_{i}}{\sum_{j=1}^{N-1}k_{j}}\\
&=m\frac{k_{i}}{2mt-m}\\
&=\frac{k_{i}}{2t-1}\\
\end{align}
$$

From this, we can extract:

$$
k_{i}(t) = m(\frac{t}{t_{i}})^{\beta}
$$

where $\beta = \frac{1}{2}$ is the dynamical exponent.

<b>Results:</b>
- All <i>nodes</i> follow the <i>same dynamical law</i>.
- <i>Growth in the degrees is sublinear (i.e. $\beta < 1$):</i> With time the existing nodes compete for links with an increasing pool of other nodes.
- The <i>earlier</i> node $i$ was <i>added</i>, the <i>higher</i> is its <i>degree</i> $k_{i}(t)$. A phenomenon called <i>first-mover advantage phenomenon</i>, athematically tranlated by:
$$
\frac{dk_{i}}{dt} = \frac{m}{2}\frac{1}{\sqrt{tt_{i}}}
$$

<i>Note:</i> In network theory we use event time, advancing our time-step by one each time when there is a change in the network topology.

# Degree Distribution

<b>Goal:</b> Calculate the functional form of $p_{k}$ to understand its origin.

<b>Approximation</b> The continuum theory predicts the degree distribution:
$$
p(k)\approx 2m^{\frac{1}{\beta}}k^{-\gamma} \text{ with } \gamma = \frac{1}{\beta} + 1 = 3
$$

<i>Notes:</i>
- $\beta$ characterizes a node’s temporal evolution
- $\gamma$ characterizes the network topology

<b>Result:</b> The degree distribution reveals a deep relationship between the network's topology and dynamics

<b>Exact degree distribution:</b> with the LCD model:
$$
p_{k} = \frac{2m(m+1)}{k(k+1)(k+2)}
$$

<b>Results:</b>
- For $k$ large $p_{k}\sim k^{-\gamma}$
- $\gamma$ independent of $m$
- $p_{k}$ independent of both time $t$ and size $N$. The model predicts the emergence of a stationary scale-free state.

# The absence of growth or preferential attachment

<b>Model with growth:</b>
- The linear-log plot indicates that the resulting network has an exponential $p_{k} = \frac{e}{m}exp(-k/m)$
- Continuum theory predicts that for Model A ki(t) increases logarithmically with time:
$$
k_{i}(t)= m ln(e\frac{m_{0}+t-1}{m_{0}+t_{i}-1})
$$
- An exponential function decays much faster than a power law, hence it does not support hubs.

<b>Model with preferential attachment:</b>
- For large $t$ the degree of each node also increases linearly with time
$$
k_{i}(t) \approx \frac{2}{N}t
$$
- $L ≪ N$ each new link connects unconnected nodes.
- $p_{k}$ is not stationary
- Converge to a complete graph

# Detect preferential attachment

<b>Goal:</b> Measure $\Pi(k)$ in real networks.

<b>Two distinct hypotheses:</b>
- The likelihood to connect to a node depends on that node’s degree $k$.
- The functional form of $\Pi(k)$ is linear in $k$.

Both hypotheses can be tested by measuring $\Pi(k)$.

<i>Requirement:</i> Have the map of the network at time $t$ and $t + \Delta t$ for $\Delta t$ little.

<b>Result:</b> $\frac{\Delta k_{i}}{\Delta t} \sim \Pi(k_{i})$

The resulting curve can be noisy so we consider the cumulative attachment function:

$$
\pi(k) = \sum_{k_{i}=0}^{k}\Pi (k_{i})
$$

|                                     | $\Pi(k_{i})$      | $\pi(k)$                  |
|-------------------------------------|-------------------|---------------------------|
| Without preferential attachment     | cte               | $\sim k$                  |
| With linear preferential attachment | $k_{i}$           | $\sim k^{2}$              |
| With preferential attachment        | $\sim k^{\alpha}$ | $\Pi(k) \sim k^{2\alpha}$ |

# Non-linear Preferential Attachment

![Non-linear preferential attachment](http://networksciencebook.com/images/ch-05/figure-5-12.jpg)


------
