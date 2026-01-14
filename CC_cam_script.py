import requests
from requests.auth import HTTPDigestAuth
import csv

USERNAME = "admin"
PASSWORD = "admin123"
TIMEOUT = 5
OUTPUT_FILE = "dahua_results.csv"

# Dahua-protected CGI endpoints
DAHUA_ENDPOINTS = [
    "/cgi-bin/magicBox.cgi?action=getSystemInfo",
    "/cgi-bin/magicBox.cgi?action=getDeviceType"
]

def check_dahua(ip, writer):
    base_url = f"http://{ip}"

    for endpoint in DAHUA_ENDPOINTS:
        url = base_url + endpoint

        try:
            r = requests.get(
                url,
                auth=HTTPDigestAuth(USERNAME, PASSWORD),
                timeout=TIMEOUT
            )

            if r.status_code == 200 and "Error" not in r.text:
                print(f"[SUCCESS] {ip} -> Dahua authenticated")
                writer.writerow([ip, "SUCCESS", endpoint, r.status_code])
                return

            elif r.status_code == 401:
                print(f"[FAILED ] {ip} -> Unauthorized")
                writer.writerow([ip, "UNAUTHORIZED", endpoint, r.status_code])

            else:
                print(f"[INFO   ] {ip} -> Status {r.status_code}")
                writer.writerow([ip, "OTHER", endpoint, r.status_code])

        except requests.exceptions.RequestException as e:
            print(f"[ERROR  ] {ip} -> {e}")
            writer.writerow([ip, "ERROR", endpoint, str(e)])
            return

    print(f"[FAILED ] {ip} -> Not Dahua or wrong credentials")

def main():
    with open("ips.txt", "r") as f:
        ips = [line.strip() for line in f if line.strip()]

    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Result", "Endpoint", "Status"])

        for ip in ips:
            print(f"\nChecking {ip}")
            check_dahua(ip, writer)

    print(f"\nResults saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
