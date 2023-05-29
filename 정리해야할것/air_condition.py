import requests
from bs4 import BeautifulSoup

# 웹 페이지에서 HTML 코드 가져오기
url = 'https://aqicn.org/city/korea/gyeonggi/suwon-si/'
html = requests.get(url).text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 미세먼지 정보 가져오기
aqi = soup.find('div', {'class': 'aqivalue'}).text.strip()

# 출력
print(aqi)
