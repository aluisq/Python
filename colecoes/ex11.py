vetor = []

x = 0

soma = 0

qt_negativo = 0

while x < 10:

    num = int(input("Digite um número: "))

    if num > 0:

        soma += num

        valor = vetor.append(num)

        x += 1
    else:
        qt_negativo += 1

        valor = vetor.append(num)

        x += 1

print(vetor)

print(f"A soma dos números positivos é : {soma}")

print(f"A quantidade de números negativos é: {qt_negativo}")