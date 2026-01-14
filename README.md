CCTV Camera Credential Checker

This tool helps verify whether user credentials are valid for a list of CCTV camera (CC cam) devices.
It checks multiple devices at once and generates a CSV report showing which credentials are correct or incorrect.

⚠️ Important Notice
This tool is intended only for devices you own or have explicit authorization to test.
Unauthorized access to CCTV systems is illegal and unethical.

Features

Bulk credential checking for CCTV cameras

Reads device IPs from a text file

Generates CSV output for easy review

Simple Python 3 execution

Requirements

Python 3.x

Network access to the target devices

Valid authorization to test the devices

Usage Instructions
1. Prepare IP Address List

Create a file named ips.txt and add one IP address per line:

192.168.1.20
192.168.1.21
192.168.1.22

2. Download the Script

Clone the repository:

git clone https://github.com/clnath/Dahua_cam.git

Make sure the script file CC_cam_script.py is present.

3. Run the Script

Execute the script using Python 3:

python3 CC_cam_script.py

4. Output

After execution, the tool will generate a CSV file containing:

Camera IP address

Username

Credential status (Valid / Invalid)

This allows you to quickly identify which CCTV devices have correct or incorrect login credentials.
