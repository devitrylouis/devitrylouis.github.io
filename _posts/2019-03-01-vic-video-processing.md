---
title: 'First order scattering transform'
date: 2018-12-01
permalink: /posts/2019/02/vic-videoo-processing/
tags:
  - Visual computing
---

## 1. Introduction

The big challenges of action recognition (variations in class, pose and appearance, occlusion and lightning) requires to design good features for video processing. Some comonly used ones are:
- Space time interest points
- Dense Trajectories
- Body joints
- Motion history images

Historically, these features are fed into an effective Machine Learning classifier (linear SVM being a popular choice)!

## 2. Action Recognition

There are different level of semantics to characterize what an action is:
- Action "Walking"
- Activity "Walking on grass"
- Event "A soccer game"

### 2.1. History Images

<b>Temporal Templates</b> Idea: summarize motion in video in a Mo on History Image (MHI):
A.F. Bobick et al., 2001, “The Recogni on of Human • Movement Using Temporal Templates”, PAMI 2001

Compute MHI for each ac on sequence.
• Describe each sequence with Hu descrip on, [Hu M. IEEE Transac on on Informa on Theory, 1962]
• Use Nearest Neighbor ac on classi ca on with Mahalanobis distance between training and test descriptors d.

<i>Dataset:</i> Aerobics Dataset.
1. Advantages = Simple + Fast
2. Disadvantages =
  - Static camera and background
  - Sensitive to segmenta on errors
  - Silhouettes do not capture interior motion / shape

### 2.2. Spatio-Temporal Features

A good idea is to extract features corresponding to space-time interest points.
-


A useful and e ec ve approach is to extract local features as space- me interest points and encode the temporal informa on directly into the local feature. This results into the de ni on of spa o-temporal local features that embed space and  me jointly.
 Videos are considered as volumes of pixels.
 Spa o-temporal features are located at spa o-temporal salient points that are
extracted with interest point operators.
 Similarly as for the 2D case, interest point structures are searched for that are stable under rota on, viewpoint, scale and illumina on changes.
• Space  me interest point detectors are extensions of 2D interest point detectors that incorporate temporal informa on.

Most popular soluions
 Detectors:
 STIP Spa o Temporal Interest Points (Harris3D) [I. Laptev, IJCV 2005]  Dollar’s detector [P. Dollar et al., VS-PETS 2005]
 Hessian3D [G. Willems et al., ECCV 2008]
 Descriptors:
 HOG/HOF [I. Laptev et al., CVPR 2008]
 Dollar [P. Dollar et al., VS-PETS 2005]
 HoG3D [A. Klaeser et al., BMVC 2008]
 Extended SURF [G. Willems et al., ECCV 2008]

<b>STIP: Spatio Temporal Interest Points Detecto</b>

<b>STIP Summar</b>

<b>Dollar’s periodic motion detector</b>

<b>Importance of multiple scales</b>

<b>Descriptors for spatio-temporal patches</b>

<b>3D HoG</b>

<b>Action Recognition</b>

### 2.3. Dense Trajectories



## 3. Object/ Action Detection
    * Frame level
## 4. Applications
    * Vehicle Tracking
    * Kinect
