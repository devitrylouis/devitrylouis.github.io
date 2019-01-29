---
title: 'Low-level vision'
date: 2018-12-01
permalink: /posts/2019/01/vic-low-level/
tags:
  - Visual computing
---

The goal of this article is to provide a Mathematical framework for the model of images. Specifically, we will recall the use of some operators (convolutions, correlation and cross-correlation) in signal processing. Then, we will define two approaches for expressing our image into a desirable signal, namely the Dirac delta function and the 2D Fourier transform. In the process, we will define in-depth the 2D Fourier transform and define a

This framework is motivated by the fact that images are finite and with compact support, so they behave well mathematically and most properties hold for them.

## Convolution, correlation and autocorrelation

In signal processing, three problems are common and are themselves enough to motivate this reminder:

<b>1. What is the output of this filter when its input is $x(t)$? </b>

The answer is given by $x(t) * h(t)$, where $h(t)$ is a signal called the <u>impulse response</u> of the filter, and $*$ is the convolution operation. Mathematically, the <u>convolution</u> is an operation on two functions ($f$ and $g$) which produce a third function $f * g$ that expresses how the shape of one is modified by the other. In the 1D space:

$$
(f * g)(x) = \int_{-\infty}^{\infty} f(u)g(x-u)du
$$

<b>2. Given a noisy signal $y(t)$, is the signal $x(t)$ somehow present in $y(t)$? </b>

In other words, is $y(t)$ of the form $x(t)+n(t)$, where $n(t)$ is noise? The answer can be found by the <u>correlation</u> of $y(t)$ and $x(t)$. If the correlation is large for a given time delay $τ$, then we may be confident in saying that the answer is yes. In 1D, the continuous correlation is defined as:

$$
(f\otimes g)(x) = \int_{-\infty}^{\infty} f(u)g(x+u)du
$$

<b>3. Is there any periodicity / repeating patterns in a noisy signal $y(t)$?</b>

Autocorrelation, also known as serial correlation, is the correlation of a signal with a delayed copy of itself as a function of delay. Informally, it is the similarity between observations as a function of the time lag between them. The analysis of autocorrelation is a mathematical tool for finding repeating patterns, such as the presence of a periodic signal obscured by noise.

$$
(f\otimes f)(x) = \int_{-\infty}^{\infty} f(u)f(x+u)du
$$

To summarize, here is an illustration of these operation inner workings:

![convolution_correlation](https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Comparison_convolution_correlation.svg/400px-Comparison_convolution_correlation.svg.png)

<i>Note:</i> Note that when the signals involved are symmetric, convolution and cross-correlation become the same operation; this case is also very common in some areas of DSP.

#### Properties

The convolution and the correlation satisfy the following set of properties:

<b>Linearity:</b>
- $f*(g+h) = f*g + f*h$
- $(f+g)*h = f*h + g*h$
- $\lambda (f*g) = (\lambda f)*g = f*(\lambda g)$

<b>Associativity:</b>
$$(f*g)*h = f*(g*h)$$

<b>Commutativity:</b> Works only for convolution
$$f*g = g*f$$

## $L^{2}(\mathbb{R})$ space

Now that we have defined the operators above, we will dive in their properties with respect to the <u>space of functions</u> they handle, namely:

$$
L^{2}(\mathbb{R}) = \{ f:\mathbb{R}\mapsto \mathbb{R}: \mid\mid f \mid\mid_{\mathcal{L}_{2}} < \infty \}
$$

where the $\mid\mid \cdot \mid\mid_{\mathcal{L}_{2}}$ is the norm corresponding to the following <u>dot product</u>:

$$
\langle f \mid g\rangle = \int_{-\infty}^{-\infty} f(x)g(x)dx
$$

• If we have a basis set for images, could perhaps be useful for
analysis – especially for linear systems because we could
consider each basis component independently.

Most notably, we are interested in finding convenient basis of the space, for which there are two main approaches:
- <u>Spatial basis</u> with Dirac Delta
- <u>Frequency basis</u> with Fourier transform



#### Dirac delta

In vision computing, Dirac delta helps measure the device's response to as simple an input as possible (i.e. a pixel):

![Image](/images/dirac_function.png)

Mathematically, this ideal input is reffered to as the <u>Dirac delta function</u>. It is defined as the limit (in the sense of distributions) of the sequence of zero-centered normal distributions:

$$
\delta(x) = \text{lim}_{a\rightarrow 0} \frac{1}{\mid a \mid \sqrt{\pi}}e^{-(x/a)^{2}}= \begin{cases}
\infty \text{ if x = 0}\\
0 \text{ otherwise}
\end{cases}
$$

Although it can be rigorously defined as a measure (thereby satisfying $\int_{-\infty}^{\infty}\delta(x)dx=1$), no such function exists. It is nonetheless very useful for approximating functions whose graphical representation is in the shape of a narrow spear:


![Dirac distribution](https://upload.wikimedia.org/wikipedia/commons/b/b4/Dirac_function_approximation.gif)

<b>Basis of $L_{2}(\mathbb{R})$</b> By convoluting a function $f$ with the Dirac delta function $\delta$, we obtain the function $f$ itself:

$$
(f*\delta)(x) = f(x)
$$

Intuitively we can think of the set of Diracs, as the basis of the $L^{2}(\mathbb{R})$ space:

$$f\approx \sum_{x}f(x)\delta_{x}$$

<i>Terminology:</i> We have used $\delta_{y}(x) = \delta(x-y)$

(NOT CLEAR YET FOR THE BASIS - SEE TRANSLATION ALSO)

#### Fourier transform
The Fourier Transform is an important image processing tool which is used to decompose an image into its sine and cosine components. The output of the transformation represents the image in the Fourier or frequency domain, while the input image is the spatial domain equivalent. In the Fourier domain image, each point represents a particular frequency contained in the spatial domain image.

The Fourier Transform is used in a wide range of applications, such as image analysis, image filtering, image reconstruction and image compression.

The Fourier transform of $f:\mathbb{R}\mapsto\mathbb{R}$ is defined as:

$$
\mathcal{F}(f)(\omega) = \hat{f}(\omega) = \int_{-\infty}^{\infty}f(x)e^{-i\omega x}dx
$$

where $e^{ix}$ is given by Euler's formula $e^{ix} = cos(x) + i\cdot sin(x)$.

The convolution theorem states that $\mathcal{F}(f*g)(\omega) = \hat{f}(\omega)\hat{g}(\omega)$

Notice that the eigenvectors of the convolution operator are the functions $e_{\omega}:x\mapsto e^{i\omega x}$ since:

$$
(f*e_{\omega})(x) = \int_{-\infty}^{\infty} f(u)e^{i\omega (x-u)}du = e^{i\omega x} \int_{-\infty}^{\infty} f(u)e^{-i\omega u}du = e^{i\omega x}\hat{f}\omega
$$

#### Frequency basis – layman’s terms

Fourier transform is invertible (under certain conditions), with its inverse given by:

$$
f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{f}(\omega) e^{i\omega x}d\omega
$$

Then, intuitively we can think of the set of complex exponential, as the basis of the $L_{2}(\mathbb{R})$ space (not precise notation!)

$$
f\approx \sum_{\omega}\hat{f}(\omega)e_{\omega}
$$

#### From continuous to discrete

How to deal with real life continuous signals in digital computers (inherently discrete representation)

We sample the signal with a certain time period T (the frequency is 1/T)

$$
f_{d}(x) = T\sum_{n=-\infty}^{\infty}f(nT)\delta_{nT}(x)
$$

Intuitively: $f(x) = lim_{T\rightarrow 0} f_{d}(x)$

Without loss of generality from now on we consider $T=1$

#### Finite signals and convolutions

The signal is not defined infinitely

• Padding: zero, wrap (circular), clamp, mirror

For Fourier circular is used to have periodicity but we will not pay attention to this(WTF).

#### Discrete Fourier Transform

• Finite signals of length N

$$
\hat{f}(k) = \sum_{n=0}^{N}f(n) e^{-\frac{2\pi i}{N}kn}
$$

Similar properties as in continuous (convolution theorem)

We have a true basis for discrete signals

$$
f = \sum_{n=0}^{N}\hat{f}(k)e_{k}, \ \text{with } e_{k}(n) = e^{\frac{2\pi i}{N}kn}
$$



## Fourier transforms and spatial frequencies in 2D

![prism](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1920,f_auto/A-dreamstime_1601578_t5w61h.jpg)

The <u>2D Fourier transform</u> is very similar than in the 1D case, excepts there are now two distinct axes on which the integral / sum operate. We define the FT pairs $(F, f)$:

$$
\begin{align}
F(u, v) &= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x, y)\ e^{-2\pi i (ux+vy)} dxdy\\

f(x, y) &= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} F(u, v)\ e^{2\pi i(ux+vy)}dudv
\end{align}
$$

where $u$ and $v$ are the <u>spatial frequencies</u>.  In general <u>complex</u>, we write $F(u, v)$ as:

$$F(u, v) = F_{R}(u, v) + i\cdot F_{I}(u, v)$$

with:
- <u>Magnitude spectrum:</u> $\mid F(u,v)\mid$ tells you how strong are the harmonics in an image
- <u>Phase angle spectrum: </u> $arctan(\frac{F_{I}}{F_{R}})$ phase spectrum tells where this harmonic lies in space.

<u>Conjugacy:</u>
<u>Symmetry:</u>

<b>Sinusoidal waves:</b> In 1D the Fourier transform is based on a decomposition into functions:

$$
e^{2\pi i(ux+vy)} = cos(2\pi(ux+vy)) + i sin(2\pi(ux+vy))
$$

The real and imaginary terms are sinusoids on the $x-y$ plance. The maxima and of $cos(2\pi(ux+vy))$ occur when:

$$
2\pi (ux+vy) = 2\pi \textbf{u}\cdot \textbf{x} = n\pi
$$

Then the maximas are the sets of equally spaced parallel lines with normal $u$ and wave-length $\frac{1}{\sqrt{u^{2} + v^{2}}}$

<b>Meaning:</b> To get some sense of what basis elements look like, we plot a basis element --- or rather, its real part --- as a function of $x$, $y$ for some fixed $u$, $v$. We get a function that is constant when $(ux+vy)$ is constant. The magnitude of the vector $(u, v)$ gives a frequency, and its direction gives an orientation. The function is a sinusoid with this frequency along the direction, and constant perpendicular to the direction.

![Image](/images/fourier_2D.png)

ADD IMAGE OF THE BASE

## The Convolution Theorem
• Applications to spatial filtering

## Sources

- [Difference convolution correlation](https://dsp.stackexchange.com/questions/27451/the-difference-between-convolution-and-cross-correlation-from-a-signal-analysis)
- [Dirac delta](http://www.med.harvard.edu/jpnm/physics/didactics/improc/intro/delta.html)
- [Dirac distribution](https://en.wikipedia.org/wiki/Dirac_delta_function)
- [Lecture notes](https://www.cc.gatech.edu/~afb/classes/CS4495-Fall2014/slides/CS4495-Frequency.pdf)
- [Lecture notes](https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.htm)
- https://dsp.stackexchange.com/questions/23325/compare-phase-and-magnitude-spectrum-results-of-2-images

<b>Questions:</b>
- Is the Dirac delta function used today in state of the art?
- Is it a specific case of the Fourier transform?
------
