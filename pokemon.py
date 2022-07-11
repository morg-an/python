# get info from API
import requests
import json
import os

# Changing directory for where new JSON files will be stored
os.chdir("/Users/morganschumann/Documents/_Programming/2022/Pokemon")

# Make initial request to Pokeapi - to change the number returned, modify the query string
r = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=151")

# Making sure the get request works:
# print(r.status_code)

# Lookup the type of the response I'm getting - expected JSON, and that's what it is.
# print(r.headers['content-type'])

# Printing the JSON as text just to see what I've got to work with.
# print(r.text)

# transforming the JSON response to Python, then verifying the new type is a dictionary
parsed = r.json()
# print(type(parsed))

# Create function to get each Pokemon's url


def getPokemon():
    pokemon_urls = []
    for poke in parsed['results']:
        pokemon_urls.append(poke['url'])
    return pokemon_urls

# create fuction to get the names of relevant Pokemon included in query string limit, above.


def getNames():
    pokemon_names = []
    for poke in parsed['results']:
        pokemon_names.append(poke['name'])
    return pokemon_names


# get all the Pokemon Names
names = getNames()

# get the urls to the API for each Pokemon
allPokemon = getPokemon()

# Create a function to get all of the types of all Pokemon by:
#  - looping through all Pokemon's urls
#  - parsing the details
#  - get types
#  - cross checking if not already in list of abilities, then
#  - adding to list.


def getTypes():
    list_of_types = []
    for pokemon in allPokemon:
        details = requests.get(pokemon)
        parsed_details = details.json()
        for type in parsed_details['types']:
            if type.get('type').get('name') not in list_of_types:
                list_of_types.append(type.get('type').get('name'))
    return list_of_types


allTypes = getTypes()
print(allTypes)

# Create a function to write JSON files for each type containing list of Pokemon with that type.
# Save in separate files by type.


def pokemonByType():
    print("Writing JSON files...")
    for type in allTypes:
        pokemon_by_type = []
        pokemon_by_type_dict = {}
        details = requests.get('https://pokeapi.co/api/v2/type/'+type)
        parsed_details = details.json()
        for pokemon in parsed_details['pokemon']:
            # checks to see if the names of the pokemon are included in the set we are analyzing based on the initial query string
            if pokemon.get('pokemon').get('name') in names:
                # if it is, append the name and url to a list -
                # Note, I know this would be better stright into a dictionary, but append doesn't work for that.
                # Tried .update(), but that replaced the values since the keys were the same. Maybe there's a better way ¯\_(ツ)_/¯
                pokemon_by_type.append({"name": pokemon.get('pokemon').get('name'), "url": pokemon.get('pokemon').get(
                    'url')})
        # Get the list of pokemon by type into a dictionary so it can be converted to JSON
        for pokemon in pokemon_by_type:
            pokemon_by_type_dict.update({type: pokemon_by_type})
        # Create JSON
        json_string = json.dumps(pokemon_by_type_dict)
        # with open('{}.json'.format(type), 'w') as newfile:
        #     newfile.write(json_string)
        print("{}.json".format(type) + " file created. Contents:" + json_string)
    print("Done")


# Call function to create the JSON files by type
pokemonByType()
