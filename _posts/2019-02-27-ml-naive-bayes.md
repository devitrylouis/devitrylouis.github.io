---
title: 'Naive Bayes'
date: 2018-10-16
permalink: /posts/2019/02/ml-naive-bayes/
tags:
  - Machine Learning
---
Naïve Bayes is a [generative learning algorithm](/posts/2018/10/ml-lda/) for discrete valued input. In particular, it is known to work great on texts classification tasks like spam detection.

## 1. Model

We represent an email via a feature vector whose length is equal to the number of words in the dictionary. Specifically, if an email contains the $i$-th word of the dictionary, then we will set $x_{i} = 1$; otherwise, we let $x_{i} = 0$

<b>Naive Bayes assumption:</b> The $x_{i}$’s are conditionally independent given $y$.

Under this, we obtain:
$$ p(x\mid y) = \Pi_{i=1}^{n}p(x_{i}\mid y)
$$

Let us set the following parameters:
$$\begin{align}
\phi_{i\mid y=1} &= p(x_{i}=1\mid y = 1)\\
\phi_{i\mid y=0} &= p(x_{i}=1\mid y = 0)\\
\phi_{y} &= p(y = 1)
\end{align}
$$

<b>Joint-likelihood:</b>

$$
\mathcal{L}(\phi_{y}, \phi_{i\mid y=0}, \phi_{i\mid y=1}) = \Pi_{i=1}^{n}p(x^{(i)}\mid y^{(i)})
$$

Maximizing with respect to our $2n+1$ parameters $\phi_{i\mid y=1}, \phi_{i\mid y=0}, \phi_{y}$ lead to:

$$
\begin{align}
\phi_{i\mid y=1} &= \frac{\sum_{i=1}^{m}1\{  x_{j}^{(i)} = 1 \wedge y^{(i)} = 1 \}}{\sum_{i=1}^{m}1\{ y^{(i)} = 1\}} \\
\phi_{i\mid y=1} &= \frac{\sum_{i=1}^{m}1\{  x_{j}^{(i)} = 1 \wedge y^{(i)} = 0 \}}{\sum_{i=1}^{m}1\{ y^{(i)} = 0\}}\\
\phi_{y} &= \frac{\sum_{i=1}^{m}1\{ y^{(i)} = 1 \} }{m}
\end{align}
$$

In Python, this leads to:
```python
def get_class_priors(y_train):
    # Count classes
    unique_labels, counts = np.unique(y_train, return_counts=True)
    # Class priors
    classes_prior = {}
    for i, label in enumerate(unique_labels):
        classes_prior[int(label)] = float(counts[i])/len(y_train)
    return classes_prior
```

To make a prediction on a new example with features $x$

$$
\begin{align}
p(y=1\mid x) &= \frac{p(x\mid y=1)p(y=1)}{p(x)}\\
&= \frac{\Pi_{i=1}^{m}p(x_{i}\mid y=1)p(y=1)}{\Pi_{i=1}^{ù}p(x_{i}\mid y=1)p(y=1) + \Pi_{i=1}^{m}p(x_{i}\mid y=0)p(y=0)} \\
\end{align}
$$

<b>Multi class: </b>Model $p(x_{i}|y)$ as multinomial rather than as Bernoulli.

<b>Simple hack:</b> Discretize values to use this algorithm.

## 2. Laplace smoothing

<b>TL; DR:</b> Naive Bayes algorithm works well for many problems, but there is a simple change that makes it work much better, especially for text classification.

<b>Problem: </b>The first time Naïve Bayes see a word, it thinks the probability of seeing it in either type class.

$$
\phi_{j} = \frac{\sum_{i=1}^{m}1\{ z^{(i)} = j \}}{m} = 0
$$

Furthermore it is statistically a bad idea to estimate the probability of some event to be zero just because you haven’t seen it before in your finite training set.

<b>Laplace smoothing:</b> Change the Maximum likelihood estimate:

$$
\phi_{j} = \frac{\sum_{i=1}^{m}1\{ z^{(i)} = j \}+1}{m+k}
$$

where $k$ is the number of classes.

<i>Notes:</i>
- Under certain (arguably quite strong) conditions, it can be shown that the Laplace smoothing actually gives the optimal estimator of the $\phi_{j}$’s. (What conditions?)
- Naïve Bayes with Laplace smoothing:
$$
\begin{align}
\phi_{i\mid y=1} &= \frac{\sum_{i=1}^{m}1\{  x_{j}^{(i)} = 1 \wedge y^{(i)} = 1 \}+1}{\sum_{i=1}^{m}1\{ y^{(i)} = 1\}+2} \\
\phi_{i\mid y=1} &= \frac{\sum_{i=1}^{m}1\{  x_{j}^{(i)} = 1 \wedge y^{(i)} = 0 \}+1}{\sum_{i=1}^{m}1\{ y^{(i)} = 0\}+2}\\
\phi_{y} &= \frac{\sum_{i=1}^{m}1\{ y^{(i)} = 1 \} +1}{m+2}
\end{align}
$$

------
