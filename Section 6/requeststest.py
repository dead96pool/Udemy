import requests

param = {"q":"pizza"}
# request to google
r = requests.get("http://www.google.com/search", params=param)

print(r.text)
print("Status:", r.status_code)

f = open("page.html", "w+")
f.write(r.text)