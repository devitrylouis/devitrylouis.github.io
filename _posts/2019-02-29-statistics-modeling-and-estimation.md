---
title: 'Statistics basics'
date: 2018-12-01
permalink: /posts/2019/01/modeling-and-estimation/
tags:
  - Statistics
---

## 1. Statistical modelling

<b>TL; DR:</b>
1. <u>Identifiability</u> = Injectivity of $\theta \mapsto P(\theta)$ + statistic = measure
2. <u>Sufficiency</u> $\Rightarrow L(x; \theta) = \psi(S(x); \theta) \lambda(x)$
3. Exponential family
    * <u>Complete statistics</u> = exist only one unique unbiased estimator of $\theta$ based on $T$. (close to the Lehmann–Scheffé theorem)
    * <u>Exponential family</u> = nice framework because canonical statistic is sufficient and complete + some sort of bijectivity of $Q$

### 1.1. Generalities

In statistics, <u>identifiability</u> is a property which a model must satisfy in order for <b>precise inference to be possible</b>. It basically means that it is <b>theoretically possible to learn the true values of this model's underlying parameters after obtaining an infinite number of observations from it</b>. Mathematically, it translates to:

<b>Definition (Identifiability conditions):</b> A model $(X, A , \{P_{\theta} : \theta \in \Theta \})$ is said identifiable if the mapping from $\Theta$ onto the probabilities space $(H, A)$, which to $\theta$ gives $P_{\theta}$ is injective.

This is equivalent to saying that different values of the parameters must generate different probability distributions of the observable variables.

<b>Definition (Statistic)</b> In a statistical model $(X, A , \{P_{\theta} : \theta \in \Theta \})$, a statistic is any measurable or $\sigma$-finite mapping $S$ from $(X, A)$ onto an arbitrary space. Let’s say a statistic is a function of r.V. $S(x_{1},...,x_{n})$.

### 1.2. Sufficiency

<b>TL;DR:</b> Where is contain the information of interest (i.e. related to the unknowns) in the data?

<b>Definition (Sufficient statistic)</b> A statistic $S$ is said to be sufficient iff the conditional distribution $L_{\theta}(X|S(X))$ does not depend on $\theta$.

> “…no other statistic that can be calculated from the same sample provides any additional information as to the value of the parameter.”

<b>Remark (Pros and cons)</b>
- Difficulty to use the definition
- Dimension of $S$ has to be minimal!

<b>Theorem (Factorisation Criterion (FC))</b> A statistic $S$ is sufficient iff the likelihood function can be written as:

$$ L(x; \theta) = \psi(S(x); \theta) \lambda(x) $$

### 1.3. Exponential family

<b>Definition (Complete statistics)</b> A statistic $S$ is said to be complete if for any measurable real-valued function $\phi$, one has:

$$
\{\forall \theta \in \Theta E_{\theta}[\phi \circ S(X)] = 0\} \Rightarrow \{\forall \theta \in \Theta \phi \circ S(X) = 0 a.s. [P_{\theta}]\}
$$

In essence, it ensures that the distributions corresponding to different values of the parameters are distinct.

<b>Definition (Exponential family)</b> A model is said to be exponential iff its LF can be written as:

$$
L(x; \theta) = h(x) \phi(\theta) exp\big[ \sum_{i=1}^{r}Q_{i}(\theta)S_{i}(x) \big]
$$

where $S(.) = (S_{1}(.), ..., S_{r}(.))$ is the canonical statistic.

<b>Proposition:</b> The canonical statistic is sufficient.

<b>Proposition:</b> For exponential family, if the $S_{i}(.)$ are linearly independent (affine sense), then $P_{\theta_{1}} = P_{\theta_{2}} \Leftrightarrow Q_{j}(\theta_{1}) = Q_{j}(\theta_{2})$

<b>Corollary:</b> For exponential family, if the $S_{i}(.)$ are linearly independent: $\theta$ is identifiable $\Leftrightarrow \theta \mapsto Q(\theta)$ is injective.

<b>Theorem:</b> If $Q(\Theta)$ contains a non-empty set of $\mathbb{R}^{r}$, the canonical statistic is complete.

<b>Proposition:</b> Of course, the canonical statistic follows an exponential model.

## 2. Unbiased estimation

<b>TL; DR:</b>
1. <b>Generalities:</b>
    * There are regularity conditions on $L(x: \theta) \in C^{2}\cap L^{2}$
    * Support of L independent of $\theta$
2. <b>Fisher information</b> = amount of info in the samples:
    * The <u>score function</u> $l'(x; theta)$ is the score and have zero mean. The FIM $I(\theta)$ is the variance of the score. Under the assumptions: $I(\theta) = - E_{\theta}[l''(x; \theta)]$
3. <b>Estimator</b> = a statistic $\delta(x)$ mapping $X$ into $g(\Theta)$ + MSE
    * $R_{δ}(\theta)=var_{\theta}(δ(x))+b_{δ}(\theta)^{2}$
    * The Rao–Blackwell theorem states that if $g(X)$ is any kind of estimator of a parameter $\theta$, then the conditional expectation of $g(X)$ given $T(X)$, where $T$ is a sufficient statistic, is typically a better estimator of $\theta$, and is never worse. At least as high as inverse of FIM
    * <b>Leman scheffé:</b> $T$ sufficient + complete, estimator unbiased => Efficient estimator (best variance of unbiased estimator)

### 2.1. Generalities

<b>Definition (Regular model)</b> If $\Theta$ is an open set and if (A1),(A2),(A3),(A4) are verified, the model is regular.

(A1) The model is dominated

(A2) The dist. domain $P_{\theta}: \Delta =\{x\in H|L(x;\theta)>0\}$ does not depend on $\theta \in \Theta$.

(A3) $L(x; \theta)$ is twice differentiable

(A4) $L'$ and $L''$ are integrable and we can permute integral and derivative.

### 2.2. Fisher Information

<b>Definition (Score)</b> The score function is the r.V. s_{\theta}(x) defined by:

$$
s_{\theta}(x) = \frac{\partial}{\partial \theta} l(x; \theta)
$$

where $l(x; \theta) = log(L(x; \theta))$

<b>Proposition:</b> The score is zero-mean, i.e. $E[s_{\theta}(x)]=0$.

<b>Definition (FIM)</b> If one has (A5) the score is square-integrable, the FIM is the variance (covariance matrix in multidimensional case) of the score:

$$
I(\theta) = var_{\theta}(s_{\theta}(x)) = E_{\theta}[s_{\theta}(x)s_{\theta}(x)^{T}]
$$

In case of a $n$-sample, $(x_{1},...,x_{n})$ we have $I_{n}(\theta) = nI(\theta)$

<b>Proposition FIM:</b> Let’s assume a regular model, plus (A5), then for a real $\theta$, one has:

$$I(\theta) = - E_{\theta}\big[ \frac{\partial^{2}}{\partial \theta \partial \theta ^{T}} l(x; \theta) \big]$$

<b>Intuition:</b> the Fisher information is a way of measuring the amount of information that an observable random variable $X$ carries about an unknown parameter $\theta$ of a distribution that models $X$.

### 2.3. Optimality

<b>Main idea:</b> give an answer $d$ regarding the data...

Define a loss function $Ω(d,\theta)$ between $d$ and the (true) value of the unknowns $\theta$ or $g(\theta)$. Generally,

<b>Definition (quadratic loss)</b>

$$\rho(d,\theta)=(d-g(\theta))A^{t}(\theta)(d-g(\theta))$$

where $A(.)$ is positive-definite

<b>Definition (Estimator):<b> An estimator of g(\theta) is a statistic \delta(x) mapping X into D = g(\Theta).

<b>Definition (Mean Square Error (MSE))</b>

$$
R_{\delta}(\theta) = E_{\theta}\big[ \rho(\theta, \delta(x)) \big] = E_{\theta}\big[ (g(\theta) - \delta(x))^{2} \big]
$$

### 2.4. Cramer Rao bound

<b>Goal:</b> minimize the MSE but...

<b>Proposition:</b> $$R_{\delta}(\theta) = var_{\theta}(\delta(x)) + b_{\delta}(\theta)^{2}$$

where $b_{\delta}(\theta)$ is the bias of $\delta(x)$ (i.e. $b_{\delta(x) - g(\theta)}$)

<b>Theorem (Rao-Blackwell estimator)</b> Let $\delta$ an estimator and $S$ a sufficient statistic. Let's define
$$
\delta_{s} : x \mapsto E_{\theta}[\delta(x) \mid S(\textbf{x}) = S(x)]
$$

Thus:

$$
\forall \theta \in \Theta, R_{\delta_{s}}(\theta) \leq R_{\delta}(\theta)
$$

$\delta_{S}$ is Rao-Blackwell estimator (or the Rao-Blackwellization of $\delta$). It is unbiased if $\delta$ is unbiased.

<b>Optimality: Lehman-Scheffé (LS) theorem</b>

If $\delta$ is unbiased and if $S$ is a sufficient and complete statistic, thus the Rao-Blackwell estimator $\delta_{S}$ is optimal in the class of unbiased estimators, i.e. its variance is minimal for all $\theta \in \Theta$

<b>Definition (Regular estimator)</b> Let a regular model, and let an estimator $\delta$ of $g(\theta)$ s.t.

$$
E_{\theta}[|\delta |^{2}] < \infty \forall \theta \in \Theta \ \text{ and } \frac{\partial}{\partial\theta}\int_{X}\delta(x)l(x; \theta) dx= \int_{X}\delta(x)\frac{\partial}{\partial\theta}l(x; \theta) dx
$$

Then $\delta$ is a regular estimator of $g(\theta)$

<b>Theorem (Cramer-Rao lower Bound (CRB) - FDCR inequality</b>
Let $\delta$ an unbiased regular eestimator of $g \in C^{1}(\mathbb{R}^{k})$ where $\theta \in \Theta \subset \mathbb{R}^{p}$. Let’s also assume that $I(\theta)$ is positive-definite. Thus, for a $n$-sample, and for all $\theta \in \Theta$ , one has:

$$
R_{\delta}(\theta) = var_{\theta}(\delta) \geq \frac{1}{n}\frac{\partial g}{\partial \theta^{t}}(\theta)I(\theta)^{-1} \frac{\partial g^{t}}{\partial \theta}(\theta)
$$

with $\frac{\partial g}{\partial \theta^{t}}(\theta)$ is the $p\times k$ matrix defined by: $(\frac{\partial g_{i}}{\partial \theta_{j}}(\theta))_{ij}$ and $\frac{\partial g^{t}}{\partial \theta}(\theta)$ its tranpose.

<i>Note:</i>In its simplest form, the bound states that the variance of any unbiased estimator is at least as high as the inverse of the Fisher information.

<b>Definition Efficiency:</b> An unbiased estimator is said to be efficient iff its variance is the CRB.

<b>Proposition:</b> If $T$ is an efficient estimator of $g(\theta)$, then the affine transform $AT +b$ is an efficient estimator of $Ag(\theta)+b$ (for $A$ and $b$ with appropriate dimensions)

<b>Proposition:</b> An efficient estimator is optimal. The converse is (obviously) wrong.

### 2.5. Link with Exponential family

<b>Definition (Exponential model under a natural form...)</b>

Consider an exponential model $L(x; \theta) = h(x)\phi(\theta)\text{exp}(\sum_{i=1}^{r}Q_{i}(\theta)S_{i}(x))$  and make the change of variable $\lambda_{j} = Q_{h}(\theta)$. Then one obtains:

$$ L(x; \theta) = K(\lambda)h(x)\text{exp}(\sum_{j=1}^{r}\lambda_{j}S_{j}(x)) $$

The new parameters $(\lambda_{1},··· ,\lambda_{r}) \in \Lambda = Q(\Theta)\subset \mathbb{R}^{r}$

<b>Theorem (Regularity)</b> Let an exponentiel model. If $\Lambda$ is a non-empty open set of $\mathbb{R}^{r}$, then the model is regular and (A5) is verified $\Rightarrow I(\lambda)$ exists. Furthermore

$$
I(\lambda) = - \mathbb{E}_{\lambda}\big[ \frac{\partial^{2}\text{log}(L(x;\lambda))}{\partial\lambda\partial \lambda^{t}} \big]
$$

<b>Theorem (Identifiability)</b> Let us consider the exponential model (2) where $\Delta$ is a (non-empty) open set of Rr. Then, the model is identifiable, i.e., $(P_{\lambda_{1}} =P_{\lambda_{2}} \Rightarrow \lambda_{1} =\lambda_{2})$ iff the FIM $I (\lambda)$ is invertible $\forall\lambda \in \Lambda$

<b>Theorem (Necessary condition)</b> Let's consider a regular exponential model and let $\delta$ an unbiased regular estimator $\delta$ of $g(\theta) \in C^{1}$. Moreover, let $I(\theta)$ be invertible $\forall \theta \in \Theta$. Thus, if $\delta$ is efficient, it is necessary an affine function of $S(x)=(S_{1}(x),···,S_{r}(x))t$.

<b>Theorem (Converse of CRB - equality)</b> Given a regular model $g: \emptyset \neq \Theta \subset \mathbb{R}^{d} \mapsto \mathbb{R}^{p}$ of class $C^{1}$ such that

- $\frac{\partial g}{\partial\theta^{t}(\theta)}$ is a square invertible matrix $\forall \theta \in \Theta$ so that $p = d$.

- $I(\theta)$ exists and is invertible $\forall \theta \in \Theta$.

Then $\delta(x)$ is a regular and efficient estimator of $g(\theta)$ if and only if $L(x;\theta)$ can be written as:

$$
L(x; \theta) = \text{C}(\theta) \text{h}(x) \text{exp}\big[ \sum_{j=1}^{d} Q_{j}(\theta) S_{j}(x) \big]
$$

where functions $Q$ and $C$ are s.t.
- $Q$ and $C$ are differentiable $\forall \theta \in \Theta$
- $\frac{\partial Q}{\partial\theta^{t}}(\theta)$ is invertible $\forall \theta \in \Theta$
- $g(\theta) = -\big( \frac{\partial Q}{\partial\theta^{t}}(\theta) \big)^{-1}\frac{\partial ln(C)}{\partial\theta^{t}}(\theta$)

<b>Corollary:</b> In an exponential model of the natural form where $\emptyset \neq \Delta \subset \mathbb{R}^{r}$ and where $I(\lambda)$ is invertible $\forall \lambda \in \Lambda$.
Thus, each statistic $S_{j}(x)$ is an efficient estimator of $E_{\lambda}[S_{j}(X)]$ which is defined as:

$$
g_{j}(\lambda) = - \frac{\partial ln(K)}{\partial \lambda_{j}}(\lambda)
$$

## 3. Theory of point estimation
### 3.1. Basics

<b>Definition (Consistancy)</b> An estimator $\hat{\theta}_{n}$ of $g(\theta)$ is strongly / weakly consistant if it $P_{\theta_{0}}$ - almost surely / in proba converges torwards $g(\theta_{0})$, with $g: \Theta \mapsto \mathbb{R}^{p}$

<b>Definition (Asymptotically unbiased)</b> An estimator $\hat{\theta}_{n}$ of $g(\theta)$ is asymptotically unbiased if its limiting distribution is zero-mean, i.e.,

$$
\exists c_{n} \rightarrow \infty s.t. c_{n}(\hat{\theta_{n}} - g_{\theta_{0}})
 \rightarrow^{dist} z ÷text{ with } E_{\theta_{0}}[z]=0$$

<i>Remark:</i> Different from "unbiased at the limit:" $E_{\theta_{0}}[\hat{\theta}_{n}]\rightarrow g(\theta_{0})$

Definition (Asymptotically normal)

Definition (Asymptotically efficient)

### 3.1. Method of moment

Theorem

Theorem (Asymptotics of the MM estimator)

### 3.1. Method of Maximum Likelihood

Definition (Maximum Likelihood Estimator (MLE))

Definition

Theorem:

Theorem (Classical asymptotics)
Theorem (Classical asymptotics)

CCL

Come back on exponential models + Theorem

### 3.1. Bayesian estimation

------
