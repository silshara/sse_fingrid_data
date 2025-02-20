import os
import urllib.request, json
import ssl
import time

# add your API key to system environment variables
# export API_KEY='your_api_key'

api_key = os.getenv('API_KEY')

# List to store dataset IDs with "Error 404"
error_404_ids = []

# List to store dataset information
datasets_info = []
# List to store time series data
merged_data = []

# Dataset IDs to fetch and merge - Wind power production and Electric boiler consumption sum
additional_dataset_ids = [181, 371]

for dataset_id in additional_dataset_ids:
    try:
        url = f"https://data.fingrid.fi/api/datasets/{dataset_id}/data"

        hdr = {
            # Request headers
            'Cache-Control': 'no-cache',
            'x-api-key': api_key,
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        context = ssl._create_unverified_context()

        response = urllib.request.urlopen(req, context=context)
        
        # Parse the JSON response
        data = json.loads(response.read().decode('utf-8'))
        
        # Append the dataset response to the list
        datasets_info.append({
            'datasetId': dataset_id,
            'data': data
        })

    except urllib.error.HTTPError as e:
        if e.code == 404:
            error_404_ids.append(dataset_id)
    except Exception as e:
        print(f"Error fetching dataset {dataset_id}: {e}")
    time.sleep(2)  # Sleep for 2 seconds to avoid hitting the rate limit

# Print the updated list of dataset information
print("Updated Dataset Information:")
print(datasets_info)

# Print the updated list of dataset IDs with "Error 404"
print("Updated Dataset IDs with Error 404:")
print(error_404_ids)

# Write the updated dataset information to the file
with open('dataset_info.txt', 'w') as file:
    json.dump(datasets_info, file, indent=4)