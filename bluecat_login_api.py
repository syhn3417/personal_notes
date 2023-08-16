import requests

# Replace with your BlueCat Address Manager API base URL
api_base_url = 'https://your-bam-server/api'

# Replace with your BAM API credentials
username = 'your-username'
password = 'your-password'

# Authenticate and obtain an API token
auth_endpoint = f'{api_base_url}/login'
response = requests.post(auth_endpoint, json={'username': username, 'password': password})
auth_data = response.json()

if 'access_token' in auth_data:
    api_token = auth_data['access_token']
    print("Authentication successful. API token obtained.")

    # Use the obtained API token for subsequent API requests
    headers = {'Authorization': f'Bearer {api_token}'}

    # Example: Retrieve a list of configured IP addresses
    ip_list_endpoint = f'{api_base_url}/ipam/address'
    ip_list_response = requests.get(ip_list_endpoint, headers=headers)

    if ip_list_response.status_code == 200:
        ip_list_data = ip_list_response.json()
        print("List of IP Addresses:")
        for item in ip_list_data:
            print(item['address'])
    else:
        print("Failed to retrieve IP address list.")
else:
    print("Authentication failed.")
