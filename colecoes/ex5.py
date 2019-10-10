vetor1 = []

x = 0

while x < 4:

    valor = vetor1.append(int(input("Digite um número: ")))


    x += 1

y = 0

for num in vetor1:
    if num % 2 == 0:
        y += 1
    else:
        y = y

if y == 0:

    print(f"Não existe número par no conjunto: {vetor1}")

elif y == 1:

    print(f"No conjunto: {vetor1} existe {y} número par.")

else:
    print(f"No conjunto: {vetor1} existem {y} números pares.")
