import requests
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()


def main():
    # IOS XE router credentials
    username = "admin"
    password = "Cisco123!"

    # IOS XE router address from Sandbox topology
    host = "10.10.20.50"

    # RESTCONF resource
    url = f"https://{host}/restconf/data/ietf-interfaces:interfaces"

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(username, password),
            headers=headers,
            verify=False,
            timeout=10
        )

        print(f"HTTP Status Code: {response.status_code}\n")

        if response.status_code != 200:
            print("Failed to retrieve interface data.")
            print(response.text)
            return

        data = response.json()

        interfaces = data[
            "ietf-interfaces:interfaces"
        ].get("interface", [])

        print("--- Interface Status ---")

        for interface in interfaces:
            name = interface.get("name", "Unknown")
            enabled = interface.get("enabled", "Unknown")

            print(f"Interface: {name:25} | Enabled: {enabled}")

    except requests.exceptions.Timeout:
        print("Connection timed out. Check that the VPN is connected.")

    except requests.exceptions.ConnectionError as error:
        print(f"Connection failed: {error}")

    except requests.exceptions.RequestException as error:
        print(f"RESTCONF request failed: {error}")


if __name__ == "__main__":
    main()