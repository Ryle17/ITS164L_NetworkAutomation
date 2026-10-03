def main():
    inventory = [
        {
            "hostname": "NYC-RTR-01",
            "ip": "10.0.1.1",
            "type": "Cisco ISR 4331",
            "location": "New York",
            "status": "up"
        },
        {
            "hostname": "LAX-SW-01",
            "ip": "10.0.2.10",
            "type": "Cisco Catalyst 9300",
            "location": "Los Angeles",
            "status": "down"
        },
        {
            "hostname": "CHI-FW-01",
            "ip": "10.0.3.254",
            "type": "Cisco Firepower 2100",
            "location": "Chicago",
            "status": "up"
        }
    ]

    print("--- All Network Devices ---")
    for device in inventory:
        print(f"[{device['hostname']}] IP: {device['ip']} | Type: {device['type']} | Loc: {device['location']} | Status: {device['status'].upper()}")

    print("\n--- Operational Devices Only (Status: UP) ---")
    operational_count = 0
    for device in inventory:
        if device['status'].lower() == "up":
            print(f"Hostname: {device['hostname']} (IP: {device['ip']})")
            operational_count += 1
            
    print(f"\nTotal Operational Devices: {operational_count}")

if __name__ == "__main__":
    main()