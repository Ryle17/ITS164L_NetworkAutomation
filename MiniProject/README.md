# Network Automation Project

This Python script reads a list of Cisco devices, simulates a network connectivity check, and logs the results.

## Prerequisites
* Python 3.x

## Files
* `inventory.json`: Source file containing network device details.
* `network_check.py`: Main execution script.
* `output.json`: Output file generated after the script runs, containing the UP or DOWN status of each device.

## Usage
Run the script from the terminal:

python network_check.py

The console will display the connection attempts and the final UP or DOWN status. The data is then saved into `output.json`.