---
title: 'The scale free property'
date: 2018-11-16
permalink: /posts/2018/11/scale-free-property/
tags:
  - Network science
---
Hubs are encountered in most real networks. They represent a signature of a deeper organizing principle that we call the scale-free property.

Intrinsically linked to the degree distribution of real networks, which allows us to uncover and characterize scale-free network and further - from communities to spreading processes.

## Power Laws and Scale-Free Networks

Most real networks degree distribution do not have the expected Poisson distribution. A log-log plot of real networksreveal that most degree distribution are well approximated with:

<b>Definition (Power law distribution):</b> and its degree exponent $\gamma$:
$$
p_{k} = k^{—\gamma}
$$

<b>Definition (Scale-free network):</b> is a network whose degree distribution follows a power law.

<i>Note:</i> In undirected networks, we distinguish:

$$
\begin{align}
p_{k_{in}} &= k_{in}^{—\gamma_{in}}\\
p_{k_{out}} &= k_{out}^{—\gamma_{out}}
\end{align}
$$

<b>Discrete Formalism:</b>
$p_{k}=Ck^{-\gamma} = \frac{k^{-\gamma}}{\zeta(-\gamma)}$

<b>Continuous Formalism:</b>
$$p_{k}=Ck^{-\gamma} = (\gamma - 1)k_{min}^{\gamma-1}k^{-\gamma}$$

<i>80/20 Rule:</i> In real networks, most links points to a small amount of nodes. These nodes are hubs.

## Hubs

The main difference between a random and a scale-free network comes in the <i>tail of the degree distribution</i>.

|                     | Distribution | Max hub size                               | Hub presence | Complexity                  |
|---------------------|--------------|--------------------------------------------|--------------|-----------------------------|
| Random Networks     | Exponential  | $k_{max} = k_{min} + \frac{ln(N)}{\gamma}$ | Unlikely     | $O(log(n))$                 |
| Random Networks     | Poisson      | Slower than log(n)                         | Unlikely     | $\approx O(log(n))$         |
| Scale-free networks | Power        | $k_{max} = k_{min} N^{\frac{1}{\gamma-1}}$ | Naturally    | $O(N^{\frac{1}{\gamma-1}})$ |

## The Meaning of Scale-Free

<b>Terminology (scale-free):</b> rooted in the theory of phase transitions (statistical physics) that extensively explored power laws in the 1960s and 1970s.

<b>Definition ($n$-th moment):</b> of the degree distribution is defined as
$$ \langle k^{n} \rangle = \sum_{k_{min}}^{\infty}k^{n}p_{k} \approx \int_{k_{min}}^{\infty}k^{n}p(k)dk $$

<b>Interpretations:</b>
1. The first moment is the <b>average degree</b> $\langle k \rangle$
2. The second moment $\langle k^{2} \rangle$, helps us calculate the <b>variance</b> $\sigma^{2} = \langle k^{2} \rangle − \langle k^{2} \rangle$, measuring the spread in the degrees.
3. The third moment $\langle k^{3} \rangle$ determines the <b>skewness</b> of a distribution, telling us how symmetric is $p_{k}$ around the average $\langle k \rangle$

<b>Property (Power law n-th moment):</b>
$$\langle k^{n} \rangle = \int_{k_{min}}^{\infty}k^{n}p(k)dk = C\frac{k_{max}^{n-\gamma+1}-k_{min}^{n-\gamma+1}}{n-\gamma + 1}$$

<i>Notes:</i>
- k_{min} is typically fixed
- k_{max} increases with the system size

<b>Key takeaway:</b> The asymptotic behavior depends on \gamma.
- $n \leq \gamma−1 \Rightarrow n$-th moment is finite.
- $n > \gamma−1 \Rightarrow n$-th moment diverges.

<i>Note:</i> Most scale-free networks the degree exponent γ is between 2 and 3.

<b>Scale?</b>
- Random Networks: Have an intrinsic scale $\langle k\rangle$
- Scale-free Networks: Lack a scale (infinite variance if $\gamma < 3$) and for a randomly chosen node, we do not know what to expect.

<i>Note:</i> This divergence is the origin of some of the most intriguing properties of scale-free networks, from their robustness to random failures to the anomalous spread of viruses.

## Universality principle

The power law approximates well lots of real networks. It is this diversity that prompts us to call the scale-free property a universal network characteristic.

This prompts us to address several issues pertaining to plotting and fitting power laws:

<b>Plotting the Degree Distribution:</b>
- <i>Perform $log_{10}-log_{10}$ plot</i>
- <i>Use logarithmic binning</i>
- <i>Use Cumulative Distribution</i>

<i>Notes:</i>
- Careful! $p_{k} = 0$ or $k=0$ are not shown on a log-log plot as $log(0)=-\infty$.
- Logarithm binning ensure that each bin has a comparable number of nodes (linear binning does not).
- Cumulative distribution enhances the statistical significance the high-degree region.

<b>Some recurring features:</b>
- <i>Low-degree saturation:</i> Its signature is a flattened $p_{k}$ for $k < k_{sat}$
- <i>High-degree cutoff:</i> rapid drop in $pk$ for $k > k_{cut}$, ( fewer high-degree nodes than expected in a pure power law)

<b>Alternative fitting procedure:</b>
$$ p_{x} = a(K+K_{sat})^{-\gamma}exp(-\frac{k}{k_{cut}}) $$

The presence of such cutoffs indicates the presence of additional phenomena that need to be understood.

### Measuring the Degree Exponent

A quick estimate of the degree exponent can be obtained by fitting a straight line to pk on a log-log plot.Yet, this approach can be affected by systematic biases, resulting in an incorrect γ. The statistical tools available to estimate γ are discussed in ADVANCED TOPICS 4.C.

### The shape of $p_{k}$

ADVANCED TOPICS

## Ultra-small Property

Do hubs affect the small world property?

distances in a scale-free network are smaller than the distances observed in an equivalent random network.

dependence of the average distance \langled〉 on the system size N

$$
\langle d \rangle \sim \begin{cases}
const. &\text{ if }\gamma = 2\\
ln(ln(N)) &\text{ if }2 < \gamma < 3\\
\frac{ln(N)}{ln(ln(N))} &\text{ if }\gamma = 3\\
ln(N) &\text{ if }\gamma > 3\\
\end{cases}
$$

### Anomalous Regime ($\gamma = 2$)

biggest hub grows linearly with the system size, i.e. kmax ~ N

hub and spoke configuration in which all nodes are close to each other because they all connect to the same central hub. In this regime the average path length does not depend on N.

### Ultra-Small World (2 ‹ γ ‹ 3)

average distance increases as lnlnN (slower growth than the lnN derived for random networks)
hubs radically reduce the path length (linking to a large number of small-degree nodes, creating short distances between them)

### Critical Point (γ = 3)

theoretical interest, as the second moment of the degree distribution does not diverge any longer

At this critical point the lnN dependence encountered for random networks returns. Yet, the calculations indicate the presence of a double logarithmic correction lnlnN [29, 31], which shrinks the distances compared to a random network of similar size.

### Small world

$\langle k^{2} \rangle$ is finite and the average distance follows the small world result derived for random networks. While hubs continue to be present, for γ > 3 they are not sufficiently large and numerous to have a significant impact on the distance between the nodes.

Result: The more pronounced the hubs are, the more effectively they shrink the distances between nodes

In summary the scale-free property has several effects on network distances:
- Shrinks the average path lengths
- Changes the dependence of 〈d〉 on the system size
- Only for γ › 3 we recover the lnN dependence

## The Role of the Degree Exponent

![Degree exponent](http://networksciencebook.com/images/ch-04/figure-box-4-5.jpg)

## Generating Networks with Arbitrary Degree Distribution

<b>Goal:</b> Generate networks with an arbitrary p_{k}

------
