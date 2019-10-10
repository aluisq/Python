comp = float(input("Insira o comprimento do terreno em metros: "))

lar = float(input("Insira a largura do terreno em metros: "))

preco_tela = float(input("Insira o preço do metro da tela: "))

perimetro = 2 * comp + 2 * lar

custo = round(perimetro*preco_tela,2)

print(f"""
Para um terreno com perímetro de {perimetro} metros será necessário desembolsar R$ {custo} reais para cercá-lo. 
""")