---
title: 'The Random Network Model'
date: 2018-11-15
permalink: /posts/2018/11/random_network/
tags:
  - Network Science
---
Network science aims to build models that reproduce the properties of real networks. As most encountered networks are irregular alnd look like they were spun randomly.

Assumption: Creating a random network boils down to placing the links randomly between the nodes.

<b>Definition (Random Network):</b> A random network consists of $N$ nodes where each node pair is connected with probability $p$.

<b>Model construction:</b>
- <b>Step 1:</b> Start with N isolated nodes.
- <b>Step 1:</b> Select a node pair and generate a random number between $0$ and 1. If the number exceeds $p$, connect the selected node pair with a link, otherwise leave them disconnected.
- <b>Step 3:</b> Repeat Step 2 for each of the $N(N-1)/2$ node pairs.

<i>Terminology:</i> random network is called the <b>Erdős-Rényi network</b>.

## Number of Links

Let us first note that the probability that a particular realization of a random network has exactly L links is

$$ p_{L} = \binom{\frac{N(N-1)}{2}}{L}p^{L}(1-p)^{\frac{N(N-1)}{2} - L} $$

<b>Expected number of links:</b>
$$\langle L \rangle = p\frac{N(N-1)}{2} = pL_{max} $$

<b>Average degree:</b>
$\langle k \rangle = \frac{2\langle L \rangle}{N}$

## Degree Distribution

![Binomial vs. Poisson](http://networksciencebook.com/images/ch-03/figure-3-4.jpg)

The exact form of the degree distribution of a random network is the binomial distribution. For sparse networks: $N ›› \langle k \rangle$, the binomial is well approximated by a Poisson distribution.

- Both formulas describe the same distribution and have the identical properties
- Expressed in terms of different parameters:
    * <i>Binomial distribution:</i> $p$ and $N$
    $$
    p_{k} = \binom{N-1}{k}p^{k}(1-p)^{N - 1 - k}
    $$
    * <i>Poisson distribution:</i> $\langle k \rangle$
    $$
    p_{k} = e^{-\langle k \rangle}\frac{\langle k \rangle}{k!}
    $$

Poisson distribution is only an approximation to the degree distribution of a random network, thanks to its analytical simplicity, it is the preferred form for $p_{k}$.

## Real Networks are Not Poisson

<b>Result:</b> in a large random network the degree of most nodes is in the narrow vicinity of \langle k \rangle

<b>Degree distribution revisited:</b> Using the sterling approximation, we rewrite:

$$
p_{k}=\frac{e^{-\langle k \rangle}}{\sqrt{2\pi k}}(\frac{e\langle k \rangle}{k})^{k}
$$

The above predicts that in a random network the chance of observing a hub decreases faster than exponentially.

<b>Dire consequence:</b> random network model underestimates the size and the frequency of the high degree nodes, as well as the number of low degree nodes.

## The Evolution of a Random Network

To quantify how a network evolve, we first inspect how the size of the largest connected cluster within the network, $N_{G}$, varies with $\langle k \rangle$.

<b>Property:</b>
- Giant component $\Leftrightarrow$ each node has on average more than one link

<b>Four topologically distinct regimes:</b>

- <i>Subcritical Regime ($0 ‹ \langle k \rangle ‹ 1$)</i>: network consists of numerous tiny components, whose size follows the exponential distribution (comparable sizes).

- <i>Critical Point ($\langle k \rangle = 1$)</i>: most nodes are located in numerous small components, whose size distribution follows the power law (components of rather different sizes coexist). Small components are mainly trees, while the giant component may contain loops.

- <i>Supercritical Regime ($\langle k \rangle › 1$):</i>
Numerous isolated components coexist with the giant component, their size distribution following (3.35). These small components are trees, while the giant component contains loops and cycles. The supercritical regime lasts until all nodes are absorbed by the giant component.

- <i>Connected Regime:</i> $\langle k \rangle › ln(N)$
  * Average degree at which this happens $\langle k \rangle=ln(N)$
  * $ln(N) / N → 0$ for large $N \Rightarrow$ Network is relatively sparse
  * Network is a complete graph $\Leftrightarrow \langle k \rangle = N - 1$.

## Real Networks are Supercritical

The average degree of real networks is well beyond the $\langle k \rangle = 1$ threshold.

- <b>Verified with real networks:</b> Real networks are supercritical $\Rightarrow$ Networks are expected to have a giant component.
- <b>Not verified in real networks:</b> Giant component should coexist with many disconnected components.

<b>Note:</i> Real Networks can stay connected despite failing the $\langle k \rangle ›› ln(N)$ criteria

## Small Worlds

<b>Small world phenomenon</b> states that if you choose any two individuals anywhere on Earth, you will find a path of at most six acquaintances between them.

<b>Meaning:</b> distance between two randomly chosen nodes in a network is short.

What does short (or small) mean, i.e. short compared to what?

Expected number of nodes up to distance $d$ from our starting node:
$N(d) \approx 1 + \langle k \rangle + \langle k \rangle^{2} + ... + \langle k \rangle^{d} = \frac{\langle k \rangle^{d} - 1}{\langle k \rangle - 1}$

identify the maximum distance, d_{max}:

$$
\begin{align}
N(d_{max}) \approx N \\
\langle k \rangle^{d_{max}} \approx N \\
d_{max} \approx \frac{ln(N)}{ln(\langle k rangle)}
\end{align}
$$

Typically the small world property is defined by:

$$
\langle d \rangle \approx \frac{ln(N)}{ln(\langle k rangle)}
$$

<b>Key takeaways:</b>
- Average path length or the diameter depends logarithmically on the system size.
- The $\frac{1}{ln \rangle k \rangle}$ term implies that the denser the network, the smaller is the distance between the nodes.
- In real networks the number of nodes at distance d › ‹d› drops rapidly

How do we explain the existence of these short distances?
------
