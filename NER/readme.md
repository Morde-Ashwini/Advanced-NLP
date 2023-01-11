# Overview

Named Entity Recognition(NER) involves the identification of proper names in texts, and the classification of these names into a set of predefined categories of interest like person, location, organization, drug, time, clinical procedure, biological protein, etc.
In this project, we have applied Bi-lstm method onto CONLL dataset after doing data pre-processing. We have used different techniques to pre-process the dataset, trained the model, got the accuracy, precision, f1-score for the model. To do all this we have used python programming language and diffenet libraries that help built different functionality.


# Data

Dataset being used is in conll format and can be downloaded from:
https://github.com/juand-r/entity-recognition-datasets/blob/master/data/BTC/CONLL-format/data/h.conll

We have combined these text file and kept it in Data folder in github. 

###### The dataset consists of 2 columns:
* Word
* Tag
Tags of entities are encoded in a BIO-annotation scheme. Each entity is labeled with a B or an I to detect multi-word entities, where B denotes the beginning of an entity and I denote the inside of an entity.
O denotes all other words which are not named entities.


![image](https://user-images.githubusercontent.com/113377938/204558719-5f7a3578-9586-4930-a801-5b6271f97c36.png)


## Data processing steps:
1. We first load the conll2000 dataset using nltk.
2. Then we divide the data in words(X) and tags(Y).
3. Then we vectorise both X and Y by tokenization.
4. Then in order to have uniformity in the dimensions of input and output data we apply padding to both X and y.
5. Then we load the pretrained word embeddings from https://nlp.stanford.edu/projects/glove/.
6. Then we use gensim library to transform the loaded glove embedding, so that they can be used as normal(skipgram or cbow) like wordembedding.
7. Then we map our input words with their corresponding word vectors.
8. Then we split our data into train, test, and validation set.

# Installation & Usage

We recommend to run the code in Google Colab. 
1. Before running the code, you have to first download the dataset and load it to your Google Colab.
2. copy this link and paste it in your browser. https://colab.research.google.com/drive/16RVIY6d09NeEm6e5id01t4_U_yEGK-CT  The data is also being downloaded in the same code.
3. Word vectors are downloaded and extracted into drive once. If you do not have these files in your google drive please donwload them. Connect to google drive. download these files and access from drive. Code for the same is present in shared python code.
4. Run NLP_InformationExtraction.ipynb


# Method 

**Bi-LSTM**
It is a simple sequential model with an Embedding, Bi-driectional LSTM, and Time Distributed layer.

![image](https://user-images.githubusercontent.com/113377938/204562890-f0619d25-eeb9-40bf-8db0-6b9e8593609c.png)

# Results

Below are the results for out Bi-LSTM model : 

**Model Accuracy**

![image](https://user-images.githubusercontent.com/113377938/204563256-7ff0d44f-a964-4e3f-b560-ce592af388f5.png)

**Accuracy, Precision, f1-score**

![image](https://user-images.githubusercontent.com/113377938/204563517-2330ed61-7aab-4c34-aaec-8755ca9d909f.png)


# Discussions

1. We have built Bi-LSTM model for NER on Conll dataset. The average accuracy of Bi-LSTM model is about 0.9899.
2. Our dataset has 'O' as most common tag and it is making our results look much better than they actual are.

# Future Work

1. Using larger dataset. Here we have used only 3200 sentences which are very few to build a good model for entity recognition.
2. Using fine tuned BERT model.
