import requests
from flask import jsonify


url = 'http://localhost:3000/api'
r = requests.post(url,json={'exp':1.8,})
print(r.json())

payload = {'label_name': "positive", 'count': 23}
payload1 = {'sort': "ASC" , 'count1': 4}
result =requests.get("http://127.0.0.1:3000/get_data_count", payload, headers= {"Content-Type": "application/json"})
result2=requests.get("http://127.0.0.1:3000/get_data", payload1, headers= {"Content-Type": "application/json"})

print(result.json())
print(result2.json())

