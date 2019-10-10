numero = abs(int(input("Digite um número: ")))

while numero % 2 != 0:

    numero = abs(int(input("Digite um número: ")))

if numero % 2 == 0:

    for i in range(0,numero + 1, 2):

        x = numero - i

        print(x)
else:
    print("Algo está errado.")