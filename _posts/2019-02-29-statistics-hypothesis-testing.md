---
title: 'Statistics basics'
date: 2018-12-01
permalink: /posts/2019/01/hypothesis-techniques/
tags:
  - Statistics
---


## 1. Generalities

## 1.1. Principles

Let a $n$-sample $(x_{1}, ..., x_{n})$ i.i.d $\sim P_{\theta}, \theta \in \Theta$ and $H_{0}, H_{1}$ be two non empty and disjoint subsets of $\Theta$ s.t. $H_{0} \cup H_{1} = \Theta$.

$H_{0}$ is the <u>null hypothesis</u> and $H_{1}$ is called the <u>alternative hypothesis</u>.

The <b>goal</b> is to test wether $\theta$ belongs to $H_{0}$ or not, regarding the datasets $X$.

<b>Definition:</b> An <u>hypothesis</u> is said <u>simple</u> if it is reduced to a single element. Else, it is called composite.

<b>Definition:</b> A <u>pure test</u> is a mapping $\delta$ from $X^{n}$ onto $\{0, 1 \}$ s.t. if $\delta(x) = 0$, one decides $H_{0}$, while if $\delta(x) = 1$, one rejects $H_{0}$.

The region $X = \{ x \in X^{n} \mid \delta(x) = 1 \}$ is called the rejection region or the critical region. Its complement is called the acceptance region.

## 1.2. Errors, power and level of a test

<i>Remark</i> A test is characterized (and will be identified) by its rejection region $W$.

<b>Definition (Different errors)<b> For a test, there are two possible error/s:
- Rejecting $H_{0}$ when it is true: type-I error or error of 1st kind.
- Accepting $H_{0}$ when it is false: type-II error or error of 2nd kind

<b>Definition (Type-I and Type-II errors)<b> For a test $\delta$ with critical regi/on $W$, one has:

1. <u>Type I error:</u>
$$\alpha_{W}:
\begin{cases}
H_{0} \rightarrow [0, 1]\\
\theta \rightarrow P_{\theta}(W)\\
\end{cases}
$$

2. <u>Type II error:</u>
$$\beta_{W}:
\begin{cases}
H_{1} \rightarrow [0, 1]\\
\theta \rightarrow P_{\theta}(W^{C}) = 1 - P_{\theta}(W)\\
\end{cases}
$$

<b>Definition (Power of a test):</b> The power of a test is defined as:

$$
\rho_{W}:\begin{cases}
H_{1} \rightarrow [0, 1]\\
\theta \rightarrow P_{\theta}(W) = 1 - \beta_{W}(\theta)\\
\end{cases}
$$

<b>Definition (Randomized test)</b> A random test is a mapping $\phi$ form $X^{n}$ in to $[0, 1]$ where $\phi(x)$ is the probability of rejecting $H_{0}$ for the dataset $x = (x_{1}, ..., x_{n}) \in X^{n}$

<i>Remark:</i> For $\phi = 1_{W}$, one retrieves the simple test.

<b>Definition (Type I and type II errors, power for a test $\phi$)</b>

1. <u>Type I error:</u>
$$\alpha_{\phi}:
\begin{cases}
H_{0} \rightarrow [0, 1]\\
\theta \rightarrow E_{\theta}[\phi(\textbf{x})]\\
\end{cases}
$$

2. <u>Type II error:</u>
$$\beta_{\phi}:
\begin{cases}
H_{1} \rightarrow [0, 1]\\
\theta \rightarrow 1 - E_{\theta}[\phi(\textbf{x})]\\
\end{cases}
$$

$$ \rho_{\phi} = 1 - \beta_{\phi} = E_{H_{1}}[\phi(\textbf{x})] $$

<b>Definition (Level of significance (ls))</b> The level of significance $\alpha$ for a test $\phi$ is:

$$
\alpha = \sup_{\theta \in H_{0}} \alpha_{\phi}(\theta) = sup_{\theta \in H_{0}} E_{\theta}[\phi(\textbf{x})]
$$

## 1.3. Neyman approach

<b>Goal:</b> One wants to control / fix the type-I error (i.e. the probability of rejecting $H_{0}$ when it is true).

The <u>Neyman principle</u> consists in considering all tests with $ls \leq$ to a fixed $\alpha$ anf then, in finding (among those tests), the one with the smallest type-II error.

Since $\rho_{\phi} = 1 - \beta_{\phi}$, such test will be said to be UMP.

<b>Definition (Uniformlu Most Powerful)</b>

$\phi$ is UMP at the threshold $\alpha$ it its $ls \leq \alpha$ and if $\forall \phi'$ which has $ls \leq \alpha$, one has:

$$
\forall \theta \in H_{1}, E_{\theta}[\phi(\textbf{x})] \geq E_{\theta}[\phi'(\textbf{x})]
$$

## 2. UMP tests

### 2.1. Simple hypothesis testing

In this part, for the $n$ sample $(\textbf{x}_{1}, ..., \textbf{x}_{n})$, one considers:

$$
H_{0}:\{ \theta = \theta_{0} \} versus H_{1}:\{ \theta = \theta_{1} \}
$$

which means that $\Theta = \{ \theta_{0}, \theta_{1} \}$

So two probabilities $P_{\theta_{0}}$ ($P_{0}$) and $P_{\theta_{1}}$ ($P_{1}$), that implies two Likelihodd functions $L_{0}(x) = L(x; \theta_{0})$ and $L_{1}(x) = L(x; \theta_{1})$, for $x= (x_{1}, ..., x_{n}) \in X^{n}$

<b>Definition (Neyman test or Likelihood Ratio Test):</b> A <u>Neyman test</u> is a test $\phi$ such that $\exists k \in \mathbb{R}_{+}^{ \text{*} }$, and

$$\phi(x) = \begin{cases}
1 \text{ if } L_{1}(x) > k L_{0}(x)\\
0 \text{ if } L_{1}(x) < k L_{0}(x)
\end{cases}
$$

The value of $\phi$ is specified for $\{ x \in X^{n} \mid L_{1}(x) = k L_{0}(x) \}$

<i>Remark:</i> $L_{1}(x) / L_{0}(x)$ is called the Likelihood Ratio (LR). The Neyman test consists in accepting the most likely hypothesis for a given observation $x$.

<b>Proposition (Neyman Pearson Lemma)</b>

1. Existence:
    * $\forall \alpha \in (0, 1)$ it exits a Neyman test such that $E_{\theta_{0}}(\phi) = \alpha$.
    * $k$ is the quantile of order $(1-\alpha)$ of the LR distribution $L_{1}(x) / L_{0}(x)$ under $P_{0}$ and one can impose that $\phi$ is constant for $x \in X^{n}$ such that $L_{1}(x) = kL_{0}(x)$.
    * If the LR CDF under $P_{0}$ evaluated in $k$ is $(1- \alpha)$ (continuous CDF), thus one can choose this constant = 0 (pure test)
2. S. cond. $\forall \alpha \in (0, 1)$; a Neyman test such that $E_{\theta_{0}}(\phi) = \alpha$ is UMP at level $\alpha$
2. N. cond. $\forall \alpha \in (0, 1)$; a UM test at level $\alpha$ is necessary a Neyman test.

<i>Remarks:</i>
1. Conclusion: the only UMP tests at level $\alpha$ are the Neyman tests of level of significance $\alpha$.
2. If the LR CDF under $H0$ is continuous, one obtains the test of critical region $W = \{x \in X^{n} \mid L_{1}(x) > kL_{0}(x) \}$ where $k$ is defined by $P_{0}(L_{1}(X)>kL_{0}(X)) = \alpha$
3. The power $E_{1}[\phi]$ of a UMP test at level $\alpha$ is necessarily $\geq \alpha$. Indeed $\phi$ is prefereable to the constant test $\psi = \alpha$ (which is of ls $\alpha$), thus $E_{1}(\phi) \geq E_{1}(\psi) = \alpha$

### 2.2. Composite tests - One-sided hypotheses

## 3. Student-t test

## 4. Asymptotic Tests

### 4.1. Generalities
### 4.2. Wald test
### 4.3. Rao (score) test and  LRT
### 4.4. $\chi^{2}$ tests

------
