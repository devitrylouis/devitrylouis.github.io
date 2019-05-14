---
title: 'Filters'
date: 2018-12-01
permalink: /posts/2019/01/vic-filters/
tags:
  - Visual computing
---

Given a camera and a still scene, how would you proceed to reduce noise in an image? Well, taking lots of pictures and averaging them should do the trick! But most of the time in computer vision, we don't have access to several images but one. And because the image formation process that produced a particular image largely depends on several factors (lighting conditions, scene geometry, surface properties, camera optics) perturbations arise in the image and need to be adressed.

More generally, we use filters in computer vision to handle key tasks such as:

- Enhance an image (denoise, resize.)
- Extract information (texture, edges.)
- Detect patterns (template matching.)

Although the <b>key principle of filters</b> is to <u>modify the pixels</u> in an image based on <u>some function of a local neighborhood</u> of each pixel, their structural properties vary stronly.

In this blogpost, we will cover the three categories below:

| Linear Filtering | Non-Linear Filtering | Morphological Filtering |
|:----------------:|:--------------------:|:-----------------------:|
| Average | Mean | Binary opening |
| Gaussian | Bilateral | Binary closing |
|  | Non-local mean | Region Filling |

More specifically, here is the outline of this review:

1. [Linear Filtering](#linear)

    * [Smoothing](#smoothing)

    * [Filtering and edge detection](#edge)

        - [Sobel filter](#sobel)
        - [Laplacian Filter](#laplacian)

    * [Practical implementation](#practical)

        - [Spatial and frequency domain](#spatial)
        - [Separability](#separability)

2. [Non-Linear Filtering](#non_linear)

    * [Median filtering](#median)
    * [Bilateral filtering](#bilateral)
    * [Equations](#equations)
    * [Non-local mean](#non_local_mean)

3. [Morphological filtering](#morphological)

4. [Sources](#sources)

## 1. Linear Filtering <a name="linear"></a>

For a given image $F$, obtaining its linearly filtered image $G$ actually boils down to plain and simple convolution with a kernel $H$:

$$H*F = G$$

Below is an animated illustration of this principle with a sharpen kernel $H$.

![GIF kernel](https://i.stack.imgur.com/9OZKF.gif)

<b>Edge handling:</b> As one can see above, $0$s were added on the border of the image. This technique called <u>padding</u> and is meant to solve a basic shortcoming: kernel convolution usually requires values from pixels outside of the image boundaries. While there is a variety of methods to handle edges, the [most common](https://en.wikipedia.org/wiki/Kernel_(image_processing)#Edge_Handling) are extend, wrap, mirror and crop.

To ensure the average pixel in the processed image is as bright as the average pixel in the original image, the kernel is typically normalized: the sum of the elements of a kernel is one.

There are [several types of kernel](https://en.wikipedia.org/wiki/Kernel_(image_processing)#Details), each suited for a specific purpose (blurring, edge detection, sharpening...). Among these ones, we will solely focus on smoothing and edge detection.

<i>Note:</i> For a fixed type of kernel, one can adjust its size.

### 1.1. Smoothing <a name="smoothing"></a>

Among kernels designed for smoothing, the most basics one are the linear and the gaussian filter, defined below.

<b>Average filter:</b> This filter gives equal importance to the neighbors of a particular point:

$$ \frac{1}{9} \begin{bmatrix} 1 & 1 & 1\\ 1 & 1 & 1\\ 1 & 1 & 1 \end{bmatrix} $$

<b>Gaussian filter:</b> This filter removes high-frequency components from the image by assigning larger weights to closer pixel neighbors:

$$ \frac{1}{16} \begin{bmatrix} 1 & 2 & 1\\ 2 & 4 & 2\\ 1 & 2 & 1 \end{bmatrix} $$

More precisely, the elements of the Gaussian kernel $H_{\sigma}$ are given by:

$$ h_{\sigma}(u, v) = \frac{1}{2\pi \sigma^{2}} e^{-\frac{u^{2} + v^{2}}{\sigma^{2}}} $$

where $\sigma$ is the variance of the Gaussian and determines extent of smoothing and the amount of smoothing is proportional to the mask size: the higher the variance, the more blurred is the image.

In the plot below, we can witness the effects of these filters on the image and their corresponding frequencies.

![Gaussian vs linear](/images/vic_gaussian_vs_linear.png)

### 1.2. Filtering and edge detection <a name="edge"></a>

High pass filters are the basis for most sharpening and edge detection methods. The end result is an image for which the contrast is enhanced between adjoining areas with little variation in brightness or darkness. To measure those variations, we use image "derivatives":

| First order derivative | Second order derivative |
|:---------------------------------------------------:|:------------------------------------------------------------:|
| $\frac{\partial f}{\partial x} = f(x+1) - f(x)$ | $\frac{\partial f}{\partial x} = f(x+1)- f(x-1) - 2f(x)$ |

which work as depicted in the diagram below:

![Derivatives of images](https://i.stack.imgur.com/r2bUi.png)

When it comes to find edges, the derivatives can actually be modelled by specific kernels, therefore being linear filters. The most popular kernels are the <u>Sobel kernel</u> and the <u>Laplacian kernel</u>.

#### 1.2.1. Sobel filter <a name="sobel"></a>

The <u>Sobel fitler</u> is a popular technique in computer vision which is heavily used within edge detection algorithms, where <u>it creates an image emphasising edges</u>.

At each point in the image, the result of the Sobel–Feldman operator is either the corresponding gradient vector or the norm of this vector.

$$ S_{1} = \begin{pmatrix}
-1 & -2 & -1\\
0 & 0 & 0\\
1 & 2 & 1
\end{pmatrix} $$

The gradient approximation that it produces is relatively crude, in particular for high-frequency variations in the image. Then the magnitude and the direction are given by:

| Edge magnitude | Edge direction |
|:------------------------------:|:-------------------------------:|
| $\sqrt{S_{1}^{2} + S_{2}^{2}}$ | $tan^{-1}(\frac{S_{1}}{S_{2}})$ |

![Sobel](/images/vic_sobel.png)

#### 1.2.2. Laplacian Filter <a name="laplacian"></a>

The Laplacian of an image highlights regions of rapid intensity change and is therefore often used for edge detection (see [zero crossing edge detectors](https://homepages.inf.ed.ac.uk/rbf/HIPR2/zeros.htm)). However, the raw image is often noisy and this is problematic for the sensitive second derivatives. To solve this issue, the Laplacian is often computed on top of the Gaussian blurred image.

The Laplacian is often applied to an image that has first been smoothed with something approximating a Gaussian smoothing filter in order to reduce its sensitivity to noise.

The Laplacian can be calculated using a convolution filter and since the input image is discrete, we find a kernel that approximates the definition in the discrete case. Two commonly used small kernels are shown below:

$$
\begin{pmatrix}
0 & -1 & 0\\
0 & 4 & -1\\
0 & -1 & 0
\end{pmatrix}
\text{ or }
\begin{pmatrix}
-1 & -1 & -1\\
-1 & 8 & -1\\
-1 & -1 & -1
\end{pmatrix}
$$

![Laplacian](/images/vic_laplacian.png)

### 1.3. Practical implementation <a name="practical"></a>

#### 1.3.1. Spatial and frequency domain <a name="spatial"></a>

They have the advantage can be applied to both spatial and frequency domain:

| Spatial domain | Frequency domain |
|:--------------:|:-------------------------------------------------------:|
| $G = H * F$ | $G = \mathcal{F}^{—1}(\mathcal{F}(H) * \mathcal{F}(F))$ |

#### 1.3.2. Separability <a name="separability"></a>

The process of performing a convolution requires $K^{2}$ operations per pixel, where $K$ is the size (width or height) of the convolution kernel. In many cases, this operation can be significantly speed up by first performing a $1D$ horizontal convolution followed by a $1D$ vertical convolution, requiring $2K$ operations. If this is possible, then the <u>convolution kernel is called separable</u>. And it is the outer product of two kernels

$$K = v\cdot h^{T}$$

<b>Theorem:</b> If $H$ has a unique non-zero eigenvalue, then its corresponding kernel is separable.

## 2. Non-Linear Filtering <a name="non_linear"></a>

### 2.1. Median filtering <a name="median"></a>

A <u>median filter</u> operates over a window by selecting the median intensity in the window.

Although it is robust to outliers, it is ill-suited for Gaussian noise. In consequence, we often use a variant called $\alpha$-trimmed mean, which averages together all of the pixels except for the $\alpha$
fraction that are the smallest and the largest.

<i>Implementation note:</i> Both versions gets slower with large windows.

### 2.2. Bilateral filtering <a name="bilateral"></a>

While Gaussian smoothing is good when it comes to remove details, it also remove edges. To tackle this issue, we use bilateral filtering which only average with similar intensity values.

### 2.3. Equations <a name="equations"></a>

- Gaussian smoothing:
$$
G[I]_{p} = \sum_{q}G_{\sigma_{S}}(p-q)\times I_{q}
$$

- Bilateral filter:
$$
BF[I]_{p} = \frac{1}{W_{p}}\sum_{q}G_{\sigma_{S}}(p-q) \times G_\sigma_{R}(I_{p} - I_{q})\times I_{q}
$$

where the middlemost term takes time to compute:
- Depends from the image value at each pixel: cannot easily be pre-computed, no Fourier transform
- Slow to compute

Bilateral filter for denoising: BF suppresses high frequency low contrast texture but preserve edges

### 2.4. Non-local mean <a name="non_local_mean"></a>

Images textures are self repetitive
Filters using pixems that have a similar intensity value and which neighbors also have a similar value: can be seen as an extension of the Bilateral Filter:

$$
NLM[I]_{p} = \frac{1}{W_{p}} \sum_{q} G_{\sigma_{R}} \big( \sum_{r}G_{\sigma_{P}}(r)(I_{p+r} - I_{q+r})^{2} /big)
$$

Basis for state of the art denoising

## 3. Morphological filtering <a name="morphological"></a>

To be written soon; stay tuned!

## 4. Sources <a name="frequency_basis_2"></a>

- [Sobel operator](https://en.wikipedia.org/wiki/Sobel_operator)
- [Lecture notes of Raquel Urtasun](https://www.cs.toronto.edu/~urtasun/courses/CV/lecture02.pdf)
- [What does the kernel size mean?](https://stats.stackexchange.com/questions/296679/what-does-kernel-size-mean)
- [Laplacian](https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm)

------
