---
title: 'Decision trees'
date: 2018-10-16
permalink: /posts/2018/11/decision-trees/
tags:
  - Machine Learning
---
# Decision Tree Induction

## How a Decision Tree Works

<b>Tree structure:</b>
- Root node
- Internal nodes
- Leaf or terminal

Non-terminal nodes contain attribute test conditions to separate records that have different characteristics.

<b>Classifying a test record</b> is straightforward once a decision tree has been constructed.
Apply the test condition to the record and follow the appropriate branch based on the outcome of the test.

## How to Build a Decision Tree

Optimal tree ? Finding the optimal tree is computationally infeasible because of the exponential size of the search space.

efficient algorithms have been developed to induce a reasonably accurate, albeit suboptimal

algorithms usually employ a greedy strategy that grows a decision tree by making a series of locally optimum decisions about which attribute to use for partitioning the data.

Hunt’s algorithm, which is the basis of many existing de- cision tree induction algorithms, including ID3, C4.5, and CART.

### Hunt’s Algorithm

<b>Step 1:</b> If all the records in $D_{t}$ belong to the same class $y_{t}$, then $t$ is a leaf node labeled as $y_{t}$.
<b>Step 2:</b> If $D_{t}$ contains records that belong to more than one class, an attribute test condition is selected to partition the records into smaller subsets.

Hunt’s algorithm will work if every combination of attribute values is present in the training data and each combination has a unique class label.

Ad- ditional conditions are needed to handle the following cases:
1. child nodes created in Step 2 to be empty: node is declared a leaf node with the same class label as the majority class of training records associated with its parent node.
2. f all the records associated with Dt have identical attribute values (except for the class label), then it is not possible to split these records any further. node is declared a leaf node with the same class label as the majority class of training records associated with this node.

<b>Design Issues of Decision Tree Induction</b>
1. How should the training records be split?
    * specifying the test condition for different attribute types as well as an objective measure for evaluating the goodness of each test condition.
2. How should the splitting procedure stop?
    * topping condition is needed to terminate the tree-growing process.
    * all the records belong to the same class or all the records have identical attribute values.

<b>Different kind of attributes:</b>

Binary attributes, nominal attributes, ordinal attributes, continuous attributes

## Measures for Selecting the Best Split

Measures developed for selecting the best split are often based on the degree of impurity of the child nodes. The smaller the degree of impurity, the more skewed the class distribution.

Examples of impurity measures include:

$$
\begin{align}
& Entropy(t) = - \sum_{i=0}^{c-1}p(i\mid t)log_{2}(p(i\mid t)) \\
& Gini(t) = 1 - \sum_{i=0}^{c-1}p(i\mid t)^{2}\\
& Classification error(t) = 1 - max_{i}p(i\mid t)
\end{align}
$$

![Plot impurity](https://yanndubs.github.io/img/blog/impurity.png)

To determine how well a test condition performs, we need to compare the degree of impurity of the parent node (before splitting) with the degree of impurity of the child nodes (after splitting). The larger their difference, the better the test condition. The gain, ∆, is a criterion that can be used to determine the goodness of a split:

$$
\Delta = I(parent) - \sum_{j=1}^{k} \frac{N(v_{j}})}{N}I(v_{j})
$$

I(·) is the impurity measure of a given node, N is the total number of records at the parent node, k is the number of attribute values, and N(vj) is the number of records associated with the child node, vj.

Since I(parent) is cte, it is equivalent to minimizing the weighted average impurity measures of the child nodes

Information gain: The gain when entropy is used

### Splitting of Binary Attributes

### Splitting of Nominal Attributes

### Splitting of Continuous Attributes

Brute-force method for finding v: consider every value of the attribute in the N records as a candidate split position.
For each candidate v:
  * Count the number of records with annual income less than or greater than v.
  * Compute the Gini index for each candidate and choose the one that gives the lowest value.

- Computationally expensive because it requires $\mathcal{O}(N)$ operations to compute the Gini index at each candidate split position. Since there are N candidates, the overall complexity of this task is $\mathcal{O}(N^{2})$.

To reduce the complexity:
- Training records are sorted based on their annual income, a computation that requires $\mathcal{O}(N log N)$ time.
- Candidate split positions are identified by taking the midpoints between two adjacent sorted values.

Update the class distribution
This procedure is less expensive because it requires a constant amount of time to update the class distribution at each candidate split position. It can be further optimized by considering only candidate split positions located between two adjacent records with different class labels.

### Gain Ratio

Impurity measures such as entropy and Gini index tend to favor attributes that have a large number of distinct values.

test condition that results in a large number of outcomes may not be desirable because the number of records associated with each partition is too small to enable us to make any reliable predictions.

Strategy n°1: restrict the test conditions to binary splits only

Strategy n°2: Another strategy is to modify the splitting criterion to take into account the number of outcomes produced by the attribute test condition.

$$
Gain ratio = \frac{\Delta_{info}}{Split Info}
$$

with $Split Info = - \sum_{i=1}^{k}P(v_{i})log_{2}P(v_{i})$

if an attribute produces a large number of splits, its split information will also be large, which in turn reduces its gain ratio.

## Algorithm

A skeleton decision tree induction algorithm.

```python
def TreeGrowth (E, F):

if stopping cond(E,F) = true:
  leaf = createNode()
  leaf.label = Classify(E)
  return leaf
else:
  root = createNode().
  root.test_cond = find_best_split(E, F)
  V = {v|v is a possible outcome of root.test_cond}
  for v in V:
    E_v ={e|root.testcond(e) == v and e in E}.
    child = TreeGrowth(E_v, F )
    add child as descendent of root
    label the edge (root → child) as v
return root
```

After building the decision tree, a tree-pruning step can be performed to reduce the size of the decision tree. Decision trees that are too large are susceptible to a phenomenon known as overfitting. Pruning helps by trim- ming the branches of the initial tree in a way that improves the generalization capability of the decision tree.

## Characteristics of Decision Tree Induction

1. Decision tree induction is a non-parametric approach for building classifi- cation models.
2. Finding an optimal decision tree is an NP-complete problem.
3. Techniques developed for constructing decision trees are computationally inexpensive, making it possible to quickly construct models even when the training set size is very large. Furthermore, once a decision tree has been built, classifying a test record is extremely fast, with a worst-case complexity of O(w), where w is the maximum depth of the tree.
4. Decision trees, especially smaller-sized trees, are relatively easy to inter- pret. The accuracies of the trees are also comparable to other classifica- tion techniques for many simple data sets.
5. Decision tree algorithms are quite robust to the presence of noise, espe- cially when methods for avoiding overfitting, as described in Section 4.4, are employed.
6. The presence of redundant attributes does not adversely affect the ac- curacy of decision trees.
7. data fragmentation problem: At the leaf nodes, the number of records may be too small to make a statistically significant decision about the class rep- resentation of the nodes.
8. A subtree can be replicated multiple times in a decision tree
9. The test conditions described so far in this chapter involve using only a single attribute at a time. As a consequence, the tree-growing procedure can be viewed as the process of partitioning the attribute space into disjoint regions until each region contains records of the same class. The border between two neighboring regions of different classes is known as a decision boundary.


oblique decision tree can be used to overcome this limitation because it allows test conditions that involve more than one attribute.

Constructive induction

------
