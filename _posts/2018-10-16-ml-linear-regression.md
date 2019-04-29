---
title: 'Linear Regression'
date: 2018-10-16
permalink: /posts/2018/11/ml-linear-regression/
tags:
  - Machine Learning
---

In layman terms, a Linear Regression consists in predicting a continuous dependent variable $Y$ as a linear combination of the independent variables $X = \{x_{1}, ..., x_{n} \}$. The contribution of each variable $x_{i}$ is expressed by a parameter $\beta_{i}$. Altogether, it is a simple weighted sum:

$$
h(x) = \sum_{i=0}^{n} \beta_{i}x_{i} = \beta^{t} x
$$

where $\beta$ are the parameters, also called weights. It should be noted that in the above formula, the sum begins at $i = 0$ to incorporate the intercept (i.e. the constant term). As for the parameters, they are learned to minimize the quadratic loss function:

$$
\begin{align}
J(\beta) &= \frac{1}{2} \sum_{i=1}^{n} (y_{i} - \beta_{i} x_{i})^{2}\\
& = \frac{1}{2} (y-\beta^{T}x)^{T}(y-\beta^{T}x)\\
\end{align}
$$

The parameters we consider best are the one that minimizes this error.

## 1. Least Mean Squares

<b>TL; DR:</b> We use gradient descent:

$$
\beta_{j} := \beta_{j}-\alpha\frac{\delta}{\delta\beta_{j}}J(\beta)
$$

where $\alpha$ is called the learning rate. Simplifying leads to this:

$$
\beta_{j} := \beta_{j} + \alpha (y - h_{beta}(x)x_{j}
$$

<b>Least Mean Square update rule (single training example):</b>
$$
\beta_{j} := \beta_{j} + \alpha (y^{(i)} - h_{beta}(x^{(i)})x_{j}^{(i)}
$$

<b>Batch gradient descent:</b>

$$
\beta_{j} := \beta_{j} + \alpha \sum_{i=1}^{m} (y^{(i)} - h_{beta}(x^{(i)})x_{j}^{(i)}
$$

It does not scale well with the number of famles $m$.

<b>Stochastic Gradient Descent:</b>

Less costly than Batch Gradient Descent $\Rightarrow$ Faster to get near the minimum.

$$
\begin{align}
\text{For i in {1, ..., m}}&\\
\beta_{j} := \beta_{j} + \alpha  &(y^{(i)} - h_{beta}(x^{(i)})x_{j}^{(i)}
\end{align}
$$

<b>Results:</b>
- The magnitude of the update is proportional to the error term.
- J is a convex quadratic function $\Rightarrow$ gradient descent always converges.

## 2. Closed form solution - Normal equations

There is a way to solve this with Linear Algebra by reformulating the loss:

$$
J(\beta) = \frac{1}{2} (X\beta - y)^{t}(X\beta - y)
$$

where $X \in \mathbb{R}^{n\times m}$ is our $n$ samples with $m$ features.

By setting the derivative of $J(\beta)$ to $0$ and solving the problem with matrix derivatives, we obtain:

<b>Result / Definition (Ordinary Least Square estimate):</b>

$$
\theta = (X^{T}X)^{-1}X^{T}y
$$

## 3. Regularization

### 3.1. Least Absolute Shrinkage and Selection Operator (LASSO)

To enhance both the prediction accuracy model and the interpretabiliy of the produced model, LASSO alters the fitting process by selecting a subset of the provided covariates for use in the final model. To this effect, it shrinks the OLS coffcient toward zero (with some exactly set to zero).

<b>Definition (LASSO estimate):</b>
$$
\hat{\beta}_{lambda} = \text{argmin}_{\beta} J(\beta) + \lambda \sum_{j=1}^{p}\mid \beta_{j} \mid
$$

<b>Terminology ($\mathcal{l}_{1}$ penalty):</b> This is the righmost term of the above equation.

<b>Note:</b> One can proove that this is equivalent to:

$$
\hat{\beta}_{lambda} = \text{argmin}_{\beta} J(\beta) \text{ subject to } \sum_{j=1}^{m} \mid \beta_{j}\mid \leq s_{\lambda}
$$

where

$$
\begin{align*}
  s_{lambda} : \mathbb{R}_{+}^{*} &\to \mathbb{R}_{+}^{*}\\
  \lambda &\mapsto s_\lambda.
\end{align*}
$$

is a bijective application.

### 3.2. Ridge Regression

Ridge Regression is also a regularization technique, with however possess a different penalty term, that
prevents it to perform variable selection in most cases.

<b>Definition (Ridge Regression estimate):</b>
$$
\hat{\beta}_{lambda} = \text{argmin}_{\beta} J(\beta) + \lambda \sum_{j=1}^{p}\beta_{j}^{2}
$$

The difference with LASSO regularization resides in the penalty term, which is in this case a $l_{2}$-penalty.

Similarly to LASSO, there exists a bijective application $s_{\lambda}$  that states the equivalent form (optimization
problem):

$$
\hat{\beta}_{lambda} = \text{argmin}_{\beta} J(\beta) \text{ subject to } \sum_{j=1}^{m} \beta_{j}^{2} \leq s_{\lambda}
$$

### 3.3. Geometric intuition (p = 2)

The optimization problems defined for both the LASSO and the Ridge Regression shrinkages yield an geometric explanation of those two shrinkage methods:

![alt text](https://statweb.stanford.edu/~tibs/lasso.jpg)

where the blue areas are the constraint region and the red lines the contours of the RSS.

Both LASSO and Ridge Regression estimates are defined by the intersecion ot the RSS lines and the constraint region. It is why variable selection is induced by the LASSO as the sharp corners of the constraint area are more likely to intersect the RSS lines. When $p > 2$, the variable selection holds due to the constraint polytope sharp corners.

### 3.4. Extensions to Elastic Nets

The LASSO penalty is somewhat indifferent to the choice among a set of strong but correlated variables. The ridge penalty, on the other hand, tends to shrink the coefficients of correlated variables toward each other.

Elastic Net is a hybrid approach that blends both penalization of the $l_{1}$ and $l_{2}$ norms. Formally, it is a convex combination of both, as it minimizes the following:

$$
\mid\mid y-X\beta \mid\mid + \lambda(\alpha \mid\mid \beta \mid\mid_{1} + (1-\alpha)\mid\mid \beta \mid\mid_{2}^{2})
$$

where $\alpha \in [0, 1]$ is a hyper-parameter controlling how much of $l_{1}$ or $l_{2}$ penalization is used.

Comparing to LASSO and Ridge Regression, an instance of elastic net yields the following constraint region for p=2

![Elastic Nets](http://www.ds100.org/sp17/assets/notebooks/linear_regression/norm_balls.png)

<i>Note:</i> LASSO tends to select noisy predictors with a high probability, leading to an inconsistent variable selection.

## 4. Locally weighted Linear Regression

<b>TL; DR:</b> The idea is to weight every training sample sample error according to their distance to the point $x$ we wish to predict. Precisely:

$$ \sum_{i}w^{(i)}(y^{(i)}-\beta^{T}x^{(i)}) $$

<b>Weights choice (Gaussian kernel)</b>
$$
w^{(i)} = exp(-\frac{(x^{i}-x)^{2}}{2\tau^{2}})
$$

The space of functions $\mathcal{H}$ corresponding to the Gaussian kernel turn out to be very smooth. Therefore, a learned function (e.g, a regression function, principal components in RKHS as in kernel PCA) is very smooth. Usually smoothness assumption is sensible for most datasets we want to tackle.[More here](https://stats.stackexchange.com/questions/131138/what-makes-the-gaussian-kernel-so-magical-for-pca-and-also-in-general)

<b>Parameteric vs. Non-parametric</b>
Algorithms described above are <b>parametric</b> (have fixed, finite number of parameters), which are fit to the data. Once fitted, we no longer need to keep the training data to make future predictions.

For locally weighted linear regression, we need to keep the entire training set around. The term “non-parametric” (roughly) refers to the fact that the amount of stuff we need to keep in order to represent the hypothesis h grows linearly with the size of the training set.

## 5. Good practices

1. Make a significance test ($t$-test)
$$
H_{0}:\{\beta_{i}=0 \} \text{ vs } H_{1}:\{\beta_{i}=0\} \
$$
2. Multicollinearity diagnostic (compute $det(X^{T}X)$, Variance Inflation Factors)
3. Check for eventuals transformations of the response (BoxCox method, typically $x \mapsto log(x)$)
4. Make a thorough residual analysis
    * Residual plot of fitted values: [Externally studentized residuals](https://en.wikipedia.org/wiki/Studentized_residual#Internal_and_external_studentization)
    * Normal probability plot
5. Leverage and influential points analysis (plot hat values)

    * <b>Hat matrix diagonal:</b> is a standardized measure of the distance of the $i$-th observation from the centroïd of the $X$ space. Therefore, large hat values ($h \geq \frac{2m}{n}$) reveal observations that are potentially influential because they are remote in $X$ space from the rest of the sample.

    * <b>Cook’s distance:</b> of the $i$-th point is a measure of the squared distance between the least-squares estimate based on all points and the estimate obtained by deleting the i-th point.
      * $D_{i}$ combines residual magnitude for the $i$th observation and the location of that point in $X$ space to assess influence.
      * $D_{i} > \frac{4}{n-m-1}$ typically indicates influential points.

    * <b>CovRatio</b> measure provide informations about the precision of estimations, which is not conveyed by the previous quantities.

$$CovRatio > 1+\frac{3(m-1)}{n} \text{ or } CovRatio < 1-\frac{3(m-1)}{n}$$

https://math.stackexchange.com/questions/2624986/the-meaning-behind-xtx-1
https://www.quora.com/How-would-linear-regression-be-described-and-explained-in-laymans-terms

------
