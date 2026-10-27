
import requests
import random
# List of Pokemon that the player can guess
pokemon_list = ["bulbasaur", "charmeleon", "charizard", "squirtle", "rattata"]

# Select rando pokemon from list
pokemon = random.choice(pokemon_list)

# API data for pokemon
x = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)

# check if the request is success
if x.status_code == 200:

     # Convert the API response into Python data
    data = x.json()
# Height and weight of the pokemon
    name = data["name"]
    height = data["height"]
    weight = data["weight"] 

    print("Pokemon Guessing Game")
    print("Height:", height)
    print("Weight:", weight)
# give 3 attemps for player
    for i in range(3):
        guess = input("Guess the Pokemon: ")
# state if the guess is correct
        if guess == name:
            print("Correct! You win!")
            break
        else:
            print("Wrong guess!")
# tell if all three guesses were incorrect
    else:
        print("You lose! The Pokemon was", name)