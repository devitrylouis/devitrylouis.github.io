---
title: 'Auto-encoder'
date: 2018-12-01
permalink: /posts/2018/11/autoencoder/
tags:
  - Deep Learning
  - Basics
---

# Autoencoder

The objective of this story is to write a V0 of an autoencoder. Although there are ùany types of autoencoders, we will focus on a subset of them. Precisely, we are going to develop:

- Simple autoencoder based on a fully-connected layer
- Sparse autoencoder
- Deep fully-connected autoencoder

## What are autoencoders?

"Autoencoding" is a data compression algorithm where the compression and decompression functions are
1. data-specific: only be able to compress data similar to what they have been trained on.
2. lossy: the decompressed outputs will be degraded compared to the original inputs
3. learned automatically from examples rather than engineered by a human: it is easy to train specialized instances of the algorithm that will perform well on a specific type of input.

Additionally, in almost all contexts where the term "autoencoder" is used, the compression and decompression functions are implemented with neural networks.

To build an autoencoder, you need three things:
- Encoding function,
- Decoding function, and
- Distance function between the amount of information loss between the compressed representation of your data and the decompressed representation (i.e. a "loss" function).

The encoder and decoder will be chosen to be parametric functions (typically neural networks), and to be differentiable with respect to the distance function, so the parameters of the encoding/decoding functions can be optimize to minimize the reconstruction loss, using Stochastic Gradient Descent. It's simple! And you don't even need to understand any of these words to start using autoencoders in practice.


------
