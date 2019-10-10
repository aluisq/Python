vendedor = input("Coloque o seu nome, vendedor! ").title()
produto = input("Digite o nome do produto eletrônico: ")

valor_produto = float(input("Digite o valor do produto: "))

qt_produto = int(input("Digite a quantidade do produto em questão: "))

preco = round((valor_produto * qt_produto),2)

preco_desconto_10per = round((valor_produto * qt_produto)*0.9,2)

preco_parc_sem_juros = round((preco)/3,2)

comissao = round(((valor_produto * qt_produto)*0.9)*0.05,2)
print(f"A sua escolha foi {produto}")
print(f"Caso a compra seja feita à vista o valor será R$ {preco_desconto_10per}")
print(f"Caso o cliente desejar comprar parcelado e sem juros a parcela fica por: R$ {preco_parc_sem_juros}")
print(f"{vendedor}, sua comissão será de R$ {comissao} caso a compra seja à vista.")