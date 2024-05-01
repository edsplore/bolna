import requests

url = "http://0.0.0.0:8001/call"

payload = {
    "agent_id": "945d024d-4d55-44e6-98c2-a01127dfd056",
    "recipient_phone_number": "+919811966113",
    "user_data": {
        "first_name": "Anmol",
        "last_name": "Rishi",
        "honorific": "Mr."
    }
}
headers = {
    #"Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)