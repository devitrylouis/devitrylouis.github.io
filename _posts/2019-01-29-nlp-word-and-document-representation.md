---
title: 'Language modelling'
date: 2018-12-01
permalink: /posts/2019/01/nlp-language-modelling/
layout: default
comments: true
tags:
  - NLP
---

## 1. Historical prespective

### 1.1. Bag of Word

When it comes to supervised learning in general, the goal can most often than not be boiled down to finding a parametrized model $f_{\theta}$ that explains best some annotated data $\{ (x_{i}, y_{i}) \}_{i=1}^{N}$. And usually, the parameters $\theta$ are learnt to satisfy:

$$
\theta = \text{argmin}_{\theta}\frac{1}{N} \sum_{i=1}^{N} L(f_{\theta}(\phi(x_{i})), y_{i}) + \lambda \cdot R(\theta)
$$

where $\phi$ is some feature extraction function and $R$ some regularization. Altogether, it simply means that the model parameters $\theta$ are learnt to map at best a representation $\phi$ of the data $(x_{i})_{i=1}^{N}$ to our targets $(y_{i})_{i=1}^{N}$!

> TODO: Give some examples of NLP + SL

<b>The missing piece:</b> In NLP, the first major feature representation $\phi$ is is the Bag-of-word (BOW), which is credited to Gerard Salton (see this [The Most Influential Paper Gerard Salton Never Wrote](https://www.ideals.illinois.edu/bitstream/handle/2142/1697/Dubin748764.pdf?sequence=2) for more details).

<b>Example:</b> For the sentence `"John likes to watch movies. Mary likes movies too." `, it works by counting each words and storing the results with dictionaries:

```python
bag_of_words = {
  "John":1,
  "likes":2,
  "to":1,
  "watch":1,
  "movies":2,
  "Mary":1,
  "too":1
}
```

In practice though, storing dictionaries is quite inefficient, so one should use the [hashing trick](https://en.wikipedia.org/wiki/Feature_hashing) to simplify the implementation of bag-of-words models and improve scalability. In NLP, the simplest hashing is the document-term matrix, whose columns are the words and the rows are the documents. It is a sparse matrix of size $N \times V$, with $V$ being the size of our vocabulary. It looks quite like this one:

![Document term matrix](https://www.darrinbishop.com/wp-content/uploads/2017/10/Document-Term-Matrix-with-Title-1.png)

<b>Drawbacks of BoW:</b> This representation is nonetheless limited because it does not account for the word order, multi-word expressions and finally because words are discrete.

> TODO: Give examples if possible

### 1.2. Pre deep learning era

Before the first successes of Deep Learning in NLP, the common procedure to build a representation $\phi$ was based on combinations of the following building blocks:

- [Document-term matrix defined above](https://en.wikipedia.org/wiki/Document-term_matrix)
- [Stemmed Word](https://en.wikipedia.org/wiki/Stemming)
- [Lemmatized Word](https://en.wikipedia.org/wiki/Lemmatisation)
- Information from lexical data-bases (dictionaries, hypernyms, synonyms,....)
- [POS tags](https://en.wikipedia.org/wiki/Part-of-speech_tagging)


- Previous / next words
- Prediction on previous words

To use machine learning machinery, need encoding of sequence into vector. Traditionally (2000 – 2015) done through feature engineering
-> sparse vectors, where each dimension corresponds to one feature
Use linear separator on that space
or transformed space (kernel trick)

### 1.3. The promises of Deep Learning

Produce a higher-level representation
Lealrn those features
Dimension do not mean anything obvious anymore
Go from high-dimension sparse vectors to low (~ 100s,1000s) dimension, dense. The rest (could) remain the same....

## 3. Feature engineering for documents
### 3.1. Distributional hypothesis
> “A synopsis of linguistic theory” John Firth 1963
### 3.1. Harris substitutability theory
### 3.1. Term-Document matrix
### 3.1. Distributional hypothesis
### 3.1. Co-occurrence matrix
### 3.1. Weighting Co-occurrence matrix
### 3.2. Densify it with SVD

## 4. Word2vec

1. [What is skipgram?](#skipgram)
    * [What is learnt?](#embeddings)
    * [How does it learn?](#neural_net)
    * [How to learn even faster?](#negative_sampling)
    * [Draw Negative samples ](#negative_sampling)
    * [Back-propagation equations - TODO](#back_propagation)
2. [Pre-processing is done in `__init__`!](#init)
    * [Text preprocessing](#text-preprocessing)
    * [Hyperparameters](#hyperparameters)
    * [Vocabulary](#vocabulary)
    * [Corpus encoding](#encoding)
    * [Negative sample distribution](#neg_sample_dist)
3. [The full `train` procedure](#train)
    * [The gradients in python](#gradients)
    * [A naïve learning procedure](#naive)
    * [Retrieve the contexts](#contexts)
    * [How to construct and learn a batch? - TODO](#batch)
    * [Negative sampling in practice](#practical_ng)
    * [Optimizing context and learning computations](#optimizing)
4. [Improve word2vec](#improve)
    * [Dynamic window size](#dynamic_window)
    * [Subsampling and rare word pruning](#subsampling)
5. [Experiments](experiments)
    * [Evaluation with SimLex](#evaluation)
    * [Post-processing embeddings with PCA](#pca)
6. [Future work](#future)
    * [Character n-grams](#ngrams)
    * [Algebraic properties of the embeddings](#algebraic)
### 4.1. Learn the representation
### 4.1. Word2Vec [Mikolov et al. 2013]
### 4.1. Word2Vec
### 4.1. Fun with Word Embeddings
### 4.1. Drawbacks of word embeddings

## 5. Practical Hints

## 6. Sources

- [Lecture notes of Naver Labs](http://www.europe.naverlabs.com/Research/Natural-Language-Processing)
- [Wikipedia](en.wikipedia.org)
- [Columbia blogpost](http://www.ee.columbia.edu/~stanchen/e6884/labs/lab3/x207.html)

------
