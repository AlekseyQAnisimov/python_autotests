from urllib import response
import requests

URL = 'https://api.pokemonbattle.me/v2/'
HEDERS = {"Content-Type" : "application/json" ,
           "trainer_token" : "XXX"}
body_created = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url = f'{URL}pokemons', headers = HEDERS , json = body_created)

print(response.text)

id_pokemons =  response.json()['id']   # id созданого пакемона сохраняю в переменную

body_patch = {
    "pokemon_id": id_pokemons,
    "name": "Крякря"
}

response = requests.patch(url = f'{URL}pokemons' , headers = HEDERS , json = body_patch)

print(response.text)

body_pokeball = {
    "pokemon_id": id_pokemons
}

response = requests.post(url = f'{URL}trainers/add_pokeball' , headers = HEDERS , json = body_pokeball)

print(response.text)


