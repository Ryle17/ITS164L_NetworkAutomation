import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

def main():
    HOST = 'ios-xe-mgmt.cisco.com'
    PORT = '9443'
    USER = 'developer'
    PASS = 'C1sco12345'
    
    url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
    
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    try:
        response = requests.get(
            url, 
            auth=HTTPBasicAuth(USER, PASS), 
            headers=headers, 
            verify=False 
        )
        
        print(f"HTTP Status Code: {response.status_code}\n")
        
        if response.status_code == 200:
            data = response.json()
            interfaces = data["ietf-interfaces:interfaces"]["interface"]
            
            print("--- Interface Status ---")
            for interface in interfaces:
                name = interface.get("name", "Unknown")
                enabled = interface.get("enabled", "Unknown")
                print(f"Interface: {name:25} | Enabled: {enabled}")
        else:
            print("Failed to retrieve data.")

    except requests.exceptions.RequestException as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()