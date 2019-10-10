import math

b_menor = round(float(input('Coloque o valor da base menor: ')),2)

b_maior = round(float(input('Coloque o valor da base maior: ')),2)

h = float(input('Coloque o valor da altura: '))

if b_maior > 0 and b_menor > 0:
    area = round(((b_menor + b_maior)*h)/2,2)
    print(f"A área do trapézio é {area}.")
else:
    print('Valor inválido, por favor, verifique se há algum número menor que zero e insira novamente os dados.')