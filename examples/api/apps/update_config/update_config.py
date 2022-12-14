import csv
import requests

VUEPILOT_API_KEY = "<your api key here>"
APP_TOKEN = "<your apps token here>"
UPDATED_TEXT = "Our New Updated Announcement Text"

# Configuration
headers = {"Authorization": f"Bearer {VUEPILOT_API_KEY}"}

# Load the apps current configuration
response = requests.get(
    f"https://www.vuepilot.com/api/v1/apps/{APP_TOKEN}", headers=headers)

result = response.json()

if response.status_code != 200:
    print("Error:", result["message"])
    exit()

# Update config including original results using ** operator
new_config = {**result, 'config': {**result["config"], 'text': UPDATED_TEXT}}

# Send the updated config
response = requests.put(f"https://www.vuepilot.com/api/v1/apps/{APP_TOKEN}",
                        json=new_config, headers=headers)

result = response.json()

if response.status_code != 200:
    print("Error:", result["message"])
    exit()

print("App updated successfully")
print(
    f"URL: https://www.vuepilot.com/dashboard#/apps/{result['category']}/{result['token']}")
