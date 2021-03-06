---
title: 'Word embeddings'
date: 2018-12-01
permalink: /posts/2019/01/bag-of-words/
tags:
  - Deep Learning
  - NLP
---
Goal: Use word embeddings to embed larger chunks of text!

# Background: TF-IDF

- Set of documents: $d_{1}, d_{2},...,d_{n}$
- Set of labels: $y_{1}, y_{2},...,y_{n} \forall i, y_{i} \in [1,...,C]$

<b>Example:</b> sentiment analysis (SST), movie review (IMDB), document classification (Reuters)

How do we get features for documents of text?

# Document-term matrix

Matrix whose columns are the words (word embedding) and the rows are the documents (document embedding). The document-term matrix is a sparse matrix of size n x V.

# Term Frequency – Inverse Document Frequency (TF-IDF)

Words that appear only in a few documents contain more discriminative information

<b>Example:</b> if “Obama” appears in 10 documents out of 10000,
these documents will likely be related to politics.

$$
tf-idf_{i, j} = tf_{i, j} idf_{i, j}
$$

Typically, the tf-idf weight is composed by two terms: the first computes the normalized Term Frequency (TF), aka. the number of times a word appears in a document, divided by the total number of words in that document; the second term is the Inverse Document Frequency (IDF), computed as the logarithm of the number of the documents in the corpus divided by the number of documents where the specific term appears.

<b>Term Frequency (TF)</b>, which measures how frequently a term occurs in a document. Since every document is different in length, it is possible that a term would appear much more times in long documents than shorter ones. Thus, the term frequency is often divided by the document length (aka. the total number of terms in the document) as a way of normalization:

$$tf_{i, j} = \frac{\mid \{ i: y_{i} \in d_{j} \}}{\#d_{j}}$$

<b>Inverse Document Frequency</b> measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following:

$$
idf_{j} = log_{e}\frac{\#D}{\{ d_{i}: t_{j} \in d_{i} \} }
$$

which is the total number of documents divided by the number of documents with term $t_{j}$ in the document.

# Document classifiation

## Latent Semantic Analysis (LSA)

1. Create TF-IDF matrix $(\#documents, \#words)$
2. Perform PCA to reduce the dimension $(\#document, p)$
3. Learn a classifier (Logistic Regression, SVM, Random Forest, MLP)

<b>Note:</b> requires many documents to get decent representations little modelling of interaction between words.

## Transfer Learning – pretrained word vectors

<u>1. Learn word embeddings on a huge unsupervised corpus (e.g. Wikipedia)</u>

To deal with word2vec, refer to [this post](https://devitrylouis.github.io/posts/2019/01/embeddings/) (code included).

<u>2. Embed documents using the (weighted) average of word embeddings</u>

```python
class BoV():
    def __init__(self, w2v, sentences):
        self.w2v = w2v
        self.encode(sentences)

    def encode(self, sentences):
        # Compute IDFs and set list of embeddings
        self.idfs = s2v.build_idf(sentences)
        sentemb_idf = []

        # Sequential encoding
        for sent in sentences:
            # Split and filter the sentences
            splitted_sent = sent.split(' ')
            splitted_sent = filter(bool, splitted_sent)

            # Word2vec
            embeddings = map(lambda x: w2v.assign_w2v(x), splitted_sent)
            dict_embeddings = dict(zip(splitted_sent, embeddings))

            # There are words in sentences missing in word2vec files
            # The next lines of code take care of this by removing useless keys
            valid_embeddings = {k:v for k, v in dict_embeddings.iteritems() if v is not None}
            valid_idfs = {k:v for k,v in idfs.iteritems() if k in valid_embeddings.keys()}
            list_embeddings = list(valid_embeddings.values())
            array_idfs = np.array(valid_idfs.values())

            # Handling error for empty sentences
            if len(list_embeddings) in [0] or list_embeddings is None:
                sentemb_idf.append(None)
            else:
                # Idf-weighted mean of word vectors
                sentemb_idf.append(np.average(np.vstack(list_embeddings), weights = array_idfs, axis = 0))

        self.embeddings_idf = dict(zip(sentences, sentemb_idf))

    def most_similar(self, s, sentences, idf=False, K=5):
        # Get most similar sentences and **print** them
        similarities = {s: self.score(s, sent, idf) for sent in sentences}
        print(sorted(similarities, key=similarities.get, reverse=True)[-K:])

    def cosine_similarity(self, s, r, idf=False):
        # Cosine similarity
        dot_product = np.dot(self.embeddings_idf[s], self.embeddings_idf[r])
        normalizer = np.linalg.norm(self.embeddings_idf[s]) * np.linalg.norm(self.embeddings_idf[r])
        return(dot_product/float(normalizer))

    def build_idf(self, sentences):
        # Build the idf dictionary: associate each word to its idf value
        idf = {}
        idf = dict.fromkeys(set(' '.join(sentences).split()), 1)

        # Iterate other words in all sentences (suboptimal)
        for sent in sentences:
            for w in sent.split(' '):
                if w != "":
                    idf[w] += 1

        idfs = {k:max(1, np.log10(len(sentences) / float(v))) for k, v in idf.items()}

        return idfs
```

<u>3. Learn a classifier (Logistic Regression, SVM, Random Forest, MLP)</u>

<b>Note:</b> This can work because in high dimension, the average of word vectors is a vector that is close to all its components (preservation of the information of each word).

<b>Practical advice:</b>
- <u>Pre-trained</u>: Learn an encoder on an external task and only learn a classifier on top of this representation for your task (which is called transfer learning)
- <u>Learn jointly</u> the “encoder” and the ”classifier” on your task

<b>Example:</b>
Learning a ConvNet on ImageNet and transferring it
Learning word embeddings on a Common Crawl and transferring it

<b>FastText</b> is an open-source tool that provides:
- a fast and easy-to-use text classification tool (based on bag-of-words)
- a fast algorithm to learn word embeddings (char-based word2vec)

<b>Drawbacks:</b> Bag-of-words are rather limited (word order, context, …)

The goal in the next articles is to capture more structure by framing the input as a sequence.

<b>Sources:</b>
- [TF-IDF website](http://www.tfidf.com/)
- K. Sparck Jones. "A statistical interpretation of term specificity and its application in retrieval". Journal of Documentation, 28 (1). 1972.
- G. Salton and Edward Fox and Wu Harry Wu. "Extended Boolean information retrieval". Communications of the ACM, 26 (11). 1983.
- G. Salton and M. J. McGill. "Introduction to modern information retrieval". 1983
- G. Salton and C. Buckley. "Term-weighting approaches in automatic text retrieval". Information Processing & Management, 24 (5). 1988.
- H. Wu and R. Luk and K. Wong and K. Kwok. "Interpreting TF-IDF term weights as making relevance decisions". ACM Transactions on Information Systems, 26 (3). 2008.

------
