numero = abs(int(input("Digite um número: ")))

while numero % 2 == 0:

    numero = abs(int(input("Digite um número: ")))

for i in range(1,numero + 1, 2):

    print(i)