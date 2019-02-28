---
title: 'Gabor filters'
date: 2018-12-01
permalink: /posts/2019/02/vic-gabor-filters/
tags:
  - Visual computing
---

In image processing, aa Gabor filter, (Dennis Gabor) is a linear filter used for texture analysis.

> <b>What is its purpose?</b> Analyzing whether there are any specific frequency content in the image in specific directions in a localized region around the point or region of analysis.

> <b>What is texture analysis?</b> Texture analysis refers to the characterization of regions in an image by their texture content. Texture analysis attempts to quantify intuitive qualities described by terms such as rough, smooth, silky, or bumpy as a function of the spatial variation in pixel intensities.

> <b>Motivated by human perception:</b> Frequency and orientation representations of Gabor filters are claimed by many contemporary vision scientists to be similar to those of the human visual system, though there is no empirical evidence and no functional rationale to support the idea. They have been found to be particularly appropriate for texture representation and discrimination. In the spatial domain, a 2D Gabor filter is a Gaussian kernel function modulated by a sinusoidal plane wave.

## 1. Formal definition

<b>TL; DR:</b> Gabor filter is nothing more complicated than a Gaussian modulated by a sinusoid.

Equation: this is the equation for a 2d Gabor filter as you can see it is comprised of a Gaussian kernel multiplied by sinusoid also as you would expect the frequency response is nothing more than two Gaussian pulses corresponding to the modulating sinusoid.

Its impulse response is defined by a sinusoidal wave (a plane wave for 2D Gabor filters) multiplied by a Gaussian function.

Because of the multiplication-convolution property (Convolution theorem), the Fourier transform of a Gabor filter's impulse response is the convolution of the Fourier transform of the harmonic function (sinusoidal function) and the Fourier transform of the Gaussian function. The filter has a real and an imaginary component representing orthogonal directions.

$$
g(x, y; \lambda, \theta, \psi, \sigma, \gamma) = \text{exp}\big(-\frac{x^{'2}}{} big)
$$

In this equation, {\displaystyle \lambda } \lambda  represents the wavelength of the sinusoidal factor, {\displaystyle \theta } \theta  represents the orientation of the normal to the parallel stripes of a Gabor function, {\displaystyle \psi } \psi  is the phase offset, {\displaystyle \sigma } \sigma  is the sigma/standard deviation of the Gaussian envelope and {\displaystyle \gamma } \gamma  is the spatial aspect ratio, and specifies the ellipticity of the support of the Gabor function.

#


------
