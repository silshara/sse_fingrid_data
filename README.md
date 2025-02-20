# FinGrid - Fetching API Data

## Overview

This Python script fetches time series data from the [FinGrid Open Source API](https://data.fingrid.fi) for the following datasets:

- **Wind Power Production** (Dataset ID: 181)
- **Electric Boiler Consumption Sum** (Dataset ID: 371)

The goal is to retrieve and analyze these datasets to determine if there is any correlation between wind power production and electric boiler consumption.

## Features

- Fetches data from the FinGrid API.
- Handles API authentication using an environment variable (`API_KEY`).
- Manages potential API errors, including `404 Not Found` responses.
- Writes the retrieved dataset information to a `dataset_info.txt` file.

## Requirements

- Python 3.x
- Internet access for API requests
- FinGrid API Key (set as an environment variable)

## Setup

1. **Obtain an API Key**:

   - Sign up at [FinGrid Open Source API](https://data.fingrid.fi) to get an API key.

2. **Set Up Environment Variable**:

   ```sh
   export API_KEY='your_api_key'

   - Windows Powershell,
   $env:API_KEY="your_api_key_here"

   ```

3. **Install Dependencies**: No additional dependencies are required, as the script uses built-in Python libraries.

4. **Run the Script**:

   ```sh
   python script.py
   ```

## Code Explanation

1. **Fetching Data**:

   - The script iterates over the dataset IDs (181 for wind power production, 371 for electric boiler consumption).
   - It constructs API requests with authentication headers.
   - If the dataset is found (`200 OK`), the response is stored; otherwise, `404` errors are logged.

2. **Handling Errors**:

   - The script catches `HTTPError` exceptions to track missing datasets.
   - A delay (`time.sleep(2)`) is included to prevent hitting the API rate limit.

3. **Saving Data**:

   - Retrieved datasets are saved in `dataset_info.txt` as JSON.