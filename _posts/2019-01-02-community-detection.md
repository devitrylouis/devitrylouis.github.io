---
title: 'Community detection'
date: 2018-11-16
permalink: /posts/2019/01/community-detection/
tags:
  - Network science
---

The notion of community structure captures the tendency of nodes to be organized into modules (communities, clusters, groups) – members within a community are more similar among each other.

Typically, the communities in graphs correspond to densely connected entities, i.e. set of nodes which display better connections between its members, than to the rest of the network.

<b>Why is this happening?</b>
– Individuals are typically organized into social groups (e.g., family, associations, profession)
– Web pages can form groups according to their topic

## Definition

The property of community structure is difficult to be defined:

- There is no universal definition of the problem
- It depends heavily on the application domain and the properties of the graph under consideration

The most widely used notion/definition of communities is based on the number of edges within a group (density) compared to the number of edges between different groups.

A community corresponds to a group of nodes with more intracluster edges than inter-clusters edges

<b>Granovetter’s theory:</b> suggests that networks are composed by tightly connected sets of nodes (see Intra-community vs. inter-community density).

<b>Related work:</b> [Newman ‘03], [Newman and Girvan ‘04], [Schaeffer ‘07], [Fortunato ‘10], [Danon et al. ‘05], [Coscia et al. 11]

## Community Detection

In this section, we give an overview of techniques which aim to automatically find such densely connected groups of nodes such that detected clusters would then correspond to real groups.

### Evaluate the quality of communities

<b>Classical approach:</b>
- Internal connectivity (intra-community edges)
- External connectivity (inter-community edges)

<b>Use random networks neutral communities:</b>
Contrary to real networks, random networks are not expected to present inherent community structure. Therefore, an analysis of the differences between the two might reveal some patterns.

To measure this phenomenon, we compare the number of edges that lie within a community to the expected one in case of random graphs with the same degree distribution. This is called modularity.

$$
Q = \sum_{c \in C} \text{#} \{ \text{ edges } \in c\} - \text{#} \{ \text{ expexted edges } \in c\}
$$

The modularity function $Q$ is a a measure for assessing the strength of communities.

### Modularity

<b>Expected number of edges of a random network?</b>
For a random graph models (with the same degree distribution), the probability $P_{ij}$ of an edge between nodes $i$ and $j$ with degrees $k_{i}$ and $k_{j}$ respectively is:

$$P_{ij} = \frac{k_{i} k_{j}}{2m}$$

where:
- $k_{i}$ is the degree of node $i$
- $m = \mid E \mid  = \frac{1}{2}\sum_{i} k_{i}$ is the number of edges

<b>Formal definition:</b>

$$
Q = \frac{1}{2m}\sum_{i, j}(A_{ij} - P_{i, j})\delta (C_{i}, C_{j})
$$

where:
- $A$ is the adjacency matrix
- $P_{ij}$ is defined above
- $m$ is the number of edges in the graph
- $C_{i}$ is the community of node $i$
- $\delta$ is the Kronecker function ($1$ if both nodes $i$ and $j$ belong to the same community ($C_{i} = C_{j}$), $0$ otherwise).

### Properties

<b>Good communities:</b> Larger modularity $Q$ indicates better communities (more than random intra-cluster density)
- The community structure is better if the number of internal edges exceed the expected number of edges.
- $Q$ in the range of $0.3 - 0.7$ means significant community structure
- Modularity value is always $-1 < Q < 1$!

<b>Negative values:<b>
- If each node is a community itself
- No partitions with positive modularity means the absence of community structure.
- Partitions with large negative modularity implies the existence of subgraphs with small internal number of edges and large number of inter-community edges.

<b>Related work:</b> [Newman and Girvan ‘04], [Newman ‘06], [Fortunato ‘10]

<b>Applications</b> Modularity can be applied to a variety of tasks:
- As quality function in clustering algorithms
- As evaluation measure for comparison of different partitions or algorithms
- As criterion for reducing the size of a graph (Size reduction preserving modularity [Arenas et al. ‘07])!
- As a community detection algorithm itself: Modularity optimization!

### Girvan-Newman’s Method

<b>TL; DR:</b> It is a divisive hierarchical clustering based on the notion of edge betweenness centrality, which roughly corresponds to the number of shortest paths passing through the edge.

<b>Algorithm:</b>
1. Calculate the betweenness centrality of all edges in the graph
2. Remove the edge with the highest betweenness score
3. Recalculate betweenness for all edges affected by the removal
4. Repeat step 2 until no edges remain

<b>Complexity: </b> $\mathcal{O}(m^{2}n)$ (or $\mathcal{O}(n^{3})$ in sparse graphs)

<b>Evaluating</b>
– The output of the algorithm is in the form of a dendrogram (stop the algorithm at some point)!
– Use modularity as a criterion to cut the dendrogram and terminate the algorithm ($Q ~= 0.3-0.7$ indicates good partitions)

# Modularity optimization

As stated earlier, high values of modularity indicate good quality of partitions

<b>Goal:</b> Find the partition that corresponds to the maximum value of modularity

<b>Modularity maximization problem</b>
– Computational difficult problem [Brandes et al. ‘06]
– Approximation techniques and heuristics

<b>Four main categories of techniques</b>
1. Greedy techniques
2. Spectral optimization
3. Simulated annealing
4. Extremal optimization

## Greedy techniques

### Newman’s algorithm [Newman ’04]

TL; DR: It is an agglomerative (bottom-up) hierarchical clustering algorithm who works by repeatedly joining pairs of communities that achieve the greatest
increase of modularity (dendrogram representation).

<b>Algorithm:</b>
1. Initially, each node of the graph belongs to its own cluster (n)
2. Repeatedly, join communities in pairs by adding edges
  a. At each step, choose the pairs that achieve the greatest increase (or minimum decrease) of modularity
  b. Consider only pairs of communities between which there exist edges (merging communities that do not share edges, it can never improve modularity)

<b>Complexity:</b> $\mathcal{0}((m+n) n)$ (or $\mathcal{0}(n^{2})$ in sparse graphs)

### Variants

Many variants - such as Clauset, Newman and Moore) - use the <u>key idea</u> of <u>sparsity</u>. More specifically, they use a <b>max-heap</b>:
  - A sparse matrix for storing the variations of modularity $\Delta Q_{i,j}$ after joining two communities $i, j$
  - A max-heap data structure for the largest element of each row of matrix $\Delta Q_{i,j}$ (fast update time and constant time for finndmax() operation)

<u>Complexity:</u> $\mathcal{0}(m d logn)$, $d$ is the depth of the dendrogram describing the performed partitions (the community structure). And $\mathcal{0}(n log^{2} n)$ for sparse graphs as $d \approx log n$.

### Spectral Optimization

<b>TL; DR:</b> Directly optimize modularity using spectral techniques.

<b>Goal:</b> Assign the nodes into two communities, $X$ and $Y$

Let $s$ is the indicator variable for nodes in $X$ ($+1$) or in $Y$ ($-1$). Then we obtain:

$$
Q = \frac{1}{4m}s^{T}B^{T}
$$

where $B_{ij} = A_{ij} - P_{ij}$ is the <b>modularity matrix</b>.

<b>New Goal:</b> Find $s$ that maximizes $Q$

By setting $s = \sum_{i} a_{i}u_{i}$ with $a_{i} = u_{i}^{T}s$ we can re-write the modularity:

$$
Q = \frac{1}{4m}\sum_{i=1}^{n} \lambda_{i}(u_{i}^{T} \cdot s)^{2}
$$

where $λ_{i}$ is the eigenvalue of $B$ corresponding to eigenvector $u_{i}$.

Once this is done, we can optimize by:
- Pick $s$ that is parallel to $u_{1}$!
- Maximize $u_{1}\cdot s$, i.e., the projection of $s$ along vector $u_{1}$

<b>Spectral modularity optimization algorithm</b>
1. Consider the eigenvector u_{1} of B corresponding to the largest eigenvalue
2. Assign the nodes of the graph in one of the two communities $X$ ($s_{i}  = +1$) and $Y$ ($s_{i}  = -1$) based on the signs of the corresponding components of the eigenvector.

<b>Working with more than two partitions</b>
1. Iteratively, divide the produced partitions into two parts
2. If at any step the split does not contribute to the modularity, leave the corresponding subgraph as is
3. End when the entire graph cannot be splitted into no further divisible subgraphs

<b>Complexity:<b> $\mathcal{O}(n^{2} log n)$ for sparse graphs

#### Faster Modularity Optimization?

The spectral modularity optimization method is slow and does not scale to large networks. We can perform greedy optimization of modularity to speed-up the process. A popular method for doing so is the Louvain method, a greedy modularity optimization method for community detection.

The algorithm performs multiple passes, each with two phases:
1. Modularity Optimization
2. Community Aggregation

<b>Louvain</b>
Start with a weighted network where all nodes are in their own communities (i.e., n communities)

<u>First phase (Modularity Optimization)</u>

1. For each node $v_{i}$
  – For all neighbors $v_{j}$ of $v_{i}$
      * Compute the modularity gain if $v_{i}$ is removed from its community and placed in the community of $v_{j}$!
  – Find the community with the maximum modularity gain
  – If the maximum gain is positive, remove $v_{i}$ from its community, and place it in that community
  - If no positive gain, keep the same communities

2.Repeat until no node changes its community

<u>Second phase (Community Aggregation):</u> Build a new network!
– Nodes are the communities
– Edges are the edges between nodes in the corresponding communities (weights are sum of the weights)
– Self-loops represent edges within the community

<b>In practice:<b>
- The algorithm creates hierarchies of communities
- Typically, less than $10$ passes are enough
- <u>Complexity:</u> $\mathcal{O}(n logn)$

<b>Extensions of Modularity:</b> Modularity has been extended in several directions
– Weighted graphs [Newman ‘04]
– Bipartite graphs [Guimera et al ‘07] !
– Directed graphs [Arenas et al. ‘07], [Leicht and Newman ‘08]!
– Overlapping community detection [Nicosia et al. ‘09]!
– Modifications in the configuration model – local definition of modularity [Muff et al. ‘05]!

<b>Resolution Limit of Modularity:</b>
The method of modularity optimization may not detect communities with relatively small size, which depends on the total number of edges in the graph

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
