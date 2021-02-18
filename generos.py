import requests
import json
import time
import string
from bs4 import BeautifulSoup

generos = {}
URL = "http://www.darwin.edu.ar/Proyectos/FloraArgentina/Generos.asp"

for letter in string.ascii_uppercase:
    page = requests.get("{}?Letra={}".format(URL, letter))
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.select('table')[1]
    elements = table.select('tr')[1:]
    for element in elements:
        genero = element.select('td')[0].text
        especies = element.select('td')[1].text.replace(",", "").split()
        generos[genero] = especies
    time.sleep(1)

with open('generos.json', 'w') as fp:
    json.dump(generos, fp, indent=2)
