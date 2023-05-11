# Information Retrieval based on ABCnews dataset

## Introduction

This project is to build a search engine based on ABCnews dataset. The search engine is able to return the top 10 relevant documents for a given query. The search engine is built on the basis of the TF-IDF technique that used to represent documents in the form of vector weights of terms. This measures the importance of a term in a document in relation to the set of documents, then I used KNN algorithm, this algorithm finds the most similar k documents to the query by calculating the distance between the query vector and the vectors of all the documents in the dataset.

then i add a new feature to the search engine, which is the ability to go directlly to the post associated to the document relevent to the query

  [`Notebook.ipynb`](IR_Project_Notebook.ipynb)

## Dataset

The dataset used in this project is ABCnews dataset, which is a collection of more than 2,000,000 news headlines published by ABC news. The dataset is available on Kaggle, and it can be downloaded from [here](https://www.kaggle.com/therohk/million-headlines).

## Preprocessing

The dataset is preprocessed by removing stop words, punctuation, and numbers. Then, the dataset is tokenized and stemmed using the NLTK library. The dataset is then converted into a dataframe.

## k-Nearest Neighbors (KNN)

The KNN algorithm is used to find the most similar k documents to the query by calculating the distance between the query vector and the vectors of all the documents in the dataset. The distance metric used in this project is the cosine similarity. The cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.

```python
from sklearn.neighbors import NearestNeighbors

# Create NearestNeighbors object
knn = NearestNeighbors(n_neighbors=10, metric='cosine')

# Fit vectorized data to NearestNeighbors model
knn.fit(vectors)
```

## USAGE

firstly, you need to
ensure that you have django and node installed on your machine

```bash
# activate the virtual environment
source venv/scripts/activate

```

```python
# install requirements
pip install -r requirements.txt

```

firstly, you need to run the server that will assist us to get the post associated to the document relevent to the query

```bash
# run the server
cd playwright-server 
node server.js
```

then, you need to run the django server

```python
# run the django server
python manage.py runserver
```

then, you can go to the browser and type the following url http://127.0.0.1:8000/

## Demo


