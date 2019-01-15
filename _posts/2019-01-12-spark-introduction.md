---
title: 'Spark introduction'
date: 2019-01-12
permalink: /posts/2019/01/spark-introduction/
tags:
  - Big data
  - Spark
comments: true
---

This lecture will be an abstract overview, we will discuss:
- Spark
- Spark vs MapReduce
- Spark RDDs
- Spark DataFrames

Spark is an Apache open source project created at the AMPLab at UC Berkeley (2013). It has exploded in popularity due to it’s ease of use and speed. Since then, it is one of the latest technologies being used to quickly and easily handle Big Data

Contrary to MapReduce requires files to be stored in HDFS, Spark does not!
Therefore, Spark also can perform operations up to 100x faster than MapReduce.

<b>Speed of Spark vs Hadoop:</b>
- MapReduce writes most data to disk after each map and reduce operation
- Spark keeps most of the data in memory after each transformation and spill over to disk if the memory is filled.

At the core of Spark is the idea of a Resilient Distributed Dataset (RDD), which has four main features:
- Distributed Collection of Data
- Fault-tolerant
- Parallel operation - partioned
- Ability to use many data sources

## Spark RDDs

- RDDs are immutable, lazily evaluated, and cacheable
- There are two types of Spark operations:
    * Transformations
    * Actions
- Transformations are basically a recipe to follow.
- Actions actually perform what the recipe says to do and returns something back.

When discussing Spark syntax you will see RDD versus DataFrame syntax show up.
With the release of Spark 2.0, Spark is moving towards a DataFrame based syntax, but keep in mind that the way files are being distributed can still be thought of as RDDs, it is just the typed out syntax that is changing

## Spark DataFrames

When discussing Spark syntax you will see RDD versus DataFrame syntax show up.
With the release of Spark 2.0, Spark is moving towards a DataFrame based syntax, but keep in mind that the way files are being distributed can still be thought of as RDDs, it is just the typed out syntax that is changing





- What is “Big Data”?
- Explanation of Hadoop, MapReduce,and Spark
- Local versus Distributed Systems
- Overview of Hadoop Ecosystem
- Overview of Spark

------
