import math

num = int(input("Digite um número inteiro: "))

if num < 0:
    print("Número inválido.")
else:
    log = round(math.log(num,10),2)
    print(f"O logaritmo do número {num} é: {log}")