from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")

# get the 'search' parameter request instead of hardcoing the search term
params = {"q": search}
r = requests.get("http://www.google.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

