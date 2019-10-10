preco_fabrica = float(input("Qual o preço de fábrica do veículo? "))

if preco_fabrica <= 12000:

    bonus_distribuidor = preco_fabrica * 0.05

    imposto = 0

    custo_consumidor = round(preco_fabrica + bonus_distribuidor + imposto, 2)

    print(f"O custo ao consumidor é R$ {custo_consumidor}")

elif 12000 < preco_fabrica <= 25000:

    bonus_distribuidor = preco_fabrica * 0.10

    imposto = preco_fabrica * 0.15

    custo_consumidor = round(preco_fabrica + bonus_distribuidor + imposto, 2)

    print(f"O custo ao consumidor é R$ {custo_consumidor}")

elif preco_fabrica > 25000:

    bonus_distribuidor = preco_fabrica * 0.15

    imposto = preco_fabrica * 0.2

    custo_consumidor = round(preco_fabrica + bonus_distribuidor + imposto, 2)

    print(f"O custo ao consumidor é R$ {custo_consumidor}")

else:
    print("Valor Inválido")
