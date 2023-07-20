import requests

r = requests.get("https://www.google.com")
print("Status:", r.status_code)

