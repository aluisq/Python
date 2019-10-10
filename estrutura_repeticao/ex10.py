numero = int(input("Digite um número: "))

if numero % 2 == 0:
    # números pares
    x = 1

    y = numero

    soma = 0

    while x <= 50:

        x += 1

        y += 2

        soma += y

    print(soma)

elif numero % 2 != 0:
    # números ímpares

    x = 1

    y = numero - 1

    soma = 0

    while x <= 50:

        x += 1

        y += 2

        soma += y

    print(soma)

else:
    print("Número inválido")
