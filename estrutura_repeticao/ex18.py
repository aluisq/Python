print("Informe cinco números!")
x = 1

lista = []

while x <= 5:
    x += 1
    numero = lista.append(abs(int(input("Digite um número: "))))

print(f"O maior número digitado é: {max(lista)}. Quantidade de vezes que ele apareceu: {lista.count(max(lista))}.")