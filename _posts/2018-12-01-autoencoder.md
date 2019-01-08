---
title: 'Auto-encoder'
date: 2018-12-01
permalink: /posts/Deep-Learning/autoencoder
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

```python
# Architecture definition
encoded = Dense(15, activation='sigmoid')(input_img)
encoded = Dense(11, activation='sigmoid')(encoded)
encoded = Dense(11, activation='sigmoid')(encoded)
encoded = Dense(8, activation='sigmoid')(encoded)
decoded = Dense(11, activation='sigmoid')(encoded)
encoded = Dense(11, activation='sigmoid')(encoded)
decoded = Dense(15, activation='sigmoid')(decoded)
decoded = Dense(18, activation='relu')(decoded)

autoencoder = Model(input_img, decoded)

# Compilation
autoencoder.compile(optimizer='adadelta', loss = 'mean_squared_error')

# Training
autoencoder.fit(X_train, X_train,
                epochs=5,
                batch_size=1000,
                shuffle=True,
                validation_data=(X_test, X_test))
```

## Adding a sparsity constraint on the encoded representations

In the previous example, the representations were only constrained by the size of the hidden layer (32). In such a situation, what typically happens is that the hidden layer is learning an approximation of PCA (principal component analysis). But another way to constrain the representations to be compact is to add a sparsity contraint on the activity of the hidden representations, so fewer units would "fire" at a given time. In Keras, this can be done by adding an activity_regularizer to our Dense layer:

```python
# Size of our encoded representations
encoding_dim = 9  # 9 floats: compression of factor 2

# Input placeholder
input_purchase = Input(shape=(18,))
# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='sigmoid', activity_regularizer=regularizers.l1(10e-5))(input_purchase)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(18, activation='sigmoid')(encoded)

# Maps an input to its reconstruction
autoencoder = Model(input_purchase, decoded)

# Maps an input to its encoded representation
encoder = Model(input_purchase, encoded)

# Placeholder for an encoded (9-dimensional) input
encoded_input = Input(shape=(encoding_dim,))
# Retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# Create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adam', loss='mean_squared_error')
autoencoder.fit(X_train, X_train,
                epochs=5,
                batch_size=1000,
                shuffle=True,
                validation_data=(X_test, X_test))
```

# Variational Autoencoder

Variational autoencoders are a slightly more modern and interesting take on autoencoding.

It's a type of autoencoder with added constraints on the encoded representations being learned. More precisely, it is an autoencoder that learns a latent variable model for its input data. So instead of letting your neural network learn an arbitrary function, you are learning the parameters of a probability distribution modeling your data. If you sample points from this distribution, you can generate new input data samples: a VAE is a "generative model".

How does a variational autoencoder work?

First, an encoder network turns the input samples $x$ into two parameters in a latent space, which we will note $z_{mean}$ and $z_{log_\sigma}$. Then, we randomly sample similar points $z$ from the latent normal distribution that is assumed to generate the data, via $z = z_{mean} + exp(z_{log \sigma}) * \epsilon$, where $\epsilon$ is a random normal tensor. Finally, a decoder network maps these latent space points back to the original input data.

The parameters of the model are trained via two loss functions: a reconstruction loss forcing the decoded samples to match the initial inputs (just like in our previous autoencoders), and the KL divergence between the learned latent distribution and the prior distribution, acting as a regularization term. You could actually get rid of this latter term entirely, although it does help in learning well-formed latent spaces and reducing overfitting to the training data.




------
