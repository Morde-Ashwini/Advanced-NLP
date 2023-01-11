
# Overview

Sentiment analysis (or opinion mining) is a natural language processing (NLP) technique used to determine whether data is positive, negative or neutral. Project that I developed uses sentiment 140 dataset from kaggle. I have used different techniques to clear the text from dataset, trained the model, got the accuracy, precision, f1-score for the model. To do all this I have used python programming language and diffenet libraries that help built different functionality. Please find the google collab link attached.

# Data
For training purpose, Sentiment140 dataset with 1.6 million tweets is used.

Csv file has been downloaded from Kaggle:
https://www.kaggle.com/datasets/kazanova/sentiment140?resource=download&select=training.160000
0.processed.noemoticon.csv


# Installation & Usage

1)Copy this link https://colab.research.google.com/drive/1UTm7U31gx9JVo1ixXlXANDLpGuRnzlS6?authuser=1#scrollTo=hSEyUJUdPobn and paste it on your browser.
2)A google colab notebook will open.
3)Sign in if necessary
4)Once it is open Click on ->> Runtime ->> Run All
5)All the dependencies required are present in the code.
6)The data is also present in the included folder.
7)Wait for the full notebook to finish executing.
8)Check the graph and the accuracy and loss of the model.

# Method 

Bert for word embedding
LSTM
Adam optimizer, binary cross entropy loss

# Results

![image](https://user-images.githubusercontent.com/122468278/211859060-7db3118b-cf3e-428f-b2a3-75753fab9fc4.png)

![image](https://user-images.githubusercontent.com/122468278/211859080-7642d5f4-0636-407c-9ce1-48b595aa81c2.png)

![image](https://user-images.githubusercontent.com/122468278/211859115-3f2de951-eb22-41f0-90c2-fa940dd99491.png)

![image](https://user-images.githubusercontent.com/122468278/211859167-cd1fe979-af78-468e-b6d1-becbce7290b3.png)

# Discussions

1)Dataset Preprocessing:
  1. Make all tweets to lower case
  2. Remove hyperlinks (http, https, www), hashtags(#) and mentions (@)
  3. Remove spaces at the begin and end of tweet
  4. Remove emoticons
  5. Stemming
  6. Remove stop-words

2)Tokenization :
  Generating tokens and assigning index for each word.

3)Word Embedding
4)Model Training - LSTM
5)Model Evaluation

# Future Work

1) Use the war related dataset, train it and validate it for ukraine-russia war.
2) Balance the dataset before training the model to get accurate results.

