pokemon = input("What is your pokemon's name? ")
pokemon = pokemon.lower()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
import requests

req = requests.get(url)

req = req.json()

print(type(req))
print(f"The pokemon's name is {req['name']}")
print("The pokemon's abilities are :")
for ability in req['abilities']:
    print(ability['ability'] ['name'])