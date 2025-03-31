# Required Libraries:
# - requests: To interact with the VirusTotal API.
# - psutil: To check the firewall and system processes.
# - os: To walk through the file system and check files.
# - shutil: To handle file operations.

# To install the necessary libraries, you can run the following commands:
# For Linux/macOS:
# pip install requests psutil
#
# For Windows:
# python -m pip install requests psutil
#
# Note: Make sure Python is installed on your system before running the script.

import os
import requests
import psutil
import shutil

# Your VirusTotal API key
API_KEY = "your_virustotal_api_key"

# Function to scan a file using VirusTotal
def scan_file(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()

    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "x-apikey": API_KEY
    }
    
    response = requests.post(url, headers=headers, files={"file": file_data})

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to scan files in a directory
def scan_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning: {file_path}")
            result = scan_file(file_path)
            if result:
                print(f"File scan result: {result}")
            else:
                print(f"Error scanning {file_path}")

# Function to check the status of the firewall
def check_firewall():
    firewall_status = psutil.win_service_get("MpsSvc").status() if os.name == 'nt' else "Not Available on this OS"
    print(f"Firewall status: {firewall_status}")

# Function to check disk space (optional additional security check)
def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    print(f"Total space: {total // (2**30)} GB")
    print(f"Used space: {used // (2**30)} GB")
    print(f"Free space: {free // (2**30)} GB")

# Main function to run the antivirus scan
def main():
    # Start the scanning process
    print("Starting system scan...")

    # Scan files in the user's home directory (or other specific directory)
    home_directory = os.path.expanduser("~")
    scan_directory(home_directory)

    # Check firewall status
    check_firewall()

    # Check disk space (optional extra)
    check_disk_space()

    # End message
    print("\nThank you for using this script!\n\nBest regards,\nLewenn\n\nFeel free to follow me on GitHub: https://github.com/lewennpy")

if __name__ == "__main__":
    main()
