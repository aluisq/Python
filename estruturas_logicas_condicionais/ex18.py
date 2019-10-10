print("""
Operações matemáticas disponíveis:
[1] - Adição
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
""")
ope_mat = int(input("Insira o número da operação desejada? "))

if ope_mat == 1:

    a = round(float(input("Digite o primeiro valor: ")),2)

    b = round(float(input("Digite o segundo valor: ")),2)

    soma = a + b

    print(f"A soma é {soma}.")

elif ope_mat == 2:

    a = round(float(input("Digite o primeiro valor: ")), 2)

    b = round(float(input("Digite o segundo valor: ")), 2)

    if a > b:
        subtracao = a - b
        print(f"A subtração é {subtracao}")

    else:
        sub = b - a

    print(f'A subtração é {sub}')

elif ope_mat == 3:

    a = round(float(input("Digite o primeiro valor: ")), 2)

    b = round(float(input("Digite o segundo valor: ")), 2)

    mut = a*b

    print(f"A multiplicação é {mut}.")
elif ope_mat == 4:

    a = round(float(input("Digite o primeiro valor: ")), 2)

    b = round(float(input("Digite o segundo valor: ")), 2)

    if a > b:
        div = a/b
        print(f"A divisão de {a} por {b} é {div}.")
    else:
        div = b/a

    print(f"A divisão de {b} por {a} é {div}.")
else:
    print("Operação não encontrada, por favor, tenha certeza que você está digitando: 1,2,3 ou 4.")
