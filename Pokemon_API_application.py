#pokemon = input("question for the pokemon name")
pokemon = input("What is your pokemon's name? ")
print(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
# import requests
# # print(f"https://{pokemon}.io")-this is the template for a dynamic url
# req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
# req = req.json()#this helps change the json formatted API into a dictionary
# print(req)
#print(f"some textin here req[key]")- this will be me taking the key that holds a certain value about that pokemon and printing it out




# ask for user input: ask for a pokemon
# create a dynamic url that requests api data for that pokemon
# fetch the data for that url
# print out the json data as a dictionary
# print out pokemon data based on what is available in the api data