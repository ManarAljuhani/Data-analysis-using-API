import requests
from flask import jsonify
import re
import pickle
import numpy as np
positive = {'label_name': 'positive' , 'count': 1000}
negative = {'label_name': 'negative' , 'count': 1000}
order = {'sort': "ASC" , 'count1': 1000}

positive_results=requests.get("http://127.0.0.1:3000/get_data_count", positive, headers= {"Content-Type": "application/json"})
negative_results=requests.get("http://127.0.0.1:3000/get_data_count", negative, headers= {"Content-Type": "application/json"})
result =requests.get("http://127.0.0.1:3000/get_data", order, headers= {"Content-Type": "application/json"})

print(result.json())


with open('model.pickle', 'rb') as file:
    model = pickle.load(file)
with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)


l = [item for sublist in result.json() for item in sublist]
myIntList = [x for x in l if isinstance(x, int)]
myStrList = [x for x in l if isinstance(x, str)]


def clean_text(text):
    text = text.lower()
    text = re.sub("@[a-z0-9_]+", ' ', text)
    text = re.sub("[^ ]+\.[^ ]+", ' ', text)
    text = re.sub("[^ ]+@[^ ]+\.[^ ]", ' ', text)
    text = re.sub("[^a-z\' ]", ' ', text)
    text = re.sub(' +', ' ', text)
    return text

for i in myStrList:
    example_test = (i)
    cleaned_test = clean_text(example_test)
    cleaned_test_vector = vectorizer.transform([cleaned_test])
    text_result = model.predict(cleaned_test_vector)
  


pred=[]
for i in myStrList: 
    vector = vectorizer.transform([i])
    text_result = model.predict(vector)
    pred.append(text_result[0]) 

from sklearn.metrics import accuracy_score
pred[:]
myIntList[:]
print(" نسبة الصحة :")
print(accuracy_score(pred,myIntList))

print("get_data_count return {} positive label".format(positive_results.json()))
print("get_data_count return {} positive label".format(negative_results.json()))
