import requests
from flask import jsonify


payload = {'var1': 1, 'var2': 3}
result =requests.get("http://0.0.0.0:3000/get_sum", payload, headers= {"Content-Type": "application/json"})
print(result.json())










