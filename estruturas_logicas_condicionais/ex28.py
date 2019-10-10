import math
print("""
Escolha uma das opções a seguir para calcular a média de três valores inteiros:
[A] - Média Geométrica
[B] - Média Ponderada
[C] - Média Harmônica 
[D] - Média Aritmética
""")

ope = input("Sua opção? ").upper()

if ope == "A":

    a = int(input("Insira um número inteiro: "))

    b = int(input("Insira um número inteiro: "))

    c = int(input("Insira um número inteiro: "))

    raiz_cubica = round((a*b*c) ** 1/3,2)

    print(f'A média Geométrica é {raiz_cubica}.')

elif ope == "B":

    a = int(input("Insira um número inteiro: "))

    b = int(input("Insira um número inteiro: "))

    c = int(input("Insira um número inteiro: "))

    resultado = round((a + 2*b + 3*c)/6,2)

    print(f'A média Ponderada é {resultado}.')

elif ope == "C":

    a = int(input("Insira um número inteiro: "))

    b = int(input("Insira um número inteiro: "))

    c = int(input("Insira um número inteiro: "))

    resultado = round(1/((1/a) + (1/b) + (1/c)),2)

    print(f"A média Harmônica é: {resultado}.")

elif ope == "D":

    a = int(input("Insira um número inteiro: "))

    b = int(input("Insira um número inteiro: "))

    c = int(input("Insira um número inteiro: "))

    resultado = (a+b+c)/3

    print(f'A média Aritmética é {resultado}.')

else:
    print("Opção Inválida!")