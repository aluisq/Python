num = int(input('Digite um número de 1 a 7: '))

if 1 <= num <= 7:
    if num == 1:
        print('Domingo')
    if num == 2:
        print('Segunda-Feira')
    if num == 3:
        print('Terça-Feira')
    if num == 4:
        print('Quarta-Feira')
    if num == 5:
        print('Quinta-Feira')
    if num == 6:
        print('Sexta-Feira')
    if num == 7:
        print('Sábado')
else:
    print('Número inválido')