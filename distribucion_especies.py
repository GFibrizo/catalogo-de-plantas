import requests
import json
import time
import string
import re
from bs4 import BeautifulSoup

especies = {}
URL = "http://www.darwin.edu.ar/Proyectos/FloraArgentina/Especies.asp"

for letter in string.ascii_uppercase:
    page = requests.get("{}?Letra={}".format(URL, letter))
    soup = BeautifulSoup(page.content, 'html.parser')
    elements = soup.select('tr')[7:]
    for elem in elements:
        especie = elem.select('td')[0].text
        distribucion = elem.select('td')[1].text.replace(",", "").split("/")
        dist_dict = {}
        for dist in distribucion:
            dist_elem = dist.lstrip()
            key = dist_elem[0:3]
            values = re.sub('[()]', '', dist_elem[3:]).split()
            dist_dict[key] = values
        print("{}: {}".format(especie, dist_dict))
        especies[especie] = dist_dict
    time.sleep(1)

with open('distribucion_especies.json', 'w') as fp:
    json.dump(especies, fp, indent=2)
