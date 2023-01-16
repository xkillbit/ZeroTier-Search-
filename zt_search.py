 import requests
import json
from tabulate import tabulate

# Replace with your ZeroTier API token
api_token = "API_KEY"

# Replace with the ID of the network you want to query
network_id = "NET_ID"

# Replace with the name of the host you want to search for
host_name = input("ENTER SEARCH QUERY:>")

# Build the API endpoint URL
url = f"https://my.zerotier.com/api/network/{network_id}/member"

# Set the headers for the API call
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_token}"
}

# Execute the API call
response = requests.get(url, headers=headers)

# Parse the JSON response
data = json.loads(response.text)

# Create an empty list to store the filtered hosts
filtered_hosts = []

# Iterate over the hosts and filter by name
for host in data:
    if host_name in host["name"] :
        filtered_hosts.append(host)

# Define the table headers
headers = ["Name", "IP Address", "Online"]

# Define the table rows
rows = [[host["name"], host["config"]["ipAssignments"][0], host["online"]] for host in filtered_hosts]

# Print the table
print(tabulate(rows, headers, tablefmt="plain"))
