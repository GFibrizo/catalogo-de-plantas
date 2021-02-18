import requests
import json
import time
from bs4 import BeautifulSoup

familias = {}
URL = "http://www.darwin.edu.ar/proyectos/floraargentina/Familias.asp"

for letter_id in [0, 1, 2]:
    page = requests.get("{}?Letras={}".format(URL, letter_id))
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.select('table')[1]
    elements = table.select('tr')[1:]
    for element in elements:
        familia = element.select('td')[0].text
        generos = element.select('td')[1].text.replace(",", "").split()
        familias[familia] = generos
    time.sleep(1)

with open('familias.json', 'w') as fp:
    json.dump(familias, fp, indent=2)
