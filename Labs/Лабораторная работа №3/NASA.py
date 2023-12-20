import requests
from nasapy import Nasa
from PIL import Image
import random

api_key = "lIquZdBhc50ci12gfKiEHjW2KTR4Iw2ZJcevZsoC"
nasa = Nasa(key=api_key)

today = "2023-09-09"
fmt_today = today.replace("-", "/")
nasa_date = nasa.epic(date=today)

images_counter = 0
num_data = len(nasa_date)
for index, data in enumerate(nasa_date):
    try:
        response = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/{fmt_today}/png/{data["image"]}.png?api_key={api_key}'
        )
        with open(f"image{str(index)}.png", "wb") as file:
            file.write(response.content)
        images_counter += 1
        print(f"proccessed: {images_counter} out of {num_data}")
    except Exception as exc:
        print(f"Ошибка при скачивании или сохранении изображения {index + 1}: ", exc)

photos = []
for i in range(images_counter):
    photo = Image.open(f"image{i}.png")
    photos.append(photo)

photos[0].save(
    "earth.gif",
    save_all=True,
    append_images=photos[1:],
    optimize=True,
    duration=[random.randint(80, 100) for i in range(len(photos))],
    loop=0,
)
