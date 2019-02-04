---
title: 'Language modelling'
date: 2018-12-01
permalink: /posts/2019/01/nlp-language-modelling/
tags:
  - NLP
---

Language is ambiguous, and we are decoding all the time the most probable meaning

Let a sentence be the ordered set $S = \{w_{1}, w_{2}, ..., w_{\mid S \mid} \}$, we want to compute its probability $P$ defined by:

$$
\mathcal{P}(S) = P(\{w_{1}, w_{2}, ..., w_{\mid S \mid} \})
$$

This model is a building block of many important algorithm, from spell correction $(\mathcal{P}("Hello world") > \mathcal{P}("World hello")$) to re-ranking (Optical Character Recognition and Automatic Speech Recognition).

## Conditional model

### Framework

The ordered nature of the sentence implies that if the sentence is shuffled, its corresponding probability changes. Consequently, one uses conditional probability derived from the chain rule:

$$
\mathbb{P}(\{w_{1}, w_{2}, ..., w_{\mid S \mid} \}) =\Pi_{i=1}^{\mid S\mid - 1} \mathbb{P}(w_{\mid S \mid - i}\mid w_{1}, w_{2}, ..., w_{\mid S \mid - i-1})
$$

with the terms of the product $\mathbb{P}(w_{\mid S \mid - i}\mid w_{1}, w_{2}, ..., w_{\mid S \mid - i-1})$ is estimated with Maximum Likelihood:

$$
\mathbb{P}(w_{\mid S \mid - i} \mid w_{1}, w_{2}, ..., w_{\mid S \mid - i - 1}) = \frac{c(w_{1}, w_{2}, ..., w_{\mid S \mid - i})}{c(w_{1}, w_{2}, ..., w_{\mid S \mid - i -1})}
$$

where $c(w_{1} w_{2} ... w_{k})$ is the number of occurences of the sentence $w_{1} w_{2} ... w_{k}$ in a big corpus text.

### $n$-gram

The problem is that as $k$ increases, $c(w_{1} w_{2} ... w_{k})$ converges to zero (long sentence are by definition scarcer than short on average).

To solve this issue, we assume the conditional probabilities are Markovian, meaning that only the $n$ most recent words matter:

$$
\mathbb{P}(w_{i} \mid w_{1} ... w_{i-1}) = \mathbb{P}(w_{i} \mid w_{i-n+1} ... w_{i-1})
$$

This assumption approximately holds true for text because of few long-range approximaion.

Depending on the hyperparameter $n$, this technique is called $n$-gram.

### Practical ressources

<b>Toolkits:</b>
- [CMU-Cambridge](http://www.speech.cs.cmu.edu/SLM)
- [SRILM](http://www.speech.sri.com/projects/srilm/)
- [KenLM](https://kheafield.com/code/kenlm/): integrated into Moses (phrase-based MT)

<b>Data</b>
- [Google Books Ngrams](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html)
    * 8M books (6% of all books every published)
    * Binned by years (culturomics)
- [Ngrams of Corpus of Contemporary American English](https://www.ngrams.info/download_coca.asp)
- Any data-set : The one task in NLP where annotation is not an issueHave to pre-process (small domain-specific often > large generic-domain)

### Evaluation - Find the most plausible next word

How do we find $n$?

Training on train data:

<b>Evaluation</b>
1. Word Error Rate: how many times your best prediction is incorrect
Problem: what if your second one was good with p = 0.49?
2. Final task: impact of different Language Model on end-task 
    * time-consuming
    * co-founding variables

<b>Evaluation: Perplexity</b>
Interpretation: maximise probability
“how well can you predict upcoming word?”
“amount of surprise that the test data generates for your model“

------
