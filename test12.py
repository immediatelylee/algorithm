import os
import time
import requests
from bs4 import BeautifulSoup

count = 0
alphabet_digit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for char in alphabet_digit:
    for char1 in alphabet_digit:
        url = "https://imgdb.in/kP{0}{1}".format(char, char1)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
        }
        count += 1
        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error: ", e)
            continue
        soup = BeautifulSoup(res.text, "lxml")
        images = soup.find(
            "img", attrs={"class": "img-responsive gallery-items"})

        if images == None:
            print(f"Error: {url} returned no images")
            continue
        image_url = images["src"]

        try:
            image_res = requests.get(image_url)
            image_res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error: ", e)
            continue

        with open("..\pythonworkspace\html\imgtest_k8{1}{0}_{2}.jpg".format(char, char1, count), "wb") as f:
            f.write(image_res.content)
        time.sleep(3)
