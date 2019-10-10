numero = abs(int(input("Digite um número: ")))

while numero % 2 == 0:

    numero = abs(int(input("Digite um número: ")))

for i in range(0,numero, 2):

    x = numero - i

    print(x)