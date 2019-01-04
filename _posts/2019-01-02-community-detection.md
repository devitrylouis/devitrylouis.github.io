---
title: 'Community detection'
date: 2018-11-16
permalink: /posts/2019/01/community-detection/
tags:
  - Network science
---
# Community structure

## Community Structure of large-scale graphs

Different network topologies and sizes will yield different community structure. To examine these discrepancies, we can resort to the <u>conductrance $\Phi(S)$</u> defined by:

$$
\Phi(S) = \frac{\# \text{Outgoing edges}}{\# \text{Edges within}}
$$

<b>Observation:</b> Smaller value of the evaluation measure $\Phi(S)$ implies better community-like properties [Leskovec et al. ’09]

<b>Framing the problem:</b> If we wish to find k= 5 communities in the graph, we have to solve:

$$
\Phi(k) = \text{min}_{S \subset V, \mid S \mid = k} \Phi(S)
$$

## Network Community Profile plot

A great tool to analyze in-depth the community structures, we use the <u>Network Community Profile [Leskovec et al. ’09]</u>, in which we plot best conductance score (minimum) $\Phi(k)$ for each community size $k$.

Once agin, we use the loglog plot.

<b>NCP Plot of Large Real Graphs:</b> A common property arises in large scale networks:

![NCP Plot Examples]()

<b>Observation in Large Graphs:</b>
- For moderate values of $k (\approx 100)$: The conductance score is inversely proportional to the number nodes in community.
- For large values of $k$: The conductance score icreases with the number nodes in community.

<u>Question:</u> How can we explain the observed structure of large graphs?

## Core-Periphery Structure

Each node typically belong to one of two categories:
1. <u>Core:</u> contains a large portion of the graph (~60% of nodes and ~80% of edges). It becomes denser and denser
2. <u>Whiskers:</u> maximal subgraphs connected to the core via a single edge. These are non-trivial structure, which are more than random in shape and size.

<i>Note:</i> We can also consider $k$-whiskers, which are subgraphs connected to the core by $k$ edges. Nodes belonging to $k$-whiskers with low are usually the farthest from the core.

<b>Important point:</b>
- Whiskers are also responsible for the best communities in large graphs (lowest point of NCP plot)
- Match the observations made using the properties of the
Kronecker graphs

## Similar Structural Observations

- Jellyfish model for the Internet topology [Tauro et al. ’01]
- Min-cut plots [Chakrabarty et al. ’04]
    * Perform min-cut recursively
    * Plot the relative size of the minimum cut
- Robustness of large scale social networks [Malliaros, Megalooikonomou, Faloutsos ’12, ‘15]!
– Robustness estimation based on the expansion properties of graphs
– Social networks are expected to have low robustness due to the existence of communities à the (small number of) inter-community edges will act as bottlenecks
– Large scale social graphs tend to be extremely robust
– Structural differences (in terms of robustness and community structure) between different scale graphs!

## Clustering Algorithms and Objective Criteria

Where does this core-structure property comes from?
1. The community detection algorithm? No, as the qualitative shape of the NCP plot is the same, regardless of the algorithm. (Metis + flow based method) [Leskovec et al. ’09]
2. The conductance community evaluation measure? No because all the objective criteria that are based on both internal and external connectivity, show an almost similar qualitatively behavior (a V-like slope in the NCP plot) [Leskovec et al. ’10]


## Conclusions

Large scale real-world graphs present an unusual core-periphery structure with no large, well defined communities. Furthermore, they appear to have important structural differencies in communities between different scale of graphs.

With this in mind, community detection algorithms should take into account these structural observation:
  - Whiskers correspond to the best (conductance-based) communities
  - Bag of whiskers: union of disjoint (disconnected) whiskers are mainly responsible for the best high-quality clusters of larger size (above 100)
  - Need larger high-quality clusters?

## Additional reading

- S. Fortunato. Community detection in graphs. Physics Reports 486,
75-174, 2010
- S. E. Schaeffer. Graph clustering. Computer Science Review, 1(1):
27–64, 2007
- F. D. Malliaros and M. Vazirgiannis. Clustering and community
detection in directed networks: A survey. Physics Reports 533,
95-142, 2013
- S. Fortunato and D. Hric. Community detection in networks: a user
guide. Physics Reports 659, 1-44, 2016
- S. Papadopoulos, Y. Kompatsiaris, A. Vakali, and P. Spyridonos.
Community detection in Social Media: Performance and application
considerations. Data Min Knowl Disc, 24:515–554, 2012

------
