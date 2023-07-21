from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
param = {"q": search}
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
r = requests.get("https://www.bing.com/search", headers = headers, params=param)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = soup.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

