preco_antigo = (float(input("Informe o preço antigo do produto: ")))

if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05

elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo * 1.1

elif preco_antigo > 100:
    preco_novo = preco_antigo * 1.15

else:
    print('CONFIRA CORRETAMENTE O VALOR DO PRODUTO!')

if preco_novo <= 80:
    print("O produto está BARATO!")

elif 80 < preco_novo <=120:
    print("O produto está com o preço NORMAL!")

elif 120 < preco_novo <= 200:
    print("O produto está com o preço CARO!")

elif preco_novo > 200:
    print("O produto está muito CARO!")

else:
    print("Relate o erro ocorrido a algum supervisor.")