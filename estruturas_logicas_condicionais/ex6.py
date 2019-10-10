import math

a = int(input("Digite um número qualquer: "))

b = int(input("Digite um número qualquer: "))



if a > b :
    print(f"{a} é o maior número")
    c = a - b
    print(f"A diferença entre os números digitados é: {c}")
else:
    print(f"{b} é o maior número")
    c = b - a
    print(f"A diferença entre os números digitados é: {c}")
