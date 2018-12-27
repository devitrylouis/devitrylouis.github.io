---
title: 'Graph theory'
date: 2018-08-14
permalink: /posts/2018/11/graph_theory/
tags:
  - Network science
  - Basics
---

Networks greatly impact the properties of a system in many forms. Graph theory - a branch of Mathematics - is fundamental to grasp and represent networks. From degrees to degree distributions, from paths to distances and learn to distinguish weighted, directed and bipartite networks.

<b>Goal:</b> Introduce a graph-theoretic formalism to map the networks wiring diagram.

## Networks and graphs

<b>TL; DR:</b> Network is a Catalog of nodes/vertices with the links/edges that describe the direct interactions between them.

<i>Note:</i> The number of nodes / edges are key informations about a graph.

<b>Direction in a graph:</b> Depending on wether edges have a direction, we will call directed / undirected.  It can be both.

<i>Terminology:</i>

|           | Graph          | Networks |
|-----------|----------------|----------|
| Type      | Representation | Real     |
| Elements  | Vertex         | Nodes    |
| Relations | Edge           | Links    |

<i>Remark:</i> Choice of representation must be done with care regarding the significance of nodes and links.

## Key metrics: Degree, Average Degree and Degree Distribution

### Undirected

<b>Degree:</b> number of links it has to other nodes

$$
L = \frac{1}{2}\sum_{i=1}^{N}k_{i}
$$

Note: We introduce the $\frac{1}{2}$ factor as each link is counted twice.

<b>Average Degree:</b>
$$
\langle k \rangle = \frac{1}{N}\sum_{i=1}^{N}k_{i}
$$

### Directed

<b>Incoming / outcoming:</b> In directed networks we distinguish between:
  - $k_{i}^{in}$ : Incoming degree (number of links that point to node $i$)

  - $k^{i}_{out}$ : Outgoing degree (number of links from node $i$)

  - $k^{i} = k_{i}^{in} + k^{i}_{out}$ : Node’s total degree

<b>Definition (Number of links):</b>
$$
L = \sum_{i=1}^{N} k_{i}^{in} = \sum_{i=1}^{N} k_{i}^{out}
$$

<b>Definition (Average degree):</b>
$$
\langle k^{in}  \rangle = \frac{1}{n} k_{i}^{in}
$$

<b>Definition (Degree Distribution):</b> probability that a randomly selected node in the network has degree $k$. For a network with N nodes:

$$p_{k} = N_{k}/N$$

<b>Note:</b> Central role in network theory following the discovery of scale-free networks

<b>Definition (Hub):</b> most connected node.

<i>Advice:</i> The degree distribution is often shown on a log-log plot

## Adjacency Matrix

<b>Adjacency matrix:</b>
$$
A_{ij} =
\begin{cases}
1 \text{ if } \exists \text{ link from j to i}\\
0 \text{ otherwise }\\
\end{cases}
$$

<b>Property:</b>

- Undirected networkd $\Rightarrow$ adjacency matrix symmetric.

- Undirected network
$$\langle k_{i} \rangle = \sum_{j=1}^{N} A_{ij} = \sum_{j=1}^{N} A_{ji}$$

- Directed networks:
    * $k_{i}^{in} = \sum_{j=1}^{N} A_{ji}$
    * $k_{i}^{out} = \sum_{j=1}^{N} A_{ij}$


<b>Definition:</b> $L_{max}$ is the maximum number of links.

## Real Networks are Sparse

<b>Definition (Network sparse):</b> if $L ‹‹ L_{max}$

<b>Storage:</b> Lighter in memory to store a sparse matrix with a list rather than the full adjacent matrix.

## Weighted Networks

<b>Definition:</b> A network is weighted if
$$
A_{ij} = w_{ij}
$$

<b>Metcalfe’s law:</b> $\text{Value}(N)\propto N^{2}$

It translates to network externality in economics.

<i>Issues with the law:</i>
- Most real networks are sparse. Hence the value of the network increases only linearly with N.
- As the links have weights, not all links are of equal value.

## Bipartite Networks

<b>Definition (bipartite graph)</b>: network whose nodes can be divided into two disjoint sets $U$ and $V$ such that each link connects a $U$-node to a $V$-node.

<i>Two projections for each bipartite network:</i>
1. Connects two U- nodes by a link if they are linked to the same V-node.
2. Connects the V-nodes by a link if they connect to the same U-node

## Paths and Distances

<b>Physical distance</b> plays a <b>key</b> role in determining the interactions between the <b>components of physical systems</b>.

<b>Definition (Path):</b> is a route that runs along the links of the network. A path’s length represents the number of links the path contains.

### Shortest Path and distance

The shortest path between nodes $i$ and $j$ is the path with the fewest number of links.

<b>Definition:</b> The shortest path is often called the distance $d_{ij}$.

<b>Notes:</b>
1. Multiple shortest paths of the same length $d$ between a pair of nodes.
2. The shortest path never contains loops or intersects itself.
2. <i>Undirected network:</i> $d_{ij} = d_{ji}$
3. <i>Directed network:</i> $\exists p_{ij} \nRightarrow \exists p_{ji}$

<b>Goal:</b> Find the shortest path.

### How to find the shortest path?

<b>Adjacency matrix</b> find the shortest path and their numbers for points $i$ and $j$.
  - $d_{ij} = 1$ if a direct link exists
  - $d_{ij} = 2$ if there is a path of length two. Then $A_{ik} A_{kj} = 1$ and the number of $d_{ij} = 2$ paths is
  $$N_{ij}^{2} = \sum_{k = 1}^{N} A_{ik}A_{kj} = A_{ij}^{2}$$


<b>Breadth first search (BFS)</b>
BFS starts from a node and labels its neighbors, then the neighbors’ neighbors, until it reaches the target node. The number of “ripples” needed to reach the target provides the distance.

```python
def bfs_paths(graph, start, goal):
    # Start at node i, that we label with “0”.
    queue = [(start, [start])]
    # Repeat until you find the target node $j$ or there are no more nodes in the queue.
    while queue:
        (vertex, path) = queue.pop(0)
        # Find the nodes directly linked to i.
        for next in graph[vertex] - set(path):
            # Find the labeled nodes adjacent to it
            if next == goal:
                yield path + [next]
            else:
                # Label them with n + 1 and put them in the queue.
                queue.append((next, path + [next]))
```

If $j$ does not have a label, then $d_{ij} = \infty$.

<i>Computational complexity</i> $\mathcal{0}(N + L)$ because each node needs to be entered and removed from the queue at most once, and each link has to be tested only once.

<b>Diameter d_{max}</b> The longest shortest path in a graph / distance between the two furthest nodes.

<b>Compute the diameter:</b>

1. Choose a node to start
2. Compute all the outgoing distances from that point (but the first one if the network is undirected)
3. Repeat with another node for all nodes

# Some definitions

<b>Average Path Length:</b> $\langle d \rangle = \frac{1}{N^{2}}\sum_{j=1}^{N}\sum_{i=1}^{N} d_{i, j}$

<b>Cycle:</b> A path with the same start and end node. In the graph shown on the left we have only one cycle, as shown by the orange line.

<b>Eulerian Path:</b> A path that traverses each link exactly once.

<b>Hamiltonian Path:</b> A path that visits each node exactly once. We show two Hamiltonian paths in orange and in blue.

## Connectedness

<b>Goal:</b> Quantify how well are nodes connected to each other (with paths).

<b>Undirected network:</b>
$$
\text{i and j are }
\begin{cases}
\text{connected if }d_{ij}<\infty\\
\text{disconnected if }d_{ij}=\infty
\end{cases}
$$

<b>Definition: (Clusters C):</b> are subnetworks so that

$$
\forall i \in C, \forall j \notin C: d_{ij} = \infty
$$

<b>How to find clusters?</b>
- Small / Moderate graphs $\rightarrow$ Linear Agebra:
    * Rearange the adjacency matrix so as to have a block diagonal form.
    * The blocks are the clusters.


- Large networks $\rightarrow$ BFS algorithm:
  * <b>Step 1:</b> Choose node $i$ randomly and perform a BFS. Label all nodes reached this way with $n=1$.
  * <b>Step 2:</b> If all nodes are labeled $\Rightarrow$ network connected.
  * <b>Step 3:</b> The network consists of several components.
    * Label $n → n + 1$.
    * Choose an unmarked node $j$, label it with $n$.
    * Use BFS on unmarked node $j$ and label them all with $n$.
    * Return to <b>Step 2</b>.

## Clustering Coefficient

<b>TL;DR:</b> The clustering coefficient captures the degree to which the neighbors of a given node link to each other.

<b>Definition (Local clustering coefficient):</b> For a node $i$ with degree $k_{i}$:
$$
C_{i} = \frac{1L_{i}}{k_{i}(k_{i}-1)}
$$

where $L_{i}$ is the number of links between the neighbors of $i$.

<b>Definition (average clustering coefficient):</b> $\langle C \rangle = \frac{1}{N}C_{i}$

<b>Probabilistic interpretation</b> $\langle C \rangle$ is the probability that two neighbors of a randomly selected node link to each other.

<i>Notes:</i>Clustering coefficient can be generalized to directed and weighted networks as well.

------
