print("Bem vindo! O sistema ja está pronto!")

cod = int(input("Insira o código do produto: "))

if 100 <= cod <= 106:
    if cod == 100 and cod == 103:
        preco = 1.2
        qtd = int(input("Qual a quantidade do produto? "))
        total = round(qtd * preco,2)
        print(f" O total do pedido é R$ {total}")

    elif cod == 101:
        preco = 1.3
        qtd = int(input("Qual a quantidade do produto? "))
        total = round(qtd * preco,2)
        print(f" O total do pedido é R$ {total}")

    elif cod == 102:
        preco = 1.5
        qtd = int(input("Qual a quantidade do produto? "))
        total = round(qtd * preco,2)
        print(f" O total do pedido é R$ {total}")

    elif cod == 104:
        preco = 1.7
        qtd = int(input("Qual a quantidade do produto? "))
        total = round(qtd * preco,2)
        print(f" O total do pedido é R$ {total}")

    elif cod == 105:
        preco = 2.2
        qtd = int(input("Qual a quantidade do produto? "))
        total = round(qtd * preco,2)
        print(f" O total do pedido é R$ {total}")

    elif cod == 106:
        preco = 1
        qtd = int(input("Qual a quantidade do produto? "))
        total = round(qtd * preco,2)
        print(f" O total do pedido é R$ {total}")
else:
    print("Código Inválido")