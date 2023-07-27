import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import json
import os
import re

def sanitize_filename(filename):
    # Remove any characters that are not allowed in filenames on most operating systems
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def Startsearch():
    url = "https://www.bing.com/images/search"
    search = input("Enter seach term:")

    # make dir if doesnt exist
    dir_name = search.replace(" ", "_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    params = {"q": search}
    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/60.0.3112.90 Safari/537.36'}

    r = requests.get(url, params = params, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "iusc"})

    print(len(links))
    #file = open("result.html", "w+", encoding="utf-8")
    #file.write(str(soup))
    """
    for item in links:
        img_obj = requests.get(item.attrs["m"])
        title = item.attrs["href"].split("/")[-1]
        img = Image.open(BytesIO(img_obj.content))

        img.save("./scaped_images/", title, img.format)

    file = open("links.txt", "w")
    for link in links:
        try:
            file.write(str(json.loads(link.attrs["m"])))
            file.write("\n")
        except:
            continue
    """
    # m element is not present in all the a tags so exception to skip those
    for link in links:
        try:
            #get the dict with key "murl" inside the dict "m"
            m = json.loads(link.attrs['m'])["murl"]
            #murl = m['murl']
            name = sanitize_filename(m.split('/')[-1])
            r = requests.get(url=m, headers=headers)
            img = Image.open(BytesIO(r.content))
            img.save(os.path.join("./" + dir_name + "/", name), img.format.lower())
            print("Image:", m)
        except KeyError as e:
            print(f"Error: KeyError - {e}. Skipping this link.")
            continue
        except OSError as e:
            print(f"Error: OSError - {e}. Skipping this link.")
            continue
    Startsearch()

Startsearch()