import sys
import random
import requests

VUEPILOT_API_KEY = "<your api key here>"

# Configuration
headers = {"Authorization": f"Bearer {VUEPILOT_API_KEY}"}

# Args validation
if len(sys.argv) < 2:
    print("Invalid number of argumets")
    exit()

action = sys.argv[1]
machine_id = sys.argv[2]
category = sys.argv[3]
destination = sys.argv[4]

if action != "stop" and action != "start":
    print("Invalid action, must be either start or stop")
    exit(1)

if action == "start":
    if category == "url":
        payload = {
            "id": machine_id,
            "command": "hijack-start",
            "url": destination,
        }

    if category == "app":
        payload = {
            "id": machine_id,
            "command": "hijack-start",
            "url": f"https://www.vuepilot.com/app/{destination}-{random.randint(100,999)}",
            "app_id": destination
        }

if action == "stop":
    payload = {
        "id": machine_id,
        "command": "hijack-stop"
    }

# Perform the hijack
response = requests.post("https://www.vuepilot.com/api/v1/machines/hijack",
                         json=payload, headers=headers)

result = response.json()

if response.status_code != 200:
    print("Error:", result["message"])
    exit()

print("Hijack completed")
