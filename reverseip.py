import os
import requests
import socket

filename = input("Enter the name : ")
with open(filename, 'r') as file:
    target_sites = file.read().splitlines()

for to in target_sites:
    site = to.replace("https://", "").replace("http://", "").rstrip("/")
    try:
        ip = socket.gethostbyname(site)
    except socket.gaierror:
        print(f"Invalid or unreachable URL: {to}")
        continue

    api = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"

    try:
        response = requests.get(api)
        if response.status_code == 200:
            with open('website.txt', 'a') as mac:
                mac.write(response.text + '\n')
        else:
            print(f"Request Failed for URL: {to}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception for URL {to}: {e}")
    except Exception as ex:
        print(f"An error occurred for URL {to}: {ex}")

print("Reverse IP lookup completed.")

