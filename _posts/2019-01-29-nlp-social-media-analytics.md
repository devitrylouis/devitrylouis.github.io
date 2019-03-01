---
title: 'Language modelling'
date: 2018-12-01
permalink: /posts/2019/01/nlp-language-modelling/
layout: default
comments: true
tags:
  - NLP
---

## 1. Social Media Analytics: Introduction

* Overview: RICHER + BIGGER DATA -> Opportunities
* Applications
* Challenges

## 2. Preprocessing social media texts

Properties of Social Media Textual Data
Social Media Texts: a Foe of NLP?
Standard NLP tools Perform Poorly on Social Media Textual

### 2.1. POS Tagging

### 2.2. Lexical Normalization
PRINCIPLE + example
An Example of Token-Based Approaches

### 2.3. Bonus
Feature Representation Using Dependencies?
SVM Training Data Generation
Detecting Ill-Formed Words
Evaluation Results
Ex for project: Adapt NLP to data: CMU Twitter POS tagger

### 2.4. Summary: NLP tools and Noisy Input
• Lexical Normalization
    • Token based approaches
    • Distributional similarity approaches
• NLP Tools adaptation (POS, NER, Parsing)
    • CMU ARK TweetNLP http://www.ark.cs.cmu.edu/TweetNLP/ : Twokenizer, POS
    tagger, TweeboParser
    • Gate Twitter Pos Tagger https://gate.ac.uk/wiki/twitter-postagger.html

## 3. Sentiment Analysis

1. Reminder on text classification and evaluation measures
2. Sentiment analysis: Introduction
    * Negation
    * Coreference
    * Slang and writing errors
    * Comparative
    * Domain Dependent Opinion
    * Many more challenges
    * Subjectivity
    * What is an Opinion? (document / sentence level)
        * Mathematical definition
    * Entity and Aspect Level
    * Structured the Unstructured
    * Document Level sentiment analysis
    * Aspect Based Sentiment analysis
3. Affective lexicons = Dictionaries of well-known sentiment words

## 4. Methods for sentiment analysis

1. Machine Learning approaches
    * ML algorithms + linguistic features
2. Lexicon based approaches
    * Sentiment lexicons (pre-compiled terms)
    * Corpus-based
3. Hybrid approaches: combine both
4. Most frequent algorithms
    * Naïve Bayes
    * Maximum Entropy
    * Logistic Regression
    * SVM
    * Recently: Deep Learning: RNN (LSTMs), CNN & word embeddings

## 5. Methods for ABSA

ABSA: Fine-grained opinion annotation
• Determine sentiments about different aspects of entities (e.g. movies, restaurants, cell phones,...)
• Aspects are features of an entity (service, food in a restaurant; screen, battery of a cell phone,...)

## 4. Fake news and stance detection
Learn the representation
Word2Vec [Mikolov et al. 2013]
Word2Vec
Fun with Word Embeddings
Drawbacks of word embeddings

## 5. Practical Hints

## 6. Sources

- [Lecture notes of Naver Labs](http://www.europe.naverlabs.com/Research/Natural-Language-Processing)
- [Wikipedia](en.wikipedia.org)

------
