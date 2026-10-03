ITS164L - Quiz 2: Network Automation

Kindly answer the practical quiz and please be guided and use the Lab format template. Submit and attached your .pdf file and must contain additional screenshots and files here. I won't grade a lab that didn't follow my instructions.

Create a group - you can work as solo, 2s, 3s, or 4s, Max of 5 members.


1. Build a Python Network Inventory Tool

Create a Python program named:

network_inventory.py

Your program must manage at least three Cisco devices.

Each device must contain:

Hostname

Management IP address

Device type

Location

Status

Your program must:

Store all devices using a Python list and dictionaries.
Display all devices.
Display only devices whose status is up.
Count how many devices are currently operational.
Produce readable output.




2. Build a RESTCONF Network Monitoring Script



Create a Python program named:

restconf_monitor.py

Use the Cisco IOS XE router from Cisco Sandbox

Use the following RESTCONF resource:

/restconf/data/ietf-interfaces:interfaces

Your program must:

Connect to the router using HTTPS.
Use the Python requests library.
Send an HTTP GET request using RESTCONF.
Retrieve interface information.
Display the interface name and enabled status.
Display the HTTP status code.
Handle a failed connection.




3. Build an Automated Interface Configuration Tool



Create a Python program named:

interface_automation.py

Using RESTCONF, configure the following interface on a Cisco IOS XE router from Cisco Devnet Sandbox:



Your program must:

Create the correct JSON configuration payload.
Use an appropriate RESTCONF URL.
Send the configuration using an appropriate HTTP method.
Display whether the configuration succeeded or failed.
Retrieve Loopback100 afterward and verify its configuration.




4. Build Your Own Mini Network Automation Project



Create a mini network automation project with the following structure:

automation_project/

│

├── inventory.json

├── network_check.py

├── README.md

└── output.json

Your solution must manage at least three Cisco devices.

The program must:

Read device information from inventory.json.
Connect to or simulate checking each network device.
Determine whether each device is UP or DOWN.
Display the result on the screen.
Save the results to output.json.
Include basic error handling.
Document the purpose and usage of the program in README.md.
Initialize the project as a Git repository and commit the project files.
