x = 1
lista =[]

while x <= 10:

    y = lista.append(int(input("Digite um número: ")))
    x += 1

print(f"Valor máximo digitado: {max(lista)}")
print(f"Valor mmínimo digitado: {min(lista)}")