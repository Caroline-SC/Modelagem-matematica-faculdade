import requests
from bs4 import BeautifulSoup
from typing import List, Dict


def pegarTituloG1():
    url = "https://g1.globo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    noticias = []
    
    for item in soup.select(".feed-post-link"):
        titulo = item.get_text(strip=True)
        if titulo:
            noticias.append(titulo)
    
    return noticias[:15] 

def pegarTituloBBC():
    url = "https://www.bbc.com/portuguese"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    noticias = []
    
    # Procura por tags <a> que estão dentro de <h3>
    for item in soup.select("h3 a"):
        titulo = item.get_text(strip=True)
        noticias.append(titulo)
    
    return noticias[:15]


print("\n- NOTÍCIAS DO G1 -\n\n")
for i, noticia in enumerate(pegarTituloG1(), 1):
    print(f"{i}) {noticia}\n")
    
print("\n- NOTÍCIAS DA BBC NEWS -\n\n")
for i, noticia in enumerate(pegarTituloBBC(), 1):
    print(f"{i}) {noticia}\n")
        