---
title: 'Optimizing Deep Learning'
date: 2018-12-01
permalink: /posts/2018/11/optimize-dl/
tags:
  - Deep Learning
---

First-order methods: gradient descent and variants.

# Local Minima

## Neural networks are not convex

In the setting of convex optimization,the problem can be reduced to finding a local minimum. Furthermore, we know that we have reached a good solution if we ﬁnd a critical point of any kind.

However nearly all Neural Networks are not convex, and are guaranteed to have an extremely large number of local minima. This is not that problematic because of the following reasonning.

## Model identiﬁability

<b>Definition</b> model has a suﬃciently large training set that can rule out all but one setting of the model’s parameters.

<i>Note</i> models with latent variables are often not identiﬁable because we can obtain equivalent models by exchanging latent variables with each other.

<b>Sources of non-identiﬁability:</b>
- <u>Weight space symmetry:</u> If we have $m$ layers with $n$ units each, then there are $n!^{m}$ ways of arranging the hidde $n$ units.
- <u>Scaling weights:</u> Rectiﬁed linear or maxout network, we can scale all the incoming weights and biases of a unit by $\alpha$ if we also scale all its outgoing weights by $1/\alpha$. This means that—if the cost function does not include terms such as weight decay that depend directly on the weights rather than the models' outputs — every local minimum of a rectiﬁed linear or maxout network lies on an $(m\times n)$-dimensional hyperbola of equivalent local minima.

<b>Consequence:</b> neural network cost function can have an extremely large or even uncountably inﬁnite amount of local minima. However, all these local minima arising from non-identiﬁability are equivalent to each other in cost function value.

<i>Note:</i> Local minima with high costs are nonetheless problematic for gradient-based optimization algorithms.

<i>Open questions:</i>
- Neural Network have many local minima of high cost?
- Do optimization algorithms encounter?

Today, experts suspect that, for suﬃciently large neural networks, most local minima have a low cost function value, and that it is not important to ﬁnd a true global minimum rather than to ﬁnd a point in parameter space that has low but not minimal cost.

## Flat Regions in random high-dimensional functions

<b>Saddle Points:</b> In high dimensional, non-convex situations, saddle points are more likely than local minima as some Hessian's eigenvalues are positive and some are negative.

For $\theta^{*}$ to be a local minimum, we need:
- $\mid\mid \frac{\partial J}{\partial \theta} (\theta^{*}) \mid\mid = 0$
- All eigenvalues of $\frac{\partial^{2}J}{\partial \theta^{2}}(\theta^{*})$ are positive.

<b>Consequences:</b>
1. For random functions in $n$ dimensions, the probability for all the eigenvalues to be all negative is $1 / n$. Many classes of random functions exhibit the following behavior: in low-dimensional spaces, local minima are common. In higher-dimensional spaces, local minima are rare, and saddle points are more common, as shown in [here](https://arxiv.org/pdf/1406.2572.pdf). More precisely, the expected ratio of the number of saddle points to local minima grows exponentially with $n$.
2. An amazing property of many random functions is that the eigenvalues of the Hessian become more likely to be positive as we reach regions of lower cost.
3. It also means that local minima are much more likely to have low cost than high cost. Critical points with high cost are far more likely to be saddle points. Critical points with extremely high cost are more likely to be local maxima.

## Flat Regions in neural networks

This happens for many classes of random functions. Does it happen for neural networks?
- Baldi and Hornik (1989) showed theoretically that shallow [autoencoders](https://devitrylouis.github.io/posts/2018/11/autoencoder/) with no nonlinearities have global minima and saddle points but no local minima with higher cost than the global minimum. These results extend to deeper networks without non-linearities (empirically). The output of such networks is a linear function of their input, but they are usefulto study as a model of nonlinear neural networks because their loss function isa non-convex function of their parameters. Such networks are essentially just multiple matrices composed together. Saxe et al. (2013) provided exact solutions to the complete learning dynamics in such networks and showed that learning in these models captures many of the qualitative features observed in the training ofdeep models with nonlinear activation functions. Dauphin et al. (2014) showed experimentally that real neural networks also have loss functions that contain very many high-cost saddle points.

Choromanska et al. (2014) provided additional theoretical arguments, showing that another class of high-dimensional randomfunctions related to neural networks does so as well.What are the implications of the proliferation of saddle points for trainingalgorithms? For ﬁrst-order optimization, algorithms that use only gradient infor-mation, the situation is unclear. The gradient can often become very small near asaddle point. On the other hand, gradient descent empirically seems able to escapesaddle points in many cases. Goodfellow et al. (2015) provided visualizations ofseveral learning trajectories of state-of-the-art neural networks, with an examplegiven in ﬁgure 8.2. These visualizations show a ﬂattening of the cost function neara prominent saddle point, where the weights are all zero, but they also show thegradient descent trajectory rapidly escaping this region. Goodfellow et al. (2015)283

For more informations on the Hessian, go [here](/posts/2018/11/basics-optimization/https://devitrylouis.github.io).

# Gradient descent

We use gradient descent to minimize the error with respect to the parameters $\theta$, namely $ \text{min}_{\theta} J(\theta)$ with the following iterates:

$$
\theta \leftarrow \theta - \lambda \frac{\partial J}{\partial \theta}
$$

where $\lambda$ is the learning rate:

![Different learning rates](https://imaddabbura.github.io/img/gradient_descent_algorithms/learning_rate.PNG)

## Back propagation

Backpropagation is shorthand for "the backward propagation of errors," since an error is computed at the output and distributed backwards throughout the network’s layers.[2] It is commonly used to train deep neural networks.

Backpropagation is a generalization of the delta rule to multi-layered feedforward networks, made possible by using the chain rule to iteratively compute gradients for each layer.

## Stochastic Gradient Descent

## Momentum

## Adagrad

## RMSProp

## Adam

# Practical DL

Ill-conditioning of the Hessian Matrix is a major problem met when optimizing convex functions (believed to be present in neural network training problems)

### Math

Recall from equation 4.9 that a second-order Taylor series expansion of the cost function predicts that a gradient descent step of $−\epsilon g$ will add

$$
\frac{1}{2} \epsilon^{2}g^{T}Hg - \epsilon g^{T}g
$$

to the cost. Ill-conditioning of the gradient becomes a problem when $\frac{1}{2} \epsilon^{2}g^{T}Hg$ exceeds $\epsilon g^{T}g$.

### Implications
- The result is that learning becomes very slow despite the presence of a strong gradient because the learning rate must be shrunk to compensate for even stronger curvature.
- Cause SGD to get “stuck” (even very small steps increase the cost function)

### How to solve it?
- One can monitor the squared gradient norm $g^{T}g$ and the $g^{T}Hg$ term.
    - The gradient norm does not shrink signiﬁcantly throughout learning, but the $g^{T}Hg$ term grows by more than an order of magnitude.



### Note for deep learning

Some of the techniques used to combat it in other contexts are less applicable to neural networks (Newton’s method is good for requires signiﬁcant modiﬁcations before it can be applied to neural networks).

<b>Test to rule out local minima:</b>
- Plotting the norm of the gradient over time.
    * Norm of the gradient does not shrink to insigniﬁcant size => the problem is neither local minima nor any other kind of critical point.
    * In high-dimensional spaces, positively establishing that local minima are the problem can be very diﬃcult. Many structures other than local minima also have small gradients!


------
