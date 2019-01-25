---
title: 'Optimizing Deep Learning'
date: 2018-12-01
permalink: /posts/2018/11/advanced-dl/
tags:
  - Deep Learning
---

* Architectures as priors on function space, initializations as random nonlinear projections
--------------------------------------------------------------------------------------------

<b>Change of design paradigm:</b>
- <u>Classical ML:</u> design features by hand   vs   deep learning : meta-design of features : design architectures that are likely to produce features similar to the ones you would have designed by hand
- <u>Architecture:</u> a parameterized family (by the neural network's weights)
- <u>Note:</u> Still a similar optimization problem (find the best parameterized function), just, in a much wider space (many more parameters)

## Architecture

<b>TL; DR:</b> An architecture is a prior on the function, which state what is expressible or not with this architecture.

Despite having a huge capacity, some are often useless (==> probabilistic prior (what is easy to reach or not)).

In classical ML, lots of works on random features + SVM on top (usually from a kernel point of view); random projections. For a neural netwokn with random weights, the features are already good (or not far). Here, random is according to some law, see later.

In some cases at least (a-few-layer deep networks?), most of the performance is due to the architecture, not the training: fitting just a linear classifier on top of the random network doesn't decrease much the accuracy: [On Random Weights and Unsupervised Feature Learning, Andrew M. Saxe, Pang Wei Koh, Zhenghao Chen, Maneesh Bhand, Bipin Suresh, and Andrew Y. Ng, ICML 2011] (old: LeNet architecture, but maybe confirmed for VGG by another paper which I cannot find anymore... so, better to check if this study generalizes to modern architectures)

   ==> training whole or keeping random "non-linear projections": just about optimization order or speed (train last layer first)
   --> Extreme Machine Learning (EML) = learn only the last layer (not proved to work on "very" deep architectures such as modern networks)
     --> visualization of the quality of random weights in known architectures by reconstrucing the input, from the k-th layer activations [VGG with random weights]: no big information loss: [A Powerful Generative Model Using Random Weights for the Deep Image Representation, Kun He, Yan Wang, John Hopcroft, NIPS 2016]
   --> On deep architectures: learn a small part of the weights only : [Intriguing Properties of Randomly Weighted Networks: Generalizing While Learning Next to Nothing, Amir Rosenfeld, John K. Tsotsos]
      --> learn only a fraction of the features of each layer = sufficient to get good results (not very surprising)
      --> if one can learn only one layer, choose the middle one
      --> if you use random features: batch-norm is important (of course: the features should be "normalized" somehow at some point instead of making the function explode or vanish)

--> bias of the architecture (i.e. proba on possible functions to learn): example: Fourier spectrum bias [On the spectral bias of neural networks, Rahaman & al, NIPS 2018] : lower frequencies (i.e. big objects) are learned first

--> random initialization: random but according to a chosen law that induce good functional properties
 - avoid exploding or vanishing gradient (ex: activities globally multiplied by a constant factor > 1 or < 1 at each layer)
  --> Xavier Glorot initialization, or similar : [Understanding the difficulty of training deep feedforward neural networks, Xavier Glorot, Yoshua Bengio, AISTATS 2010]
     . multiplicative weights: uniform over [-1 / sqrt(d), +1 / sqrt(d)], or Gaussian(0, sigma^2 = 1/d)  where d = number of inputs of the neuron (justification: if weights w_i are Gaussian and inputs x_i of variance 1, sum_i w_i x_i will still be of variance ~ 1)
     . multiply by an activation-function-dependent factor if needed (eg: ReLU divide variance by 2, since they are 0 over half of the input domain, so, correct by * 2)
     . biases: 0
 - [Which neural net architectures give rise to exploding and vanishing gradients? NIPS 2018, Boris Hanin]
     . check the Jacobian df/dx at initialization
     . turns out that, with n_l = "number of neurons in layer l":
         . variance(df/dx) is fixed = 1/n_0
         . var( df/dx ^2), i.e. the fourth moment E[ df/dx ^4 ] is lower- and upper- bounded by terms in exp(sum_{layers l} 1/n_l )
         ==> sum 1/n_l is an important quantity
         ==> avoid many thin layers; if on a neuron budget, choose equal size for all layers

--> designing architectures easy to train
    . training "deep" networks : not really deep in terms of distance between any weight to tune and the loss information (except for orthonormal matrices...) for easier information communcation (through the backpropagation)
       --> ResNet architectures (see next chapter)
       --> or add intermediate losses (idem)
    . we saw that overparameterized networks (i.e. large layers) seem to be easier to train
    . is depth required? Not an easy question. [Do Deep Nets Really Need to be Deep? https://arxiv.org/abs/1312.6184] : learning a shallow network doesn't work; learning a deep one works; training a shallow one to learn the deep one works, and possibly with no more parameter than the deep one
       ==> "good architecture" is about "more likely to get the right function"; better, future optimizers might make smaller architectures more attractive


===================================================================

.===============.
| Architectures |
`==============='


[joke: deep_learning_vs_classical_ML.png]

NB: this is about current most popular architectures, not to be taken as an exhaustive, immutable list
--> "deep learning" is moving towards general "differentiable programming", with more flexible architectures/approaches every year: any computational graph provided all operations are differentiable.


Architecture zoo reminder (CNN, auto-encoder, LSTM, adversarial...)
-------------------------------------------------------------------

- CNN : reducing parameters by sharing local filters + hierarchical model (==> invariance to translation)
  --> needs to be interleaved with "zooming-out" operations (such as max-poolings) to be able to get wide enough receptive field (otherwise, won't see the whole object)
  --> conv block: conv ReLU conv ReLU max-pool    with conv 3x3 or so (better rewrite 15x15 as a hierarchical series of 3x3 filters: though the expressivity is similar, the probabilities are different, e.g. typical Fourier spectrum is different)

- auto-encoder, VAE, GAN, cycle-GAN : adversarial approach ==> no need to model the task anymore
 . cycle-GAN : when learning mappings between 2 domains (e.g., images of 2 different styles), ask that the two mappings be consistent [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks, Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros]

Recurrent networks
- basic RNN
  --> issue: memory? (keep a description of the context)
  --> get "leaky": progressive update of the memory
  --> get "gated": i.e. make the update amount dependent on the context (cf "attention" later)
- building & explaining LSTM [Long Short-term Memory, Sepp Hochreiter; J�rgen Schmidhuber, Neural Computation 1997]
- GRU: simplified version [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling, Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, Yoshua Bengio, NIPS 2014]
- simplifying more? if update = f(last input only): MinimalRNN [MinimalRNN: Toward More Interpretable and Trainable Recurrent Neural Networks, Minmin Chen, Symposium on Interpretable Machine Learning at NIPS 2017]
--> design of the "forget gate" justified by continuous analysis, with additional recommendations on bias initialization (equivalent to typical memory duration) as b ~ -log( Uniform[1, T_max] ) [Can recurrent neural networks warp time? Corentin Tallec, Yann Ollivier, ICLR 2018]



Dealing with scale & resolution
-------------------------------

The deeper we get, the bigger part of the image the net sees.

Classification / generation of high-resolution images: pyramidal approaches (e.g. any conventional conv-network for ImageNet / reverse pyramid for image generation)
- e.g., for classification (ImageNet): LeNet, AlexNet, VGG...
   . LeNet [eg: Handwritten digit recognition with a back-propagation network, Y. LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard, W. Hubbard, and L. D. Jackel, NIPS 1989]
   . AlexNet [Imagenet classification with deep convolutional neural networks, Alex Krizhevsky, Ilya Sutskever, Geoffrey E Hinton, NIPS 2012]
   . VGG [Very Deep Convolutional Networks for Large-Scale Image Recognition, K. Simonyan, A. Zisserman, ICLR 2015]
      ==> show image of VGG [vgg.png]
- one of the first realization with generative neural networks: [Deep Generative Image Models using a Laplacian Pyramid of Adversarial Networks, Emily Denton, Soumith Chintala, Arthur Szlam, Rob Fergus, NIPS 2015]
   --> example of the NVIDIA face generator (the old one): [Progressive Growing of GANs for Improved Quality, Stability, and Variation, Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen, ICLR 2018]

Same, full resolution for input and output simultaneously: details should not be lost, while reasoning at high level (object recognition) required
  ==> fully-convolutional [show conv-deconv.png], yet fine details lost
  ==> U-nets, with "skip-connections" [U-Net: Convolutional Networks for Biomedical Image Segmentation, Olaf Ronneberger, Philipp Fischer, Thomas Brox, MICCAI 2015]
   (show U-net.png)




Dealing with depth and mixing blocks - ADDING SKIP CONNECTIONS EVERY FEW BLOCKS
------------------------------------

IMPORTANT IS the depth of the propagation chain and not the network depth
Put architectures in parallel (resnet))

Training deep : not really deep in terms of distance to the loss information (except for orthonormal matrices...)
--> avoid gradient vanishing/exploding : orthonormal or Glorot...
--> chain of additions (ResNet) [Deep Residual Learning for Image Recognition, Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun, CVPR 2016]
       \-> show ResNet.png
        \-> each block = 2x conv-relu
--> or chain of blocks initialized to Identity (Highway network; not as common in the literature)
      \-> same as ResNet but with attention modules instead of additions (like LSTM, but non stationary) : alpha old + (1-alpha) new   with adaptative alpha
       \-> [Highway Networks, R. K. Srivastava, K. Greff and J. Schmidhuber, ICML 2015] --> [Highway and Residual Networks learn Unrolled Iterative Estimation, Klaus Greff, Rupesh K. Srivastava, J�rgen Schmidhuber, ICLR 2017]
--> Training a standard CNN with 10 000 layers is possible according to [Dynamical Isometry and a Mean Field Theory of CNNs: How to Train 10,000-Layer Vanilla Convolutional Neural Networks, Lechao Xiao, Yasaman Bahri, Jascha Sohl-Dickstein, Samuel S. Schoenholz, Jeffrey Pennington, ICML 2018]
    \-> using orthogonal matrices (for initialization) in such a way that no explosion/vanishing can happen
    \-> yet, validated on easy tasks only (MNIST, CIFAR 10); notice performance saturation with depth, and argue that architecture design = important, not just depth.

Inception [v1: Going deeper with convolutions, C Szegedy et al, CVPR 2015]
--> chain of blocks, each of which = parallel blocks whose outputs are concatenated (later turned in a ResNet form)
--> auxiliary losses at intermediate blocks to help training
--> show Inception.png

DenseNet [Densely Connected Convolutional Networks, Gao Huang, Zhuang Liu, Laurens van der Maaten, Kilian Q. Weinberger, CVPR 2017, https://arxiv.org/abs/1608.06993]
 --> series of blocks, each of them = feed-forward network of a few layers with dense connections between layers (i.e. each layer receives information from all previous ones in its block)
 --> show densenet.jpeg



Examples (case study)
---------------------

What architecture would you propose for:
- Aligning satellite RGB pictures with cadaster maps (indicating buildings, roads, etc.: one label per pixel), i.e. estimating the (spatial) deformation between the two images: full resolution output, multi-scale processing, very deep network
- Video analysis/prediction: auto-encoder + LSTM = conv-LSTM



Attention mechanisms, R-CNN
---------------------------

[Digest : Attention is all you need](http://mlexplained.com/2017/12/29/attention-is-all-you-need-explained/)

Basics of attention: one variable informing how to sum two other ones (tell which weights)
 --> cf MinimalRNN/LSTM

Case of many variables influencing each other [Attention is all you need, Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin, NIPS 2017]
 --> Principle; want to combine 'values', each of which is introduced with a 'key'; a 'query' will search for the most suitable 'keys' and combine the associated 'values' accordingly.
 --> attention block: function(query, keys, values): query |-> sum_i value(i) w(i)  with sum_i w(i) = 1 : softmax of (query . key(i))  i.e. pick values of similar keys
  \-> more exactly: normalize (query . key(i)) by sqrt(d) before applying softmax, where d = length(query) = length(key), for better initialization/training
 --> block "multi-head" : apply several attention modules and concatenate their outputs --> allow to assemble different parts of the 'value' vectors

Application of attention to features / blocks : [Squeeze-and-Excitation Networks, Jie Hu, Li Shen, Samuel Albanie, Gang Sun, Enhua Wu, CVPR 2017, https://arxiv.org/abs/1709.01507]
--> attention on features of a CNN / blocks in an Inception / features in a ResNet block / etc.
  `-> show squeeze_and_excitation_net.jpg


R-CNN : Region-CNN
--> papers: R-CNN, Mask R-CNN, Fast R-CNN, Faster R-CNN...
--> detect zones of interest (rectangles), then, for each zone, rectify it, and apply a classification/segmentation tool on it
- [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks, Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun, NIPS 2015]
--> idem but with attention mechanism: classification features = already computed before ('values'); use same features (pipeline) for detection and classification/segmentation
--> display RCNN.png FAsterRCNN.png



``memory"
---------

Not really working yet.
- most known papers: Memory networks / Neural Turing Machine / Sparse Access Memory
- attention mechanism to know when/where to write/read numbers in the memory
 --> reading = softmax over memory values, with weights depending on the weights for the "address"



GraphCNN
--------

Principles:
- a graph with values on nodes (and/or edges) is given as input
- each layer computes new values for nodes / edges, as a function of node neighborhoods
- same function for all nodes (neighborhoods) : kind of "convolutional"
- new node value may depend on edge values also (kind of attention)
- idem for edge values (function of node values, edges...)
- stack as many layers as needed
- max-pooling: means coarsening the graph (deleting nodes)
- etc.


Related literature:

Graph-conv-nets
- [Convolutional Networks on Graphs for Learning Molecular Fingerprints, David Duvenaud, Dougal Maclaurin, Jorge Aguilera-Iparraguirre, Rafael Gomez-Bombarelli, Timothy Hirzel, Alan Aspuru-Guzik, Ryan P. Adams, NIPS 2015]
- [Semi-Supervised Classification with Graph Convolutional Networks, Thomas N. Kipf, Max Welling, ICLR 2017]
   --> spectral view

With attention: [Graph Attention Networks, Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, Yoshua Bengio, ICLR 2018]
--> use node features to compute similarity between nodes (instead of values on edges)
--> multi-head attention for node value update

[Geometric deep learning on graphs and manifolds using mixture model cnns, Federico Monti, Davide Boscaini, Jonathan Masci, Emanuele Rodola, Jan Svoboda, Michael M. Bronstein, CVPR 2017]



Others / advanced
-----------------

Relation Networks
. first detect objects, then apply a network to these descriptions, for easier reasoning at the object (interaction) level.
. SHRDLU new age: [A simple neural network module for relational reasoning, Adam Santoro, David Raposo, David G.T. Barrett, Mateusz Malinowski, Razvan Pascanu, Peter Battaglia, Timothy Lillicrap, NIPS 2017]
. Image segmentation: image input --> conv for object detection, then fully-connected between objects, then back to image with convnets
       [Symbolic graph reasoning meets convolutions, X Liang, Z Hu, H Zhang, L Lin, EP Xing, NIPS 2018]

PixelRNN [Pixel Recurrent Neural Networks, Aaron van den Oord, Nal Kalchbrenner, Koray Kavukcuoglu, NIPS 2016]
  --> display PixelRNN.png

Wavenet : to deal with time in a hierarchical manner [WaveNet: A Generative Model for Raw Audio, Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, Koray Kavukcuoglu, 2016]
--> stack of dilated causal convolution layers (+ ResNet attention) [wavenet.jpeg]

[Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context, Zihang Dai, Zhilin Yang, Yiming Yang, William W. Cohen, Jaime Carbonell, Quoc V. Le, Ruslan Salakhutdinov, 2019]
--> stacked attention modules in a RNN (so: when a new input arrives, each of them is applied once, in series), with attention performed on the previous layer at all previous times.

NB: all LSTM / all conv / all attention : it all works (with proper design, initialization and training) and better than the other, previous methods (according to the papers)
 --> e.g.: [Attention Is All You Need, Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin, NIPS 2017]

Executing n steps after each new input before reading the next one (when applying a RNN), with variable n [Adaptive Computation Time for Recurrent Neural Networks, Alex Graves, 2016, unpublished]

Social LSTM [Social LSTM: Human Trajectory Prediction in Crowded Spaces, Alexandre Alahi, Kratarth Goel, Vignesh Ramanathan, Alexandre Robicquet, Li Fei-Fei, Silvio Savarese, CVPR 2016]
--> video analysis with several objects moving: one LSTM per object
--> interaction between objects: add communication in the graph of LSTMs



Other important pieces of design:
---------------------------------

- Loss design: (why not binary classification...) http://cs231n.github.io/neural-networks-2/

Activation functions:
- max-pool -> global average pooling --> ranking/softmax (to use/train all regions)

Layer size, feature size (number of neurones and/or features)


Opening:
--------

- hyperparameter tuning (architecture + optimization parameters)
--> auto-DL (Chapter 8)


----------------------------------------------

Refs:
http://www.deeplearningbook.org/

------
