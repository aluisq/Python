"""
import random

x = random.randint(0,10)

print(x)
"""



import random

cont = 0
contPar = []
contaImpar = []

while cont < 10:
  x = random.randint(0,10)
  print(x)
  if x % 2 == 0:
    contPar.append(x)
  else:
    contaImpar.append(x)
  cont += 1

print("-------Quantidade de valores PAR - AMANDA---------")
print(len(contPar))
print("--------Quantidade de valores ÍMPARES- ARTHUR-----------")
print(len(contaImpar))
print("----------------")

if len(contPar) > len(contaImpar):
    print("Amanda - Ganhou")
else:
    print("Arthur - Ganhou")
