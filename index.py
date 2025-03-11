import requests
import pandas as pd

def get_pokemon_data (url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'id' : data['id'],
            'name' : data ['name'],
            'types' : ', ' .join([t['type']['name'] for t in data['types']]),
            'height' : data['height'],
            'weight': data['weight']
        }
    else:
        return None
    
response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=50')
if response.status_code == 200:
    pokemon_list = response.json()['results']
    pokemon_data = [get_pokemon_data(pokemon['url']) for pokemon in pokemon_list]

    df = pd.DataFrame(pokemon_data)

    df.to_csv('pokemon_data.csv', index= False)
    print ("Datos guardados en 'pokemon_data.csv'")
else:
    print("Error al obtener la lista de Pokémon")
