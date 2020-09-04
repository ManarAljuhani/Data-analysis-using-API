import requests
from flask import jsonify
import pandas as pd
import numpy as np
np.random.seed(0)
data = pd.read_csv("/home/ubuntu/IMDB Dataset (1).csv")
payload = {'label_name': "positive", 'count': 15}
payload1 = {'sort':'ASC', 'count1': 20}
result =requests.get("http://0.0.0.0:3000/get_data_count", payload, headers= {"Content-Type": "application/json"})
result2 =requests.get("http://0.0.0.0:3000/get_data", payload1, headers= {"Content-Type": "application/json"})
print(result.json())
print(result2.json())
data['TEXT']=data['review']
data =  data.drop(['review'], axis=1)
data['sentiment'][data['sentiment'] == 'positive'] = 1
data['sentiment'][data['sentiment']== 'negative'] = 0
data['CLASSIFICATION_NUM'] =data['sentiment'].astype('int')
data = data.drop(['sentiment'], axis=1)
data['ID'] = pd.Series(np.arange(1, len(data.index)+1)).astype(str).str.zfill(4)
data.insert(0, 'DATE', pd.datetime.now().replace(microsecond=0))
data.head()
negative_texts = []
positive_texts = []
import re


def clean_text(text):
    text = text.lower()

    text = re.sub("@[a-z0-9_]+", ' ', text)
    text = re.sub("[^ ]+\.[^ ]+", ' ', text)
    text = re.sub("[^ ]+@[^ ]+\.[^ ]", ' ', text)
    text = re.sub("[^a-z\' ]", ' ', text)
    text = re.sub(' +', ' ', text)
    return text
for i in range(len(data)):
    if data['CLASSIFICATION_NUM'][i] ==0 :
        negative_texts.append(clean_text(data['TEXT'][i]))
    else:
        positive_texts.append(clean_text(data['TEXT'][i]))
print("عدد النصوص الإيجابية:")
print(len(positive_texts))
print("عدد النصوص السلبية:")
print(len(negative_texts))
positive_labels = [1]*len(positive_texts)
negative_labels = [0]*len(negative_texts)

all_texts = positive_texts + negative_texts
all_labels = positive_labels + negative_labels
print("عدد النصوص يساوي عدد التصنيفات؟")
print(len(all_labels) == len(all_texts))
from sklearn.utils import shuffle
all_texts, all_labels = shuffle(all_texts, all_labels)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(all_texts, all_labels, test_size=0.20)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}', min_df=1)
vectorizer.fit(x_train)
x_train = vectorizer.transform(x_train)
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(x_train, y_train)
from sklearn.metrics import accuracy_score
x_test = vectorizer.transform(x_test)
predictions = model.predict(x_test)
print(" نسبة الصحة باستخدام خوارزمية نايف بيز :")
print(accuracy_score(y_test, predictions))
from sklearn.svm import LinearSVC
model = LinearSVC()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print("نسبة الصحة باستخدام خوارزمية إس في إم :")
print(accuracy_score(y_test, predictions))
import pickle
with open('model.pickle', 'wb') as file:
    pickle.dump(model, file)
with open('vectorizer.pickle', 'wb') as file:
    pickle.dump(vectorizer, file)
with open('model.pickle', 'rb') as file:
    model = pickle.load(file)
with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)

example_test = 'I am so happy, the picnic was amazing and the weather was great'
cleaned_example_test = clean_text(example_test)
example_test_vector = vectorizer.transform([cleaned_example_test])
example_result = model.predict(example_test_vector)
print("تصنيف الجملة:", example_test)
print(example_result[0])



