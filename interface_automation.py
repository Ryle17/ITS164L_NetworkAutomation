import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

def main():
    # actual values removed for security
    HOST = '[ROUTER_IP]'
    PORT = '9443'
    USER = '[ROUTER_USER]'
    PASS = '[ROUTER_PASS]'

    base_url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"
    loopback_url = f"{base_url}/interface=Loopback100"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    payload = {
        "ietf-interfaces:interface": {
            "name": "Loopback100",
            "description": "Configured via RESTCONF Python Script",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "10.100.100.1",
                        "netmask": "255.255.255.255"
                    }
                ]
            }
        }
    }

    print("Sending configuration to router...")
    try:
        put_response = requests.put(
            loopback_url,
            auth=HTTPBasicAuth(USER, PASS),
            headers=headers,
            data=json.dumps(payload),
            verify=False,
            timeout=10
        )

        if put_response.status_code in [201, 204]:
            print(f"SUCCESS: Loopback100 configured! (Status Code: {put_response.status_code})")
        else:
            print(f"FAILED to configure. HTTP Status Code: {put_response.status_code}")
            print(put_response.text)
            return

        print("\nVerifying configuration...")
        get_response = requests.get(
            loopback_url,
            auth=HTTPBasicAuth(USER, PASS),
            headers=headers,
            verify=False
        )

        if get_response.status_code == 200:
            print("Verification successful. Retrieved configuration:")
            print(json.dumps(get_response.json(), indent=2))
        else:
            print(f"Verification failed. HTTP Status: {get_response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    main()