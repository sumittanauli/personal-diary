import requests

api_key = '720f6fd9-0d29-48db-bf0d-f8add57fccd6'
word = 'car'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)

