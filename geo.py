import requests, json
# from qgis.core import QgsField, QgsFeature
from PyQt5.QtCore import QVariant
query = r'Mörikestraße 2, 06862 Dessau-Roßlau'
key = "iQbK29zKzxCfTwp97lOnx6fXrSKbjdhDo-tlQWnZoKs"
r = requests.get('https://atlas.microsoft.com/search/fuzzy/json?api-version=1.0&subscription-key=' + key + '&query=' + query)

import json

# Opening JSON file
f = open('sample3.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['glossary']:
    print(i)

# Closing file
f.close()