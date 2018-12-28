---
title: 'Multi-Layer Perceptron'
date: 2018-12-01
permalink: /posts/2018/11/mlp/
tags:
  - Deep Learning
  - Basics
---

This post covers the history of Deep Learning, from the Perceptron to the Multi-Layer Perceptron Network.

## Perceptron

<b>Key idea (1958, Frank Rosenblatt)</b>
1. Data are represented as vectors
2. <i>Collect training data:</i> some are positive examples, some are negative examples
3. <i>Training:</i> find $a$ and $b$ so that
    * $a > x + b$ is positive for positive samples $x$
    * $a > x + b$ is negative for negative samples $x$
4. <i>Testing:</i> the perceptron can now classify new examples.

<i>Notes:</i>
- This is not always possible to satisfy for all the samples
- Intuitively, it is equivalent to finding a separating hyperplane

<b>Training the perceptron:</b> At the time, ad hoc algorithm:
1. Start from a random initialization
2. For each training sample $x$:
    * compare the value of $a > x + b$ and its expected sign
    * adapt a and b to get a better value for $a > x + b$

<i>Note:</i> The perceptron is roughly inspired from the neuron:

![Perceptron vs. Neuron](https://appliedgo.net/media/perceptron/neuron.png)

<b>Limitations:</b> 1969, Perceptrons book, Minsky and Papert
- A perceptron can only classify data points that are linearly separable:
- Fail easy case such as the x-or function

<i>Consequence:</i> It is seen by many as a justification to stop research on perceptrons and entails the "AI winter" of the 1970s.

## Multilayer Perceptron/Neural Network

<b>Key idea (1980 - Rumelhart, Hinton, Williams)</b> "Chain" several perceptron together at different depth, with the help of a "squashing" function.

![Multi Layer Perceptron](https://raw.githubusercontent.com/ledell/sldm4-h2o/master/mlp_network.png)

<b>Formalism:</b>
1. <u>Input layer:</u> $x$ is the same vector used for the perceptron.
2. <u>Hidden layer:</u> consists of perceptrons + squashing function
    * Perceptrons weight their input $Wx + b$, where $W \in \mathbb{R}^{perceptrons\times features}$
    * Squashing / activation function $h = g(Wx+b)$ "rescales" the input for the next layer.
3. <u>Output:</u> $y = W_{2}h+b_{2}$

<i>Note:</i> We can construct networks with arbitrary number of hidden layers, hence the usefullness of the activation function.

We can find $W, b, W_{2}$, and $b_{2}$ with the objective:

$$
\mathcal{L}(\mathcal{T}) = \sum_{x, d\in \mathcal{T}} \mid\mid y(x) - d \mid\mid^{2}
$$

where $\mathcal{T}$ is the training set (features $x$ and expected output $d$).

<i>Note:</i> A Multilayer Perceptron solves  non-linearly separable problems such as the x-or function with $g(a) = max(a, 0)$

<b>In practice:</b>
- Do NOT use a least-squares loss function for classification problems!
- There are no closed-form solution so we use gradient descent.


------
