print("""
Olá,
Seja Bem-Vindo(a) ao sistema de verificação de conceito.
""")

nome = input("Informe seu nome: ").title()

print(f"{nome}, preciso que você me informe alguns dados!")

nota = round(float(input("Qual foi a sua nota? ")),2)

falta = int(input("Informe o seu número de faltas: "))

if falta <= 20:

    if 9 <= nota <= 10:
        print("Seu conceito é: A")

    elif 7.5 <= nota <= 8.9:
        print("Seu conceito é: B")

    elif 5 <= nota <= 7.4:
        print("Seu conceito é: C")

    elif 4 <= nota <= 4.9:
        print("Seu conceito é: D ")

    elif 0 < nota <= 3.9:
        print("Seu conceito é: E")
    else:
        print("Nota Inválida.")

elif falta > 20:

    if 9 <= nota <= 10:
        print("Seu conceito é: B")

    elif 7.5 <= nota <= 8.9:
        print("Seu conceito é: C")

    elif 5 <= nota <= 7.4:
        print("Seu conceito é: D")

    elif 4 <= nota <= 4.9:
        print("Seu conceito é: E ")

    elif 0 < nota <= 3.9:
        print("Seu conceito é: E")
    else:
        print("Nota Inválida.")

else:
    print("Número de faltas inválido.")