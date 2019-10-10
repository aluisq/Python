vetor1 = []

x = 0

while x < 8:
    valor = vetor1.append(int(input("Digite um número: ")))
    x += 1

print(f"O número de elementos na lista é: {len(vetor1)}")

y = abs(int(input("Escolha a posição do elemento da lista (0-7):")))

if y < len(vetor1):

    z = abs(int(input("Escolha a posição do elemento da lista (0-7):")))

    if z < len(vetor1):

        soma = vetor1[y] + vetor1[z]


        print(f"A Soma do elemento na posição [{y}]:{vetor1[y]} e [{z}]:{vetor1[z]} é: {soma}")

    else:
        print("Valor maior do que o número de elementos")
else:
    print("Valor maior do que o número de elementos")