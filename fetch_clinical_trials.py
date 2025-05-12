import requests
import json

# Define the API endpoint
BASE_URL = "https://clinicaltrials.gov/api/v2/studies"

# Set the parameters for the request
params = {
    "pageSize": 1000  # Maximum allowed per request
}

# Set the headers to accept JSON response
headers = {
    "Accept": "application/json"
}

print("Fetching the first 1000 studies...")
response = requests.get(BASE_URL, params=params, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    studies = data.get("studies", [])

    # Save the studies to a JSON file
    with open("first_1000_studies.json", "w") as f:
        json.dump(studies, f, indent=2)

    print(f"✅ Saved {len(studies)} studies to 'first_1000_studies.json'")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}")
    print(response.text)  # Print the error message for debugging

