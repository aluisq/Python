print("""
Olá!
Escolha a sua opção:
[1] - Soma de dois números.
[2] - Diferença entre 2 números (maior pelo menor).
[3] - Produto entre 2 números.
[4] - Divisão entre 2 números ( o denominador não pode ser zero.) 
""")

calculo = int(input("Coloque o opção desejada: "))

if calculo == 1:

    a = round(float(input("Digite o primeiro número: ")),2)
    b = round(float(input("Digite o segundo número: ")),2)
    c = a + b
    print(f"A soma de {a} com {b} é {c}.")

elif calculo == 2:

    a = round(float(input("Digite o primeiro número: ")),2)
    b = round(float(input("Digite o segundo número: ")),2)

    if a >= b:
        c = a - b
        print(f"A diferença entre {a} e {b} é {c}.")
    else:
        c = b - a
        print(f"A diferença entre {b} e {a} é {c}.")
elif calculo == 3:

    a = round(float(input("Digite o primeiro número: ")),2)
    b = round(float(input("Digite o segundo número: ")),2)
    c = a * b
    print(f"O produto de {a} e {b} é {c}.")

elif calculo == 4:

    a = round(float(input("Digite o numerador: ")),2)
    b = round(float(input("Digite o denominador: ")),2)

    if b == 0:
        print("O denominador igual a zero.")
    else:
        c = a/b
        print(f"A divisão entre {a} e {b} é {c}")

else:
    print("Opção inválida.")