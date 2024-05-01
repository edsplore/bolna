import requests

url = "http://0.0.0.0:8001/call"

payload = {
    "agent_id": "ce5947da-3927-4b78-b3ce-1781719c8e17",
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