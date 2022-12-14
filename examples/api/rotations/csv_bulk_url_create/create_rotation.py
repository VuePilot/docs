import csv
import requests

VUEPILOT_API_KEY = "<your api key here>"
ROTATION_NAME = "Bulk URL Rotation"

# Configuration
headers = {"Authorization": f"Bearer {VUEPILOT_API_KEY}"}

with open('pages.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    pages = []
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        pages.append(row)
        line_count += 1

# Build the payload
payload = {"name": ROTATION_NAME, "pages": pages}

# Create the rotation with pages
response = requests.post("https://www.vuepilot.com/api/v1/rotations",
                         json=payload, headers=headers)

result = response.json()

if response.status_code != 201:
    print("Error:", result["message"])
    exit()

print("Rotation created successfully")
print(f"URL: https://www.vuepilot.com/dashboard#/rotations/{result['id']}")
