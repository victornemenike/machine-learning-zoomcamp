import requests

url = 'http://localhost:9696/predict'
customer_id = 'Max Mustermann'
client = {"job": "student", "duration": 280, "poutcome": "failure"}

response = requests.post(url, json=client).json()
print(response)

if response['churn'] == True:
    print(f'Sending promo email to client, {customer_id}.')
else:
    print(f'Not sending promo email to client, {customer_id}.')