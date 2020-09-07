import requests
from flask import jsonify
import re
import pickle

positive = {'label_name': 'positive' , 'count': 1000}
negative = {'label_name': 'negative' , 'count': 1000}
order = {'sort': "ASC" , 'count1': 1000}

positive_results=requests.get("http://127.0.0.1:3000/get_data_count", positive, headers= {"Content-Type": "application/json"})
negative_results=requests.get("http://127.0.0.1:3000/get_data_count", negative, headers= {"Content-Type": "application/json"})
result =requests.get("http://127.0.0.1:3000/get_data", order, headers= {"Content-Type": "application/json"})

print(result.json())
print("get_data_count return {} positive label".format(positive_results.json()))
print("get_data_count return {} positive label".format(negative_results.json()))



def clean_text(text):
    text = text.lower()
    text = re.sub("@[a-z0-9_]+", ' ', text)
    text = re.sub("[^ ]+\.[^ ]+", ' ', text)
    text = re.sub("[^ ]+@[^ ]+\.[^ ]", ' ', text)
    text = re.sub("[^a-z\' ]", ' ', text)
    text = re.sub(' +', ' ', text)
    return text

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

with open('model.pickle', 'rb') as file:
    model = pickle.load(file)
with open('vectorizer.pickle', 'rb') as file:
    vectorizer = pickle.load(file)
    
positive_texts =[]
negative_texts =[]
for i in myStrList:
    example_test = (i)
    cleaned_test = clean_text(example_test)
    cleaned_test_vector = vectorizer.transform([cleaned_test])
    text_result = model.predict(cleaned_test_vector)
    print("sentence classification:", cleaned_test)
    print(text_result[0])
    if text_result[0] == 0:
        negative_texts.append(cleaned_test[:])
    else:
        positive_texts.append(cleaned_test[:])

print("positive texts:")
print(positive_texts)
print(" negative texts:")
print(negative_texts)
print("the amount of positive texts:")
print(len(positive_texts))
print("the amount of negatve texts:")
print(len(negative_texts))

positive_labels = [1]*len(positive_texts)  
negative_labels = [0]*len(negative_texts) 
all_texts = positive_texts + negative_texts 
all_labels = positive_labels + negative_labels  


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


predictions = model.predict(x_test)
print("نسبة الصحة باستخدام خوارزمية إس في إم :")
print(accuracy_score(y_test, predictions))


example_test = 'I am so happy, the picnic was amazing and the weather was great'
cleaned_example_test = clean_text(example_test)
example_test_vector = vectorizer.transform([cleaned_example_test])
example_result = model.predict(example_test_vector)
print("تصنيف الجملة:", example_test)
print(example_result[0]) 
