import math
y = 0

vetor1 = []

while y < 10:
    num = vetor1.append(int(input('Digite um número: ')))
    y += 1
print(vetor1)

vetor2 = []

x = 0

while x < len(vetor1):
    valor = vetor2.append(vetor1[x]**2)
    x += 1

print(vetor2)