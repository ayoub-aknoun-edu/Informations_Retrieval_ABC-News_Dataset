# Create your views here.
import pickle
from django.shortcuts import render
from datetime import datetime
from pandas import read_csv
import re
import nltk
from django.views.decorators.csrf import csrf_exempt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

def preprocess(text):
    text = text.lower() # convert to lowercase
    text = re.sub(r'\d+', '', text) # remove digits
    text = re.sub(r'[^\w\s]', '', text) # remove punctuation
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text) # tokenization
    tokens = [stemmer.stem(w) for w in tokens if not w in stop_words] # remove stopwords and stemming
    return ' '.join(tokens)



# Load the IR model
with open('C:/Users/ayoub/IRProject_ABCnewsDataset/searsh/IRmodel.pkl', 'rb') as f:
    model = pickle.load(f)

data = read_csv('C:/Users/ayoub/IRProject_ABCnewsDataset/searsh/abcnews-date-text.csv')
with open('C:/Users/ayoub/IRProject_ABCnewsDataset/searsh/vectorizer.pkl','rb') as f :
    vectorizer = pickle.load(f)


@csrf_exempt
def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        # Use the IR model to retrieve the most relevant documents
        query = preprocess(query)
        query_vector = vectorizer.transform([query])
        distance, indices = model.kneighbors(query_vector)
        relevant_docs = []
        for i,index in enumerate(indices[0]):
            relevant_docs.append({"top_document":i+1,"headline":data.iloc[index]['headline_text'], "date":datetime.strptime(str(data.iloc[index]['publish_date']),'%Y%m%d').strftime('%d-%m-%Y'),"link":data.iloc[index]['link']})
        return render(request, 'search/search.html', {'docs': relevant_docs})
    else:
        return render(request, 'search/search.html')