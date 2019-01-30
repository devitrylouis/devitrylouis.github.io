---
title: 'Low-level vision framework'
date: 2018-12-01
permalink: /posts/2019/01/vic-low-level/
tags:
  - Visual computing
---

The goal of this article is to provide a Mathematical framework for the model of images. Specifically, we will recall the use of some operators (convolutions, correlation and cross-correlation) in signal processing. Then, we will define two approaches for expressing our image into a desirable signal, namely the Dirac delta function and the 2D Fourier transform. In the process, we will define in-depth the 2D Fourier transform and define a

Most notably, we are interested in finding convenient basis of the space, for which there are two main approaches:
- <u>Spatial basis</u> which is suited for pixel like input and is built upon the Dirac Delta delta function.
- <u>Frequency basis</u> brought by the 2D Fourier transform, this basis has several advantages (frequency instead of space).

This framework is motivated by the fact that images are finite and with compact support, so they behave well mathematically and most properties hold for them.

## Mathematical reminder - the 1D case

In this section, we will review some mathematical concepts (convolution-like operations, $L_{2}$ space) and we will see why we can restrict ourselves to a discrete context.

### Convolution, correlation, autocorrelation

Three common problems in signal processing are important enough to motivate this reminder:

<b>1. For an input signal $f$, what is the output of a filter with impulse response $g(t)$? </b>

The answer is given by the convolution $f(t) * g(t)$. Mathematically, the <u>convolution</u> is an <u>operation</u> on two functions $f$ and $g$ which produce a third function $f * g$ that <b>expresses how the shape of one is modified by the other</b>.

$$
(f * g)(x) = \int_{-\infty}^{\infty} f(u)g(x-u)du
$$

<b>2. Given a noisy signal $f(t)$, is the signal $g(t)$ somehow present in $f(t)$? </b>

In other words, is $f(t)$ of the form $g(t)+n(t)$, with $n(t)$ is noise? The answer can be found by the <u>correlation</u> of $f(t)$ and $g(t)$. If the <b>correlation is large</b>, then we may be confident in saying that <b>the answer is yes</b>.

$$
(f\otimes g)(x) = \int_{-\infty}^{\infty} f(u)g(x+u)du
$$

<b>3. Is there any periodicity / repeating patterns in a noisy signal $f(t)$?</b>

<u>Autocorrelation</u>, also known as serial correlation, is the <u>correlation of a signal</u> with a <u>delayed copy of itself</u> as a <u>function of the delay</u>. Informally, it is the similarity between observations as a function of the time lag $x$ between them. The analysis of autocorrelation is a mathematical tool for <b>finding repeating patterns</b>, such as the <b>presence of a periodic signal obscured by noise</b>.

$$
(f\otimes f)(x) = \int_{-\infty}^{\infty} f(u)f(x+u)du
$$

These operations are convenient to deal with because of its inherent properties:

| Linearity | Associativity |
|:-----------------------------------------------------:|:--------------------------------:|
| $f * (g+h) = f * g + f * h$ | $(f * g) * h = f * (g * h)$ |
| $(f+g) * h = f * h + g * h$ | <b>Commutativity (convolution only)</b> |
| $\lambda (f * g) = (\lambda f) * g = f * (\lambda g)$ | $f * g = g * f$ |

We will use these operations in 2D. The principles To understand how these operation work, I suggest seeing this illustration in detail:

![convolution_correlation](https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Comparison_convolution_correlation.svg/400px-Comparison_convolution_correlation.svg.png)

Now that we have defined the operators above, we will dive in their properties with respect to the <u>space of functions</u> they handle, namely:

$$ L^{2}(\mathbb{R}) = \{ f:\mathbb{R}\mapsto \mathbb{R} \text{ such that } \mid\mid f \mid\mid_{\mathcal{L}_{2}} < \infty \} $$

where the $\mid\mid \cdot \mid\mid_{\mathcal{L}_{2}}$ is the norm corresponding to the following <u>dot product</u>:

$$
\langle f ,\ g\rangle = \int_{-\infty}^{-\infty} f(x)g(x)dx
$$

### Fourier transform and the convolution theorem

The [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform) is very popular when it comes to dealing with signal because it provides a "bridge" <u>between time</u> and <u>frequency domain</u>.

![Image](/images/time_freq.png)

It is furthermore empowered by the <b>convolution theorem</b>, which states that this "bridge" <b>preserves the convolution operation</b>:

$$\mathcal{F}(f*g)(\omega) = \hat{f}(\omega)\hat{g}(\omega), \text{ for } f, g \in L_{2}(\mathbb{R}) $$

where the Fourier transform of $f:\mathbb{R}\mapsto\mathbb{R}$ is defined as:

$$
\mathcal{F}(f)(\omega) = \hat{f}(\omega) = \int_{-\infty}^{\infty}f(x)e^{-i\omega x}dx \text{ , with }e^{ix} = cos(x) + i\cdot sin(x)
$$

### A frequency basis

Notice that the <b>eigenvectors</b> of the <b>convolution operator</b> are the functions $e_{\omega}:x\mapsto e^{i\omega x}$ since:

$$
\begin{align}
(f*e_{\omega})(x) &= \int_{-\infty}^{\infty} f(u)e^{i\omega (x-u)}du \\
&= e^{i\omega x} \int_{-\infty}^{\infty} f(u)e^{-i\omega u}du \\
&= e^{i\omega x}\hat{f}(\omega)\\
\end{align}
$$

Since the <u>Fourier transform</u> is <u>invertible</u> (under certain conditions), with its inverse given by:

$$
f(x)=\frac{1}{2\pi}\sum_{-\infty}^{\infty}\hat{f}(\omega) e^{i\omega x}d\omega
$$

we can think of the set of complex exponential, as some basis of the $L_{2}(\mathbb{R})$ space:

$$
f\approx \sum_{\omega}\hat{f}(\omega)e_{\omega}
$$

<i>Note:</i> The equation above is not rigorous for the continuous case.

However, if we consider finite signals of length $N$

$$
\hat{f}(k) = \sum_{n=0}^{N}f(n) e^{-\frac{2\pi i}{N}kn}
$$

it turns out that it satisfies the <u>same properties</u> than its <u>continuous couterpart</u>, but can additionally provide a <b>true basis for discrete signals</b>:
$$
f = \sum_{n=0}^{N}\hat{f}(k)e_{k}(n), \ \text{with } e_{k}(n) = e^{\frac{2\pi i}{N}kn}
$$

### From continuous to discrete

As <u>computers</u> are fundamentally <u>limited to discrete representation</u>, we <u>sample</u> real life <u>continuous signals</u> with a certain time period $T$ (the frequency is $1/T$):

$$
f_{T}(x) = T\sum_{n=-\infty}^{\infty}f(nT)\delta_{nT}(x)
$$

Consequently, the higher the period, the closer our discrete representation is from the real signal:

$$f(x) = lim_{T\rightarrow 0} f_{T}(x)$$

This discrete representation is actually rather convenient, because <b>images are finite</b> and with <b>compact support</b>. It is notably <b>suited</b> for <b>padding zones, wrap, clamp and mirrors</b>.

Without loss of generality, we consider $T=1$ to lighten the equations.

## Fourier transform of an image

The Fourier Transform is an <b>important image processing tool</b> which is used to <u>decompose an image into its sine and cosine components</u>.

The <u>output</u> of the transformation represents the <u>image in the frequency domain</u>, while the <u>input image</u> is the <u>spatial domain</u> equivalent. In the Fourier domain image, each point represents a particular frequency contained in the spatial domain image:

![Image](/images/fourier_transform_image.png)

The Fourier Transform is used in a wide range of applications, such as <b>image analysis</b>, <b>image filtering</b>, <b>image reconstruction</b> and <b>image compression</b>.

### Spatial basis: Dirac delta

In vision computing, <u>Dirac delta</u> helps <u>measure</u> the device's response to <u>as simple an input as possible</u> (i.e. a pixel):

![Image](/images/dirac_function.png)

Mathematically, this ideal input is reffered to as the <u>Dirac delta function</u>. It is defined as the limit (in the sense of distributions) of the sequence of zero-centered normal distributions:

$$
\delta(x) = \text{lim}_{a\rightarrow 0} \frac{1}{\mid a \mid \sqrt{\pi}}e^{-(x/a)^{2}}= \begin{cases}
\infty \text{ if x = 0}\\
0 \text{ otherwise}
\end{cases}
$$

Although it can be rigorously defined as a measure (thereby satisfying $\sum_{-\infty}^{\infty}\delta(x)dx=1$), no such function exists. It is nonetheless very useful for approximating functions whose graphical representation is in the shape of a narrow spear:


![Dirac distribution](https://upload.wikimedia.org/wikipedia/commons/b/b4/Dirac_function_approximation.gif)

<b>Basis of $L_{2}(\mathbb{R})$</b> By convoluting a function $f$ with the Dirac delta function $\delta$, we obtain the function $f$ itself:

$$
(f*\delta)(x) = f(x)
$$

Intuitively we can think of the set of Diracs, as the basis of the $L^{2}(\mathbb{R})$ space:

$$f\approx \sum_{x}f(x)\delta_{x}$$

<i>Terminology:</i> We have used $\delta_{y}(x) = \delta(x-y)$

(NOT CLEAR YET FOR THE BASIS - SEE TRANSLATION ALSO)

### Fourier transforms

![prism](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1920,f_auto/A-dreamstime_1601578_t5w61h.jpg)

The <u>2D Fourier transform</u> is very similar than in the 1D case, excepts there are now two distinct axes on which the integral / sum operate. We define the FT pairs $(F, f)$ as:

$$
\begin{align}
F(u, v) &= \sum_{x = -\infty}^{\infty}\sum_{y = -\infty}^{\infty} f(x, y) e^{-2\pi i (ux+vy)}\\
f(x, y) &= \sum_{u = -\infty}^{\infty}\sum_{v = -\infty}^{\infty} F(u, v) e^{2\pi i(ux+vy)}
\end{align}
$$

where $u$ and $v$ are the <u>spatial frequencies</u>.  In general <u>complex</u>, we write $F(u, v)$ as:

$$F(u, v) = F_{R}(u, v) + i\cdot F_{I}(u, v)$$

with:
- <u>Magnitude spectrum:</u> $\mid F(u,v)\mid$ tells you how strong are the harmonics in an image
- <u>Phase angle spectrum: </u> $arctan(\frac{F_{I}}{F_{R}})$ phase spectrum tells where this harmonic lies in space.

### Frequency basis

Just like in the 1D discrete case, we can construct a true frequency basis, composed of "sinusoidal waves" (each with fixed $u, v$):

$$
e^{2\pi i(ux+vy)} = cos(2\pi(ux+vy)) + i\cdot sin(2\pi(ux+vy))
$$

<i>Note:</i> The term sinusoidal waves is used because the real and imaginary terms are sinusoids on the $x-y$ plane. To get this right, consider the following argument:

<b>Basis shape?</b> For a given $\textbf{u} = (u, v)$, the maxima $\textbf{x} = (x, y)$ of the real part occur when $2\pi \textbf{u}\cdot \textbf{x} = n\pi$. This imply that the maximas are sets of equally spaced parallel lines with normal $u$ and wave-length $\frac{1}{\sqrt{u^{2} + v^{2}}}$

<b>Meaning:</b> To get some sense of what basis elements look like, we plot some basis element - or rather, their real part - as a function of $x$, $y$ for some fixed $u$, $v$. We get a function that is constant when $(ux+vy)$ is constant. The magnitude of the vector $(u, v)$ gives a frequency, and its direction gives an orientation. The function is a sinusoid with this frequency along the direction, and constant perpendicular to the direction.

![Image](/images/fourier_2D_basis.png)

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
