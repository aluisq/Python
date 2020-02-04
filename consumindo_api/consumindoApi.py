import requests

print("########################")
print("####CONSULTANDO CEP#####")
print("########################")

cep = input("Digite seu CEP: ")

if len(cep) != 8:
    print("Quantidade de dígitos inválido.")
    print(f"Você digitou: {len(cep)} dígitos")
    print("É necessário inserir 8 dígitos")
    exit()

def obterEnd(cep):
    url = f'http://viacep.com.br/ws/{cep}/json/'
    r = requests.get(url)
    response = r.json()

    print(f'Logradouro : {response["logradouro"]}')
    print(f'Bairro : {response["bairro"]}')
    print(f'localidade : {response["localidade"]}')

obterEnd(cep)
