from flask import  requests

api_key = 'c0f3af32-1aec-406c-b06a-7759ee6a9e76'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definition = res.json()

for definition in definition:
    print(definition)