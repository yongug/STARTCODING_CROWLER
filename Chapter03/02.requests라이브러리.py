import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com")

html = response.text
# print(html)

soup = BeautifulSoup(html,'html.parser')
word = soup.select_one('#u_ftlkw')


print(word)