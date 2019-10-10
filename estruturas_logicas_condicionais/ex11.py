num = int(input('Digite um número inteiro maior que zero e menor que 999: '))

if num > 0 and num < 999:
    valor = str(num)
    a = int(valor[0])
    b = int(valor[1])
    c = int(valor[2])
    soma = a + b + c
    print(f'A soma dos algorismo desse número é: {soma}')
else:
    print("Número Inválido.")