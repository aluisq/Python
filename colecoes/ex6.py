vetor1 = []

x = 0

while x < 10:

    valor = vetor1.append(int(input("Digite um número: ")))

    x += 1

print(f"O maior valor do conjunto: {vetor1} é {max(vetor1)}.")

print(f"O menor valor do conjunto: {vetor1} é {min(vetor1)}.")