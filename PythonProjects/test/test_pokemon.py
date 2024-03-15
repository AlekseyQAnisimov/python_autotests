
import requests
import pytest
URL = 'https://api.pokemonbattle.me/v2/'
id_trainer = 190

def test_status_code():
    response = requests.get(url = f'{URL}trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}trainers' , params = {'trainer_id' : id_trainer})
    assert response.json()["data"][0]["trainer_name"] == 'Изя'

