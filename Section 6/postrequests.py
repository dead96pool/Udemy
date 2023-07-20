import requests

# https://tryphp.w3schools.com/demo/demo_form_post.php
my_data = {"name": "Nick", "email": "nick@sample.com"}
r = requests.post("https://tryphp.w3schools.com/demo/welcome.php", data=my_data)

f = open("mydata.html", "w+")
f.write(r.text)

print(r.text)