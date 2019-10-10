valor_mensal = float(input("Insira o valor das vendas mensais: "))

if valor_mensal < 20000:
    bonus = round(400 + 0.14 *valor_mensal,2)
    print(f"Sua comissão de acordo com as vendas no valor de R$ {valor_mensal} será de {bonus}")

elif 20000 <= valor_mensal < 40000:
    bonus = round(500 + 0.14 *valor_mensal,2)
    print(f"Sua comissão de acordo com as vendas no valor de R$ {valor_mensal} será de {bonus}")

elif 40000 <= valor_mensal < 60000:
    bonus = round(550 + 0.14 * valor_mensal,2)
    print(f"Sua comissão de acordo com as vendas no valor de R$ {valor_mensal} será de {bonus}")

elif 60000 <= valor_mensal < 80000:
    bonus = round(600 + 0.14 * valor_mensal,2)
    print(f"Sua comissão de acordo com as vendas no valor de R$ {valor_mensal} será de {bonus}")

elif 80000 <= valor_mensal < 100000:
    bonus = round(650 + 0.14 * valor_mensal,2)
    print(f"Sua comissão de acordo com as vendas no valor de R$ {valor_mensal} será de {bonus}")

elif valor_mensal >= 100000:
    bonus = round(700 + 0.16 * valor_mensal,2)
    print(f"Sua comissão de acordo com as vendas no valor de R$ {valor_mensal} será de {bonus}")

else:
    print("Valor Inválido!")