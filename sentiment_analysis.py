import requests
from flask import jsonify

payload = {'label_name': "positive", 'count': 15}
payload1 = {'sort_order':'ASC', 'count1': 20}
result =requests.get("http://0.0.0.0:3000/get_data", payload, headers= {"Content-Type": "application/json"})
result =requests.get("http://0.0.0.0:3000/get_data_count", payload1, headers= {"Content-Type": "application/json"})
print(result.json())







