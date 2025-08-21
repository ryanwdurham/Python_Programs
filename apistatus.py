
# This program tests multiple API endpoints, checks their status codes, and validates that the expected JSON keys are present in the responses.

import requests
import json
import csv
from datetime import datetime

# List of API endpoints and expected JSON keys
api_tests = [
    {
        "url": "https://jsonplaceholder.typicode.com/posts/1",
        "expected_keys": ["userId", "id", "title", "body"]
    },
    {
        "url": "https://jsonplaceholder.typicode.com/users/1",
        "expected_keys": ["id", "name", "username", "email"]
    },
    {
        "url": "https://jsonplaceholder.typicode.com/todos/1",
        "expected_keys": ["userId", "id", "title", "completed"]
    }
]

# CSV filename with timestamp
csv_filename = f"api_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Write CSV header
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Status Code", "Status Test", "JSON Keys Test", "Missing Keys"])

# Function to test an API endpoint
def test_api(endpoint):
    url = endpoint["url"]
    expected_keys = endpoint["expected_keys"]

    try:
        response = requests.get(url)
        status_code = response.status_code
        status_test = "PASSED" if status_code == 200 else "FAILED"

        # Validate JSON keys
        missing_keys = []
        try:
            data = response.json()
            missing_keys = [key for key in expected_keys if key not in data]
        except json.JSONDecodeError:
            missing_keys = expected_keys  # if response is not JSON, all keys are missing

        json_keys_test = "PASSED" if not missing_keys else "FAILED"

        # Log result to CSV
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url, status_code, status_test, json_keys_test, ", ".join(missing_keys)])

        # Print result to console
        print(f"URL: {url}")
        print(f"Status Code: {status_code} -> {status_test}")
        print(f"JSON Keys Test: {json_keys_test}")
        if missing_keys:
            print(f"Missing Keys: {missing_keys}")
        print("-" * 50)

    except requests.exceptions.RequestException as e:
        print(f"API Request Failed for {url}: {e}")

# Run tests for all endpoints
print(f"Starting batch API tests... Results will be saved in {csv_filename}\n")
for test in api_tests:
    test_api(test)

print("\nBatch API testing completed.")