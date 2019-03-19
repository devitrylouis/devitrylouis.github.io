---
title: 'Statistics basics'
date: 2018-12-01
permalink: /posts/2019/01/modeling-and-estimation/
tags:
  - Statistics
---

## 1. Statistical modelling

<b>TL; DR:</b> We deal with <u>identifiable models</u> (i.e. different parameters lead to different distributions) with statistics (measure). In particular, we are interested in <u>sufficient statistics</u>, those that explain well the data. They verify have the advantage to statisfy the factorization theorem:

$$L(x; \theta) = \psi(S(x); \theta) \lambda(x)$$

Another important characteristic is <u>completeness</u>: whether there is a unique unbiased estimator of $\theta$ based on the statistic (close to the Lehmann–Scheffé theorem)

Then we define exponential family which constitutes a nice framework as its canonical statistic is sufficient and complete, among others.

### 1.1. Generalities

In statistics, <u>identifiability</u> is a property which a model must satisfy in order for <b>precise inference to be possible</b>. It basically means that it is <b>theoretically possible to learn the true values of this model's underlying parameters after obtaining an infinite number of observations from it</b>. Mathematically, it translates to:

<b>Definition (Identifiability conditions):</b> A model $(X, A , \{P_{\theta} : \theta \in \Theta \})$ is said identifiable if the mapping from $\Theta$ onto the probabilities space $(X, A)$, which to $\theta$ gives $P_{\theta}$ is injective.

This is equivalent to saying that different values of the parameters must generate different probability distributions of the observable variables.

<b>Definition (Statistic)</b> In a statistical model $(X, A , \{P_{\theta} : \theta \in \Theta \})$, a statistic is any measurable or $\sigma$-finite mapping $S$ from $(X, A)$ onto an arbitrary space. Let’s say a statistic is a function of r.V. $S(x_{1},...,x_{n})$.

### 1.2. Sufficiency

> “…no other statistic that can be calculated from the same sample provides any additional information as to the value of the parameter.”

The formal definition of a <u>sufficient statistic</u> is a bit hard to grasp and can be difficult to use in practice:

$$L_{\theta}(X\mid S(X)) \text{ independent of } \theta$$

where $L_{\theta}(X\mid S(X))$ is the conditional distribution of $X$ knowing $S(X)$. In consequence, one commonly refer to the <b>Factorisation Criterion</b>, which states that the statistic is sufficient it its likelihood functions is of the form:

$$ L(x; \theta) = \psi(S(x); \theta) \lambda(x) $$

<i>Note:</i> One could choose $S(X) = S$ of course, but the point is to find $S$ of minimal dimension.

### 1.3. Exponential family

A statistic $S$ is said to be <u>complete</u> if for any measurable real-valued function $\phi$, one has:

$$
\{\forall \theta \in \Theta: \ E_{\theta}[\phi \circ S(X)] = 0\} \Rightarrow \{\forall \theta \in \Theta: \ \phi \circ S(X) = 0 \text{ a.s.} [P_{\theta}]\}
$$

In essence, it ensures that the distributions corresponding to different values of the parameters are distinct. But once again, its hard to use in practice. Therefore, we will define family of models that is large enough to have expressive power and simple enough for theoretical manipulations. This family is the <b>Exponential family</b> and the condition for a model to belong to this family is that one can re-write its likelihood function as:

$$
L(x; \theta) = h(x) \phi(\theta) \text{exp}\Bigg[ \sum_{i=1}^{r}Q_{i}(\theta)S_{i}(x) \Bigg]
$$

where $S(.) = (S_{1}(.), ..., S_{r}(.))$ is the canonical statistic. The big advantage is that the canonical statistic is always sufficient and it is furthermore complete if $Q(\Theta)\neq\emptyset$.

For a given exponential model with $S_{i}$ are linearly independent in the affine sense, then:

$$P_{\theta_{1}} = P_{\theta_{2}} \Leftrightarrow Q_{j}(\theta_{1}) = Q_{j}(\theta_{2})$$

This is quite powerful because it means that there is some sort of basis and that for two distributions to be equal, each of the component of the basis must be equal. The corollary is that under these conditions:

$$ \text{Identifiability } \Leftrightarrow Q \text{ injective} $$

## 2. Unbiased estimation

In this section, we define regularity conditions ($C^{2}\cap L^{2}$ and support independent of $\theta$) on the likelihood function, and use them to build the Fisher Information Matrix (FIM), which measure of the amount of informations in the samples. This will be our basis to build bounds on the variance of an unbiased estimator (CRB) and optimal estimators for the parameters (Lemman-Scheffé). In particular, we will show that if $g(X)$ is any kind of estimator of a parameter $\theta$, then the conditional expectation of $g(X)$ given $T(X)$, where $T$ is a sufficient statistic, is typically a better estimator of $\theta$, and is never worse.

### 2.1. Generalities

<b>Definition (Regular model)</b> If $\Theta$ is an open set and if (A1),(A2),(A3),(A4) are verified, the model is regular.

> <i>(A1)</i> The model is dominated<br>
> <i>(A2)</i> The dist. domain $P_{\theta}: \Delta =\{x\in H\mid L(x;\theta)>0\}$ does not depend on $\theta \in \Theta$.<br>
> <i>(A3)</i> $L(x; \theta)$ is twice differentiable<br>
> <i>(A4)</i> $L'$ and $L''$ are integrable and we can permute integral and derivative.

### 2.2. Fisher Information

<b>Definition (Score)</b> The score function is the r.V. $s_{\theta}(x)$ defined by:

$$
s_{\theta}(x) = \frac{\partial}{\partial \theta} l(x; \theta)
$$

where $l(x; \theta) = \text{log}(L(x; \theta))$. The score is zero-mean (i.e. $E[s_{\theta}(x)]=0$) and if one has:

> <i>(A5)</i> the score is square-integrable

we can define the <u>FIM</u> as the variance (covariance matrix in multidimensional case) of the score:

$$
I(\theta) = var_{\theta}(s_{\theta}(x)) = E_{\theta}[s_{\theta}(x)s_{\theta}(x)^{T}]
$$

In case of a $n$-sample, $(x_{1},...,x_{n})$ we have $I_{n}(\theta) = n\cdot I(\theta)$

<b>Proposition (FIM):</b> Let’s assume a regular model, plus (A5), then for a real $\theta$, one has:

$$I(\theta) = - E_{\theta}\big[ \frac{\partial^{2}}{\partial \theta \partial \theta ^{T}} l(x; \theta) \big]$$

The intuition behind the Fisher information is a way of measuring the amount of information that an observable random variable $X$ carries about an unknown parameter $\theta$ of a distribution that models $X$.

### 2.3. Optimality

<b>Main idea:</b> give an answer $d$ regarding the data by using a loss function $\rho(d,\theta)$ between $d$ and the (true) value of the unknowns $\theta$ or $g(\theta)$.

<b>Definition (quadratic loss):</b>

$$\rho(d,\theta)=(d-g(\theta))A^{t}(\theta)(d-g(\theta))$$

where $A(.)$ is positive-definite

<b>Definition (Estimator):</b> An estimator of $g(\theta)$ is a statistic $\delta(x)$ mapping $X$ into $D = g(\Theta)$.

<b>Definition (Mean Square Error (MSE))</b>

$$
R_{\delta}(\theta) = E_{\theta}\big[ \rho(\theta, \delta(x)) \big] = E_{\theta}\big[ (g(\theta) - \delta(x))^{2} \big]
$$

### 2.4. Cramer Rao bound

The <b>goal</b> is to minimize the MSE but reformulate it with the [bias-variance dilemma](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)

$$R_{\delta}(\theta) = var_{\theta}(\delta(x)) + b_{\delta}(\theta)^{2}$$

where $b_{\delta}(\theta)$ is the bias of $\delta(\textbf{x})$ (i.e. $b_{\delta}(\theta) = E_{\theta}[\delta(\textbf{x}) - g(\theta)]$).

In this subsection, we will give the following results:
1. <u>Rao-Blackwell estimator:</u> An estimator with a sufficient statistic is always better than the same without (w.r.t. MSE).
2. <u>Lehman-Scheffé:</u> If the statistic is additionally complete, it is the best of all unbiased estimators in terms of variance.
3. <u>Cramer-Rao lower Bound</u> For a unbiased and regular estimator $\delta$ of $g \in C^{1}$, its variance is lower-bounded.

<b>Theorem (Rao-Blackwell estimator)</b> Let $\delta$ an estimator and $S$ a sufficient statistic. Let's define an estimator with the knowledge of this statistic $\delta_{s} : x \mapsto E_{\theta}[\delta(\textbf{x}) \mid S(\textbf{x}) = S(x)]$. Then:

$$
\boxed{\forall \theta \in \Theta, R_{\delta_{s}}(\theta) \leq R_{\delta}(\theta)}
$$

$\delta_{s}$ is Rao-Blackwell estimator (or the Rao-Blackwellization of $\delta$). As it turns out, it is unbiased if $\delta$ is unbiased.

<b>Theorem: (Lehman-Scheffé optimality)</b> If $\delta$ is unbiased and if $S$ is a sufficient and complete statistic, then the Rao-Blackwell estimator $\delta_{S}$ is optimal in the class of unbiased estimators, i.e. its variance is minimal for all $\theta \in \Theta$.

<b>Definition (Regular estimator)</b> $\delta$ is a regular estimator of the regular model $g(\theta)$ if:

1. $E_{\theta}[|\delta |^{2}] < \infty\ \forall \theta \in \Theta$

2. $\frac{\partial}{\partial\theta}\int_{X}\delta(x)l(x; \theta) dx= \int_{X}\delta(x)\frac{\partial}{\partial\theta}l(x; \theta) dx$

<b>Theorem (Cramer-Rao lower Bound)</b>
Let $\delta$ an unbiased regular estimator of $g \in C^{1}(\mathbb{R}^{k})$ where $\theta \in \Theta \subset \mathbb{R}^{p}$. Let’s also assume that $I(\theta)$ be positive-definite. Then, for $n$-samples, and for all $\theta \in \Theta$, one has:

$$
\boxed{R_{\delta}(\theta) = var_{\theta}(\delta) \geq \frac{1}{n}\frac{\partial g}{\partial \theta^{t}}(\theta)I(\theta)^{-1} \frac{\partial g^{t}}{\partial \theta}(\theta)}
$$

where $\frac{\partial g}{\partial \theta^{t}}(\theta)$ is the $p\times k$ matrix defined by: $(\frac{\partial g_{i}}{\partial \theta_{j}}(\theta))_{ij}$ and $\frac{\partial g^{t}}{\partial \theta}(\theta)$ its tranpose.

<i>Note:</i> In its simplest form, the bound states that the variance of any unbiased estimator is at least as high as the inverse of the Fisher information.

<b>Definition (Efficiency):</b> An unbiased estimator is said to be efficient if and only if its variance is the CRB.

<b>Proposition:</b> If $T$ is an efficient estimator of $g(\theta)$, then the affine transform $AT +b$ is an efficient estimator of $Ag(\theta)+b$ (for $A$ and $b$ with appropriate dimensions)

<b>Proposition:</b> An efficient estimator is optimal. The converse is (obviously) wrong.

### 2.5. Link with Exponential family

The exponential model can be re-written in its natural form by making the change of variable $\lambda_{j} = Q_{h}(\theta)$:

$$ L(x; \theta) = \text{K}(\lambda)\text{h}(x)\text{exp}\Big(\sum_{j=1}^{r}\lambda_{j}S_{j}(x)\Big) $$

where the new parameters are given by $(\lambda_{1},··· ,\lambda_{r}) \in \Lambda = Q(\Theta)\subset \mathbb{R}^{r}$

<b>Theorem (Regularity)</b> For an exponential and regular model with $\emptyset \neq \Lambda\subset \mathbb{R}^{r}$ that satisfy (A5) one obtain that $I(\lambda)$ and equals to:

$$
\boxed{I(\lambda) = - \mathbb{E}_{\lambda}\Big[ \frac{\partial^{2}\text{log}(L(x;\lambda))}{\partial\lambda\partial \lambda^{t}} \Big]}
$$

<b>Theorem (Identifiability):</b> An exponential model with $\emptyset \neq \Lambda \subset \mathbb{R}^{r}$ is <b>identifiable</b> if and only if the <b>FIM</b> $I (\lambda)$ is <b>invertible</b> $\forall\lambda \in \Lambda$

<b>Theorem (Necessary condition):</b> Let's consider a regular exponential model and $\delta$ an unbiased regular estimator $\delta$ of $g(\theta) \in C^{1}$. Moreover, let $I(\theta)$ be invertible $\forall \theta \in \Theta$. Thus, if $\delta$ is efficient, it is necessary an affine function of $S(x)=(S_{1}(x),···,S_{r}(x))$.

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

<b>Corollary:</b> In an exponential model of the natural form where $\emptyset \neq \Lambda \subset \mathbb{R}^{r}$ and where $I(\lambda)$ is invertible $\forall \lambda \in \Lambda$.
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
 \rightarrow^{dist} z \text{ with } E_{\theta_{0}}[z]=0$$

<i>Remark:</i> Different from "unbiased at the limit:" $E_{\theta_{0}}[\hat{\theta}_{n}]\rightarrow g(\theta_{0})$

<b>Definition (Asymptotically normal)</b> $\hat{\theta}_{n}$ os asymptotically normal if

$$
\sqrt{n}(\hat{\theta}_{n} - g(\theta_{0})) \rightarrow^{dist} \mathcal{N}(\textbf{0}, \Sigma(\theta_{0}))
$$

where $\Sigma(\theta_{0})$ is the asymptotic CM of $\hat{\theta}_{n}$

<i>Remark:</i> This implies that $\hat{\theta}_{n}$ is asymptotically unbiased.

<b>Definition (Asymptotically efficient):</b> An estimator is asymptotically efficient if it is asymptotically normal and if:

$$
\Sigma(\theta_{0}) = \frac{\partial g}{\partial \theta^{t}}(\theta_{0})I(\theta_{0})^{-1} \frac{\partial g^{t}}{\partial \theta}(\theta_{0})
$$

### 3.2. Method of moment

<b>Theorem</b>

$$
\begin{align}
U_{p} = \frac{1}{n}\sum_{i=1}^{n}x_{i}^{p} &\rightarrow^{a.s.} m_{p} = E_{\theta}[\textbf{x}^{k}]\\
\sqrt{n}(\textbf{U}-\textbf{m}) &\rightarrow ^{dist}\mathcal{N}(\textbf{0}, \textbf{Z})
\end{align}
$$

where $\textbf{U} = (U_{1}, ..., U_{p})$ and $\textbf{m} = (m_{1}, ..., m_{p})$

<b>Theorem (Asymptotics of the MM estimator)</b> If the function $\psi(\textbf{U}) = \theta_{n}$ is differentiable then:

$$
\begin{align}
\hat{\theta}_{n} &\rightarrow^{a.s.} \theta\\
\sqrt{n}(\hat{\theta}_{n} - \theta) &\rightarrow^{dist}\mathcal{N}(\textbf{0}, \textbf{A}(\theta))
\end{align}
$$

where $\textbf{A}(\theta) = \frac{\partial\psi}{\partial\theta^{t}}(m) \Sigma(\theta) \frac{\partial\psi^{t}}{\partial\theta}(m)$

MME strongly consistant, asymptotically normal BUT generally NOT asymptotically efficient!

### 3.3. Method of Maximum Likelihood

<b>Definition (Maximum Likelihood Estimator (MLE))</b>

Consider a regular model that satisfy (A5) and (A6)

> (A6) $\forall x \in \Delta$, for $\theta$ close to $\theta_{0}$, $\text{log}(f(x;\theta))$ is three times differentiable w.r.t. $\theta$ and
>
> $$ \lvert\frac{\partial^{3}}{\partial \theta_{j}\partial \theta_{k}\partial \theta_{l}}\text{log}(f(x; \theta))\rvert \leq M(x) $$
>
> with $E_{\theta_{0}}[M(x)] < + \infty$

<b>Proposition:</b> Assume that the model is identifiable then $\forall \theta \neq \theta_{0}$, one has:

$$
P_{\theta_{0}}(L(\textbf{x}, \theta_{0}) > L(\textbf{x}, \theta )) \rightarrow 1
$$

<b>Definition (MLE)</b> The MLE is defined by

$$
T:(\textbf{x}_{1}, ..., \textbf{x}_{n}) \mapsto \hat{\theta}_{n}\in \text{argmax}_{\theta\in \Theta} L(\textbf{x}_{1}, ..., \textbf{x}_{n}; \theta)
$$

The MLE has to verified the following likelihood equations!

$$
\begin{cases}
\frac{\partial}{\partial\theta}l(\theta) = 0\\
\frac{\partial^{2}}{\partial\theta\partial\theta^{t}}l(\theta) \leq 0
\end{cases}
$$

<b>Proposition:</b> Let $g:\Theta\mapsto\mathbb{R}^{p}$. If $\hat{\theta}_{n}$ is the MLE of $\theta$ then $g(\hat{\theta}_{n})$ is also a MLE of $g(\theta)$

<i>Note:</i> The MLE is not necessary unique..

<b>Theorem:</b> Assume that the model is identifiable, that (A1) and (A2) hold and that $\theta_{0} \in \Theta \neq \emptyset$ compact and:
- $x_{1} \mapsto L(x_{1}, \theta)$ is bounded $\forall \theta \in \Theta$
- $\theta \mapsto L(x_{1}, \theta)$ is continuous $\forall x_{1} \in \Delta$

$$
\boxed{\hat{\theta}_{n}^{ML} \rightarrow^{a.s.} \theta_{0}}
$$

<b>Theorem (Classical asymptotics)</b>

Assume that the model is identifiable and that $\Theta$ is an open set of $\mathbb{R}^{d}$ and (A1)-(A6) hold. Then, it exists $\hat{\theta}_{n}^{ML}$ (from a given $n_{0}$) solution to the likelihood equations such that:

$$
\begin{cases}
\hat{\theta}_{n}^{ML} \rightarrow^{a.s.} \theta_{0}\\
\sqrt{n}(\hat{\theta}_{n}^{ML} - \theta_{0}) \rightarrow^{dist} \mathcal{N}(\textbf{0}, I_{1}(\theta_{0})^{-1})
\end{cases}
$$

If furthermore we have that $g$ is differentiable then it exists $\hat{\theta}_{n}^{ML}$ (from a given $n_{0}$) solution to the likelihood equations such that:

$$
\begin{cases}
\hat{\theta}_{n}^{ML} \rightarrow^{a.s.} \theta_{0}\\
\sqrt{n}(\hat{\theta}_{n}^{ML} - \theta_{0}) \rightarrow^{dist} \mathcal{N}(\textbf{0}, \frac{\partial g}{\partial\theta^{t}}(\theta_{0})I_{1}(\theta_{0})^{-1}\frac{\partial g^{t}}{\partial\theta}(\theta_{0}))
\end{cases}
$$

<b>Conclusions:</b> The MLE is strongly consistant, asymptotically normal and asymptotically efficient.

<b>Come back on exponential models</b> Let an exponential model with $\lambda \in \Lambda \neq \emptyset$ and $I(\lambda)$ invertible $\forall \lambda in \Lambda$ (identifiable model). Thus, the MLE exists (from a given n_{0}), is unique, strongly consistant and asymptotically efficient (which includes asymptotically normal).

### 3.4. Bayesian estimation

<u>Principles:</u> Philosophy is different from previous MM/ML estimation approaches (frequentist methods). The purpose is the same: estimating an unknown parameter $\theta \in \mathbb{R}$ or $\mathbb{R}^{p}$ thanks to the sample $(x_{1},...,x_{n})$ likelihood (parameterized by $\theta$) and an a priori distribution $p(\theta)$. So, $\theta$ is assumed to random.

<u>Ideas:</u> To that end, one has to minimize a cost function $c(\theta,\hat{\theta})$ that
represents the error between $\theta$ and its estimator $\hat{\theta}$.

<u>Reminders:</u> A posteriori distribution / posterior distribution

$$
\boxed{p(\theta \mid \textbf{x}_{1}, ..., \textbf{x}_{1}) \propto L(\textbf{x}_{1}, ..., \textbf{x}_{1} ; \theta)\cdot p(\theta)}
$$

<b>MMSE estimator (mean of the posterior PDF)</b> is the estimator that minimizes the MSE as the cost function:

$$
c(\theta, \hat{\theta}) = E[(\theta - \hat{\theta})^{2}]
$$
There are two cases:

1. $\theta \in \mathbb{R}$

$$
E[(\theta - \hat{\theta}_{MMSE})^{2}] = \text{min}_{\pi}E[(\theta - \pi(x))^{2}]
$$

so

$$
\hat{\theta}_{MMSE}(x) = E[\theta \mid \textbf{x}]
$$

2. $\theta \in \mathbb{R}^{p}$.
The MMSE estimator $\hat{\theta}_{MMSE}(x) = E[\theta \mid x]$ minimizes the quadratic cost:

$$
E[(\theta - \pi(x))^{t} Q (\theta - \pi(x))]
$$

for any symmetric definite positive matrix $Q$ (and in particular for $Q = I_{p}$ the identity matrix).

<b>MAP estimator:</b> Once again there are two cases:

1. $\theta \in \mathbb{R}$

The MAP estimator $\hat{\theta}_{MAP}(\textbf{x})$ minimizes the average of a uniform cost function:

$$c((\theta - \pi(x))) = \begin{cases}
0 \text{ if } \mid \theta - \pi(x) \mid \leq \Lambda / 2\\
1 \text{ if } \mid \theta - \pi(x) \mid > \Lambda / 2
\end{cases}
$$

and is defined by:

$$
c((\theta - \hat{\theta}_{MAP}(\textbf{x}))) = min_{\pi} c((\theta - \pi(x)))
$$

If $\Lambda$ is arbitrarily small, $\hat{\theta}_{MAP}(\textbf{x})$ is the value of $\pi(x)$ which maximizes the posterior $p(\theta\mid x)$ hence its name MAP estimator. It is computed by setting to zero the derivative of $p(\theta \mid x)$ or its log with respect to $\theta$.

2. $\theta \in \mathbb{R}^{d}$

Determine the values of $\theta_{j}$ which make the partial derivatives of $p(\theta \mid \textbf{x})$ (or its logarithm) with respect to $\theta_{i}$ equal to zero.

------
