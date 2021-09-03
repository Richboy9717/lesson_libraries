import requests
from pprint import pprint
from googletrans import Translator
from bs4 import BeautifulSoup

tarjimon = Translator()

sahifa = 'https://kun.uz/news/main'
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())

news = soup.find_all(class_='news-title') #faqatgina class_='news-title' shu so'zlar bilan boshlanuvchi so'zlar olinadi
pprint(news)
print(len(news))

# Api
# country = 'Uzbekistan'
# url = f'https://restcountries.eu/rest/v2/name/{country}'
# r = requests.get(url)
# r_json = r.json()[0]
# pprint(r_json['region'])

# url = f'https://api.adviceslip.com/advice'
# r = requests.get(url)
# rj = r.json()['slip']['advice']
# tarjima = tarjimon.translate(rj,dest='uz')
# print(tarjima.origin)
# print(tarjima.text)