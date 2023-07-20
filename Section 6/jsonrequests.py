import requests
import json
 
 
url = "https://jsonplaceholder.typicode.com/posts"
 
# payload is the data that is sent to the URL
payload = {"title": "foo",
           "body": "bar",
           "userId": 1}
# format the payload to json
headers = {"Content-Type": "application/json; charset=utf-8"}
 
response = requests.post(url, json=payload, headers=headers)
 
print(response.text)
#print(json.loads(response.text))
print(response.headers)