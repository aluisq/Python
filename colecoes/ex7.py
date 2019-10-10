vetor1 = []

x = 0

while x < 10:

    valor = vetor1.append(int(input("Digite um número: ")))

    x += 1

print(f"O maior valor do conjunto: {vetor1} é {max(vetor1)}")

max = max(vetor1)

print(f"A posição do número com o maior valor dentro da lista é: {vetor1.index(max)} posição.")
