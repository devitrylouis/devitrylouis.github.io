---
title: 'Hadoop'
date: 2019-01-12
permalink: /posts/2019/01/hadoop/
tags:
  - Big data
  - Hadoop
comments: true
---

Hadoop is a way to distribute very large files across multiple machines.
It uses the Hadoop Distributed File System (HDFS)
HDFS allows a user to work with large data sets
HDFS also duplicates blocks of data for fault tolerance
It also then uses MapReduce
MapReduce allows computations on that data

# HDFS

Let’s discuss the typical format of a distributed architecture that uses Hadoop

HDFS will use blocks of data, with a size of 128 MB by default
Each of these blocks is replicated 3 times
The blocks are distributed in a way to support fault tolerance

Smaller blocks provide more parallelization during processing
Multiple copies of a block prevent loss of data due to a failure of a node

MapReduce is a way of splitting a computation task to a distributed set of files (such as HDFS)
It consists of a Job Tracker and multiple Task Trackers

The Job Tracker sends code to run on the Task Trackers
The Task trackers allocate CPU and memory for the tasks and monitor the tasks on the worker nodes

What we covered can be thought of in two distinct parts:
Using HDFS to distribute large data sets
Using MapReduce to distribute a computational task to a distributed data set
Next we will learn about the latest technology in this space known as Spark.
Spark improves on the concepts of using distribution


------
