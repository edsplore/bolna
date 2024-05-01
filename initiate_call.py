import requests

url = "http://0.0.0.0:8001/call"

payload = {
    "agent_id": "876610d2-9187-4757-aa14-b717cd1c9fdc",
    "recipient_phone_number": "+917042423450",
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