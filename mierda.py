import requests

API_URL = "http://161.35.113.72:3000/api/v1/prediction/940107e9-61e5-43dd-bf44-a3c9079cc943"
headers = {"Authorization": "Bearer OCtTClr7ajlz70NqRwoEWPXMljs7acxZKv54mpH-QAU"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json())
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})