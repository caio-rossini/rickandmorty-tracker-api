import requests


""" Function for fetching data from the Rick and Morty API based on character ID. """

def fetch_data(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Testing
data = fetch_data(2)
if data:
    print(f"Nome: {data['name']} | Status: {data['status']}")
