import requests
import json
import time
import string
import re
from bs4 import BeautifulSoup


def get_sinonimo(path):
    pass


def get_referencia(path):
    pass


def get_ejemplares(path):
    pass


def get_especie(path):
    time.sleep(1)
    especie = {}
    url = "http://www.darwin.edu.ar{}".format(path)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.select('table')[2]
    elements = table.select('tr')[:-6]
    for element in elements:
        fields = element.select('td')
        if len(fields) >= 2:
            especie[fields[0].text] = fields[1].text
    return especie




especies = {}
URL = "http://www.darwin.edu.ar/Proyectos/FloraArgentina/Especies.asp"

for letter in string.ascii_uppercase:
    page = requests.get("{}?Letra={}".format(URL, letter))
    soup = BeautifulSoup(page.content, 'html.parser')
    elements = soup.select('tr')[7:]
    for elem in elements:
        especie = elem.select('td')[0].text
        especie_link = elem.select('td')[0].select('a')[0].get('href')
        especies[especie] = get_especie(especie_link)
        print("{}: {}".format(especie, especies[especie]))
    time.sleep(1)

with open('especies.json', 'w') as fp:
    json.dump(especies, fp, indent=2)
