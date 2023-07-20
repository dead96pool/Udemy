import requests
from io import BytesIO
from PIL import Image


r = requests.get("https://freepngimg.com/download/game/65816-television-firewatch-campo-wallpaper-desktop-4k-santo.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format

try:
    image.save(path)
except:
    print("Cannot save image.")
