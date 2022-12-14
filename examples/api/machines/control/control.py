import sys
import random
import requests

VUEPILOT_API_KEY = "<your api key here>"

# Configuration
headers = {"Authorization": f"Bearer {VUEPILOT_API_KEY}"}

# Args validation
if len(sys.argv) < 2:
    print("Invalid number of arguments")
    exit()

action = sys.argv[1]
machine_id = sys.argv[2]

if action != "stop" and action != "start" and action != "pause" and action != "fullscreen":
    print("Invalid action, must be either start, stop, pause or fullscreen")
    exit(1)

if action == "start":
    payload = {
        "id": machine_id,
        "command": "start-rotation"
    }

if action == "stop":
    payload = {
        "id": machine_id,
        "command": "stop-rotation"
    }

if action == "pause":
    payload = {
        "id": machine_id,
        "command": "pause-rotation"
    }

if action == "fullscreen":
    payload = {
        "id": machine_id,
        "command": "fullscreen-toggle"
    }

# Perform the command
response = requests.post("https://www.vuepilot.com/api/v1/machines/command",
                         json=payload, headers=headers)

result = response.json()

if response.status_code != 200:
    print("Error:", result["message"])
    exit()

print("Command completed")
