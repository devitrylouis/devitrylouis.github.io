---
title: 'Multiple criteria decision'
date: 2018-12-01
permalink: /posts/2019/01/multiple-criteria/
tags:
  - Decision Modeling
---

Each possible states of the decision models relate to certain consequences
- Each alternative/action is characterized by the consequences (diverse in nature) of its eventual implementation,
- These consequences refer to the “points of view” according to which alternatives are compared,
- Some consequences permit direct comparison (existence of a “natural” unit),
- Necessity to encodage (when the direction of preference is not specified by the consequence, age of a candidate).

## Notion of criterion

A criterion is a real valued function $g$ defined on the set of alternative $A$ allowing to compare alternatives according to a “viewpoint” such that:

$$g(a) > g(b) \Rightarrow a \succeq_{g} b, \forall a, b \in A$$

where the relation $\succeq_{g}$ means “at least as good as”

### Monocriterion versus multicriteria approach

Many works in operational research and decision making are grounded on a mono-criterion approach:
- The decision model uses a <u>single criterion</u>
- <u>Other alternatives</u> are marginalized, thus making them seem <u>negligible</u> to the decision model
- Aggregate all aspects into a <u>single synthetic criterion</u>.

A multiple criteria approach consists in building a model which explicitly accounts for several criteria of the decision problem, each criterion representing a “homogenous class of consequences.

### Image of A in the criteria space

Multiple criteria preference modeling consists of building $n$ ($n ≥ 2$) criterion functions ($g_{1}, g_{2}, . . . , g_{n}$), $F = {1, 2, . . . , n}$
Each criterion expresses DM preferences wrt “significance
axis”,
An alternative a ∈ A is represented by an evaluation vector $(g_{1}(a), g_{2}(a), . . . , g_{n}(a))$,
The image of $A$ in the criteria space corresponds to the set of evaluation vectors corresponding to an alternative $a \in A$,

------
