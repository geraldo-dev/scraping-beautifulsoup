import requests
from bs4 import BeautifulSoup as bs

headers = { "User-Agent" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0' }

url = 'https://inglescompensadores.com.br/texto-em-ingles-com-audio-1-mike-tyson/'

req = requests.get(url, headers=headers)
soup = bs(req.content, "html.parser")

completo = []

#taking the title
title = soup.find('h1')['title']

#filter content by paragraphs
paragraphs = soup.find_all('p')[2:11]

completo.append(title)

for p in paragraphs:
    completo.append(p.text)


def save_csv(name_file, list_phrases):

    for phrase in list_phrases:
        new_file = open(f"{name_file}.csv",'a')
        new_file.write(phrase+'\n')
        new_file.close()

save_csv('historia', completo)
print('salvo')