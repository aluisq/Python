import math
g = int(input('Digite o valor do ângulo em graus: '))

r = round((g*math.pi)/180,2)

print(f'Para {g} graus temos {r} radianos.')