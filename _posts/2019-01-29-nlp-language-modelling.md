---
title: 'Language modelling'
date: 2018-12-01
permalink: /posts/2019/01/nlp-language-modelling/
layout: default
comments: true
tags:
  - NLP
---

> "But it must be recognized that the notion ’probability of a sentence’ is an entirely useless one, under any known interpretation of this term."

Language is ambiguous, and we are decoding all the time the most probable meaning. Historically, we approached the problem by defining a sentence as an ordered set $S = \{w_{1}, w_{2}, ..., w_{\mid S \mid} \}$ to compute its probability $P$ defined by:

$$ \mathbb{P}(S) = P(\{w_{1}, w_{2}, ..., w_{\mid S \mid} \}) $$

This model is a building block of many important algorithm, from spell correction $(\mathbb{P}("Hello world") > \mathbb{P}("World hello")$) to re-ranking for Optical Character Recognition and Automatic Speech Recognition.

## 1. Conditional model

### 1.1. Framework

The ordered nature of the sentence implies that if the sentence is shuffled, its corresponding probability changes. Consequently, one uses conditional probability derived from the chain rule:

$$ \mathbb{P}(\{w_{1}, w_{2}, ..., w_{\mid S \mid} \}) =\Pi_{i=1}^{\mid S\mid - 1} \mathbb{P}(w_{\mid S \mid - i}\mid w_{1}, w_{2}, ..., w_{\mid S \mid - i-1}) $$

with the terms of the product $\mathbb{P}(w_{\mid S \mid - i}\mid w_{1}, w_{2}, ..., w_{\mid S \mid - i-1})$ is estimated with Maximum Likelihood:

$$
\mathbb{P}(w_{\mid S \mid - i} \mid w_{1}, w_{2}, ..., w_{\mid S \mid - i - 1}) = \frac{c(w_{1}, w_{2}, ..., w_{\mid S \mid - i})}{c(w_{1}, w_{2}, ..., w_{\mid S \mid - i -1})}
$$

where $c(w_{1} w_{2} ... w_{k})$ is the number of occurences of the sentence $w_{1} w_{2} ... w_{k}$ in a big corpus text.

### 1.2. $n$-gram

The problem is that as $k$ increases, $c(w_{1} w_{2} ... w_{k})$ converges to zero (long sentence are by definition scarcer than short on average).

To solve this issue, we assume the conditional probabilities are Markovian, meaning that only the $n$ most recent words matter:

$$
\mathbb{P}(w_{i} \mid w_{1} ... w_{i-1}) = \mathbb{P}(w_{i} \mid w_{i-n+1} ... w_{i-1})
$$

This assumption approximately holds true for text because of few long-range approximaion.

Depending on the hyperparameter $n$, this technique is called $n$-gram.

### 1.3. Practical ressources

<b>Data</b>
- [Google Books Ngrams](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html)
    * 8M books (6% of all books every published)
    * Binned by years (culturomics)
- [Ngrams of Corpus of Contemporary American English](https://www.ngrams.info/download_coca.asp)
- Any data-set : The one task in NLP where annotation is not an issueHave to pre-process (small domain-specific often > large generic-domain)

<b>Toolkits:</b>
- [CMU-Cambridge](http://www.speech.cs.cmu.edu/SLM)
- [SRILM](http://www.speech.sri.com/projects/srilm/)
- [KenLM](https://kheafield.com/code/kenlm/): integrated into Moses (phrase-based MT)

## 2. Evaluation - Find the most plausible next word

### 2.1. Word Error Rate and perplexity

A naïve way of proceeding is the <u>Word Error Rate</u> which consists of counting how many times the best prediction was correct. Its main drawback is that it is litteraly blind for the second and so on prediction.

In practice, it has negative impacts on the final NLP task because of its time-consuming nature and the presence of cofounding variables.

> TODO: Define co-founding variables

To palliate this issue, the concept of perplexity was introduced. It is simply a measurement of how well a probability distribution or probability model predicts a sample and is formally defined by:

$$
\begin{align}
ppx(q) &= 2^{-\sum \text{log}_{2}q(x_{i})}\\
&= 2^{H(p, q)}\\
\end{align}
$$

where $p$ is the observed (see empirical) distribution $p(x) = \frac{c(x)}{N}$.

A low perplexity indicates the probability distribution is good at predicting the sample. I found perplexity's intuition to be best explained by this [Quora answer](https://www.quora.com/What-is-perplexity-in-NLP), from which I quote this passage:

> Perplexity means inability to deal with or understand something complicated or unaccountable.<br> <br>
> When a toddler or a baby speaks unintelligibly, we find ourselves 'perplexed'. Why ? because their spoken language does not comply with the grammar and construct of the language that we tend to understand and speak.<br> <br>
> Now imagine you trained a machine learning NLP model on lots and lots of well written blogs and answers. Now the task is to evaluate how good a certain Quora answer is (for, say, pushing it to the top of the feed). Among very many models that you trained, which model will you select for picking good blogs from bad ?<br> <br>
> Answer: You would pick that NLP model which is least "perplexed" when presented with a well written blog.

Its main drawback though is that it requires lot of effort to model unseen events. To continue with the example above, let's ponder on how a model could predict that a very well written blog (from a new user) would be a hit? It's hard, and it lacks generalization. Another drawback is overfitting.

### 2.2. Smoothing

> Whenever data sparsity is an issue, smoothing can help performance, and data sparsity is almost always an issue in statistical modeling. In the extreme case where there is so much training data that all parameters can be accurately trained without smoothing, one can almost always expand the model, such as by moving to a higher n-gram model, to achieve improved performance. With more parameters data sparsity becomes an issue again, but with proper smoothing the models are usually more accurate than the original models. Thus, no matter how much data one has, smoothing can almost always help performance, and for a relatively small effort.” Chen & Goodman (1998)

The simplest case is Laplace Smoothing, which reverse some probability mass for unseen events:

$$
\mathbb{P}(w | c) = \frac{\# c.w}{\# c.w} \rightarrow \mathbb{P}(w | c) = \frac{\# c.w + \alpha}{\# c.w + \alpha V}
$$

where $V$ is the size of the vocabulary.

<i>Note:</i> Smoothing is useful in models like [Naïve Bayes](/posts/2019/02/ml-naive-bayes/) for instance.

> TODO: Give some variations examples

### 2.3. Back-off and interpolation

<b>TL; DR of backoff:</b> When we have weak evidence, we should use smaller contexts.

Mathematically, if the number of occurences $c(w_{i-2}w_{i-1}) > K$ is above some threshold $K$, we use:

$$
p(w_{i} | w_{i-2} w_{i-1}) = p_{2}(w_{i} | w_{i-1} w_{i-2})
$$

Otherwise, we use:

$$
p(w_{i} | w_{i-2} w_{i-1}) = p_{2}(w_{i} | w_{i-1})
$$

<b>TL; DR of interpolation:</b> Interpolation is a way to continuously manage the changements induced by back-off. Also refered to as Jelinek-Mercer in the literature, this combine signal from past contexts as:

$$
p(w_{i} | w_{i-2} w_{i-1}) = \lambda_{1}\cdot p_{2}(w_{i} | w_{i-1} w_{i-2}) + (1-\lambda_{1})\cdot p_{2}(w_{i} | w_{i-1})
$$

This is quite cool because it can be done recursively and works well with Maximum Likelihood Estimation.

As for the hyperparameter $\lambda_{1}$, it can be found on held-out data but not the training data!

### 2.4. Witten-Bell

Witten-Bell smoothing is this smoothing algorithm that was invented by some a guy named Moffat, but Witten and Bell have generally gotten credit for it. It is significant in the field of text compression and is relatively easy to implement, and that's good enough for us.

The intuition about Witten-Bell method is that the context of a word is naturally limited, because otherwise, it would not make much sense to try predicting it either way.

It models the probability of using a smaller-order model $(1 - \lambda_{c})$ as:

$$
\frac{\text{rd}(c)}{\text{rd}(c) + \sum_{w_{i}} \# cw_{i}}
$$

where $\text{rd}(c)$ is the <u>right-diversity</u> of $c$: $|\{ w | \# cw > 0 \}|$

### 2.5. Kneser-Ney

Kneser-Ney is widely considered the most effective method of smoothing due to its use of absolute discounting. This works by subtracting a fixed value from the probability's lower order terms, so as to omit n-grams with lower frequencies. This approach has been considered equally effective for both higher (Kneser-Ney) and lower order $n$-grams (Kneser-Ney II).


The Mathematics are given by:

$$
p(w_{i} | w_{i-1}) = \frac{\text{max}\big( c(w_{i-1}w_{i}) - \delta , 0\big)}{c(w_{i-1})} + \lambda_{w_{i-1}} p(w_{i})
$$

From this equation, one can retrieve:

$$
\lambda_{w_{i-1}} = \delta \frac{\text{rd}(w_{i-1})}{c(w_{i-1})}
$$

As for Kneser-Ney II, it is defined as:

$$
p(w_{i}) = \frac{\text{ld}(w_{i})}{N_{\text{bigrams}}}
$$

where $\text{ld}$ is the left diversity.

> TODO: Find definition of left diversity

In practice, "Modified Kneser-Ney" (normally) uses 3 different values for $\delta$ (for ngrams occurring 1, 2 and 3+ times).

<i>Notes:</i>
- Nonetheless, lower-order should only be used when higher-order are non-informative.
- And much like other smoothing techniques, it also set the probability mass for unseen event.

## 3. Data structures - OUT SOON

- Hashing
- Quantize probabilities
- Approximate hashing
- Suffix Trees

## 4. Sources

- [Lecture notes of Naver Labs](http://www.europe.naverlabs.com/Research/Natural-Language-Processing)
- [Wikipedia](en.wikipedia.org)
- [Columbia blogpost](http://www.ee.columbia.edu/~stanchen/e6884/labs/lab3/x207.html)

------
