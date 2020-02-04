import requests
import json

print("###########################")
print("####ESCOLHA SEU POKEMON####")
print("###########################")

pkm = input("Escolha seu pokemon: ").lower() #método dinâmico

def obterPkm(pkm):
    url = f'https://pokeapi.co/api/v2/pokemon/{pkm}/'
    r = requests.get(url)
    response = r.json()
    cont = 0
    for ability in response["abilities"]:
        cont += 1
        print(f'{cont}° habilidade : {list(ability.values())[0]["name"]}')

obterPkm(pkm)
