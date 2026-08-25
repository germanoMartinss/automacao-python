import requests
from bs4 import BeautifulSoup

def ultimas_noticiais():
    url = "https://g1.globo.com/rss/g1/tecnologia/"
    response = requests.get(url)
    noticias = BeautifulSoup(response.text, "html.parser")
    titulos = []
    for item in noticias.find_all('item')[:4]:
        titulos.append(item.title.text)
    return ". ".join(titulos)
