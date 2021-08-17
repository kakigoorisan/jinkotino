import requests


url = "https://discord.com/api/v8/applications/873072627336503336/commands"

json = {
    "name":"jinko",
    "description":"Will you talk with AI?",
    "options": [
        {
        "name": "talk",
        "description": "Talking start or stop",
        "type": 3,
        "required": True,
        "choices": [
                {
                    "name": "start",
                    "value": "start_talk"
                },
                {
                    "name":"end",
                    "value": "end_talk"
                }
            ]
        },
        {
            "name":"help",
            "description":"when you get lost, this command helps you",
            "type": 5,
            "required":False
        }
    ]
}
headers = {
    "Authorization": "Bot ODczMDcyNjI3MzM2NTAzMzM2.YQzGPw.l7ju4edj1-OcF1LB9X3FhInLD9Q"
}
r = requests.post(url, headers=headers, json=json)
print(r.json())
