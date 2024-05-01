import requests

url = "http://0.0.0.0:8001/call"

payload = {
    "agent_id": "eb7d50a8-7a25-4de1-b6ea-0c51d22742e6",
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