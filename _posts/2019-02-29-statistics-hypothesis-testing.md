---
title: 'Statistics basics'
date: 2018-12-01
permalink: /posts/2019/01/hypothesis-techniques/
tags:
  - Statistics
---


## 1. Generalities

## 1.1. Principles

<b>TL; DR:</b> Define a test to see whether the parameter $\theta$ belongs to some set $H_{0}$!

For $n$-sample $(x_{1}, ..., x_{n}) \overset{i.i.d}{\sim} P_{\theta}$ with $\theta \in \Theta$, we consider the <u>null hypothesis</u> $H_{0}$ and the <u>alternative hypothesis</u> $H_{1}$. They are a partition of $\Theta$ (i.e. $H_{0} \cup H_{1} = \Theta$ and $H_{0} \cap H_{1} = \emptyset$).

<b>Definition (Simple hypothesis):</b> The hypothesis is reduced to a single element. Else, it is called composite.

<b>Definition (Pure test):</b> It is a mapping $\delta$ from $X^{n}$ onto $\{0, 1 \}$ define so that:

<center>

|  Decide $H_{0}$  |   Reject $H_{0}$  |
|:----------------:|:-----------------:|
|  $\delta(x) = 0$ |  $\delta(x) = 1$  |
| Acceptance region | Rejection region |

</center>

<i>Remark</i> A test is characterized (and will be identified) by its rejection region $W$.

## 1.2. Errors, power and level of a test

For a test, there are <u>two possible errors</u>:

<center>

|   | Decide $H_{0}$ | Reject $H_{0}$ |
|:------------:|:--------------:|:--------------:|
| $H_{0}$ true | Good! | Type I error |
| $H_{1}$ true | Type II error | Good! |

</center>

Mathematically, for a pure test $\delta$ along its critical region $W=\{x\in X^{n}: \delta(x) = 1 \}$, the error types are defined respectively by:

$$
\alpha_{W}:
\begin{cases}
H_{0} \rightarrow [0, 1]\\
\theta \rightarrow P_{\theta}(W)\\
\end{cases} \text{ and }
\beta_{W}:
\begin{cases}
H_{1} \rightarrow [0, 1]\\
\theta \rightarrow P_{\theta}(W^{C}) = 1 - P_{\theta}(W)\\
\end{cases}
$$

- The [power of a test](https://apcentral.collegeboard.org/courses/ap-statistics/classroom-resources/power-in-tests-of-significance) is is the probability of correctly rejecting the null hypothesis:

$$
\rho_{W}:\begin{cases}
H_{1} \rightarrow [0, 1]\\
\theta \rightarrow P_{\theta}(W) = 1 - \beta_{W}(\theta)\\
\end{cases}
$$

- Pure tests are [not enough](https://www.quora.com/What-are-randomized-and-non-randomized-tests) for applications. In consequence, we define a <b>randomized test</b> $\phi: X^{n}\mapsto [0, 1]$, that is the probability of rejecting $H_{0}$ for our dataset $X^{n}$. We can retrieve the simple test for $\phi = 1_{W}$. But the errors definition and the power are different than in the pure test:

$$
\alpha_{\phi}:
\begin{cases}
H_{0} \rightarrow [0, 1]\\
\theta \rightarrow E_{\theta}[\phi(\textbf{x})]\\
\end{cases}
\text{ and }
\beta_{\phi}:
\begin{cases}
H_{1} \rightarrow [0, 1]\\
\theta \rightarrow 1 - E_{\theta}[\phi(\textbf{x})]\\
\end{cases}
$$

$$ \rho_{\phi} = 1 - \beta_{\phi} = E_{H_{1}}[\phi(\textbf{x})] $$

- As for assessing the performance of such test $\phi$, one typically use the <b>level of significance</b> $\alpha$, which verify:

$$
\alpha = \sup_{\theta \in H_{0}} \alpha_{\phi}(\theta) = \text{sup}_{\theta \in H_{0}} E_{\theta}[\phi(\textbf{x})]
$$

<b>Question:</b>
- Definition of $p$-value

<b>Notes:</b>
- [Difference between power and p-value](https://www.quora.com/What-is-the-relationship-between-statistical-power-and-the-p-value)

## 1.3. Neyman approach

The <u>Neyman principle</u> consists in fixing the type I error (i.e. the probability of rejecting $H_{0}$ when it is true) at signigicance level $\alpha$ and compute the tests with the minimal type II error. As it turns out, the randomized test $\phi$ is <b>Uniformly Most Powerful</b>: it has the highest power among all tests with $ls \leq \alpha$
$$
\forall \theta \in H_{1}, E_{\theta}[\phi(\textbf{x})] \geq E_{\theta}[\phi'(\textbf{x})]
$$

> <b>Question:</b>
> - Why "Since $\rho_{\phi} = 1 - \beta_{\phi}$, such test will be said to be UMP"?
> Because $\rho_{\phi}$ is the power.

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

Now let us consider a model with only one parameter and where $\Theta$ is an interval of $\mathbb{R}$. One assume $L(x; \theta) > 0, \forall x \in X^{n}, \forall \theta \in \Theta$.

<b>Goal:</b> test $H_{0}: \{ \theta \leq \theta_{0} \} versus H_{1}:\{ \theta > \theta_{0} \}$

Let us consider the family having monotonous likelihood ratio:

<b>Definition (Monotone LR)</b> The family $\{ P_{\theta}^{\symb}, \theta \in\Theta \}$ is said to have monotone likelihood ratio if it exists a real valued statistic $U(x)$ such that $\forall \theta ' < \theta'', \frac{L(x; \theta '')}{L(x; \theta ')}$ is a strictly increasing (or decreasing) function of $U$.

<i>Remark:</i> By changing $U$ into $-U$, one can always assume strictly increasing in previous definition.

<b>Theorem: (Lehman theorem)</b>

Let $\alpha \in (0, 1)$. If the family $(P_{\theta}, \theta \in \Theta)$ has monotone increasing likelihood ratio, there exists a UMP test at level $\alpha$ for testing $H_{0}: \{ \theta \leq \theta_{0} \}$ versus $H_{1}:\{ \theta > \theta_{0} \}$. This test is defined by:

$$
\begin{cases}
\phi(x) = 1 \text{ if } U(x) > c \\
\phi(x) = \gamma \text{ if } U(x) = c \\
\phi(x) = 0 \text{ if } U(x) < c
\end{cases}
$$

where $c$ and $\gamma$ are obtained with $E_{\theta_{0}}[\phi] = \alpha$. The same test is UMP at level $\alpha$ for testing:
1. $H_{0}: \{ \theta = \theta_{0} \} versus H_{1}:\{ \theta > \theta_{0} \}$
2. $H_{0}: \{ \theta = \theta_{0} \} versus H_{1}:\{ \theta = \theta_{1} \}$
where $\theta_{1} > \theta_{0}$

<i>Remark:</i> If the inequalities are reversed in the test, then the UMP test is obtained by reversing the inequalities (in the test).

<i>Remark (important)</i> In general, it does not exist a UMP test for testing $H_{0}: \{ \theta = \theta_{0} \} versus H_{1}:\{ \theta \neq \theta_{0} \}$

## 3. Student-t test

Let $(X_{1}, ..., X_{n}) \sim^{iid} \mathcal{N}(\mu, \sigma^{2})$ with $\mu$ and $\sigma^{2}$ unknown. The goal is to test $H_{0}: \{ \mu = \mu_{0} \}$ versus $H_{0}: \{ \mu = \mu_{1} \}$ at level $\alpha\in (0, 1)$.

The general methodology is:
1. From the student theorem, one has
$$ T_{n} = \frac{\sqrt{n}(\overline{X}_{n} - \mu)}{S_{n}} \sim t(n-1) $$
2. Under H_{0}:
$$ T_{n} = \frac{\sqrt{n}(\overline{X}_{n} - \mu_{0})}{S_{n}} \sim t(n-1) $$
3. Under $H_{1}$: From the SLLN, $\overline{X}_{n} - \mu_{0} \rightarrow^{a.s.}\mu- \mu_{0}$ ans $S_{n} \rightarrow^{a.s.} \sigma$. Thus $\eta \rightarrow^{a.s.} \infty$ if $\mu > \mu_{0}$ and $\eta \rightarrow^{a.s.} -\infty$ if $\mu < \mu_{0}$$
4. Critical region: $W_{n} = \{ \mid \eta_{n} \mid > a \}$

## 4. Asymptotic Tests

### 4.1. Generalities
### 4.2. Wald test
### 4.3. Rao (score) test and  LRT
### 4.4. $\chi^{2}$ tests

------
