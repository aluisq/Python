preco = float(input("Qual o valor do produto? "))

estado = input("Qual o Estado de destino do produto? [MG/SP/RJ/MS]").upper()

if estado == "MG":

    preco_final = round(preco + preco*0.07,2)
    print(f"O produto irá para {estado} e o custo unitário final será R$ {preco_final}.")

elif estado == "SP":
    preco_final = round(preco + preco * 0.12,2)
    print(f"O produto irá para {estado} e o custo unitário final será R$ {preco_final}.")

elif estado == "RJ":
    preco_final = round(preco + preco * 0.15,2)
    print(f"O produto irá para {estado} e o custo unitário final será R$ {preco_final}.")

elif estado == "MS":
    preco_final = round(preco + preco * 0.08,2)
    print(f"O produto irá para {estado} e o custo unitário final será R$ {preco_final}.")
else:
    print("Estado inválido.")