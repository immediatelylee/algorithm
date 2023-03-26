import requests
from bs4 import BeautifulSoup

url = 'https://aqicn.org/city/korea/gyeonggi/suwon-si/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('div', {'class': 'aqiwidget aqiwidget - xxl'})

print(div)
