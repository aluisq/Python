import requests
import json


print("########################")
print("####ESCOLHA SEU POKEMON#####")
print("########################")

pkm = input("Escolha seu pokemon: ") #método dinâmico

# pkm = pikachu #método estático

def obterEnd(pkm):
    url = f'https://pokeapi.co/api/v2/pokemon/{pkm}/'
    r = requests.get(url)
    response = r.json()

    print(pkm_inf)

print(f'{response["moves"]}')

obterEnd(pkm)
