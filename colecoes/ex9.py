vetor = []

x = 0


while x < 6:

    num = abs((int(input("Digite um número: "))))

    if num % 2 == 0:

        x += 1

        num = vetor.append(num)

    else:
        num = abs((int(input("Digite um número: "))))

print(vetor[::-1])