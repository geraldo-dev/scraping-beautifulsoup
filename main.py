import requests
from bs4 import BeautifulSoup as bs

headers = { "User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0' }

url = 'https://inglescompensadores.com.br/texto-em-ingles-com-audio-1-mike-tyson/'

req = requests.get(url, headers=headers)
soup = bs(req.content, "html.parser")

titulo = soup.find('h1')['title']


