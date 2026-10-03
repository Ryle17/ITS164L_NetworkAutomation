import json
import random
import sys


def load_inventory(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {filepath} contains invalid JSON.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred reading {filepath}: {e}")
        sys.exit(1)


def ping_device(ip):
    states = ["UP", "DOWN"]
    return random.choice(states)


def main():
    inventory_file = "inventory.json"
    output_file = "output.json"

    inventory_data = load_inventory(inventory_file)
    devices = inventory_data.get("devices", [])

    if not devices:
        print("No devices found in the inventory.")
        sys.exit(1)

    results = []

    for device in devices:
        hostname = device.get("hostname", "Unknown")
        ip = device.get("ip", "0.0.0.0")

        print(f"Checking device {hostname} at {ip}...")
        status = ping_device(ip)
        print(f"Result: {hostname} is {status}\n")

        results.append({
            "hostname": hostname,
            "ip": ip,
            "status": status
        })

    try:
        with open(output_file, 'w') as out_file:
            json.dump({"results": results}, out_file, indent=4)
        print(f"Results successfully written to {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")


if __name__ == "__main__":
    main()