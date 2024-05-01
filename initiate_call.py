import requests

url = "http://0.0.0.0:8001/call"

payload = {
    "agent_id": "523f1451-aab9-4ed5-b446-eeccb57bd508",
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