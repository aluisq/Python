from random import random

x = 0
lista = []

while x <= 3:
    x+=1
    lista.append(random())

lista_1 = [round(numero,2) for numero in lista]

Arthur, Amanda, Adrielly, Henrique = lista_1

print(f"Arthur: {round(Arthur * 100,2)} "
      f"Amanda: {round(Amanda * 100,2)}, "
      f"Adrielly: {round(Adrielly * 100,2)} "
      f"Henrique: {round(Henrique * 100,2)}")


#print([round(numero * 100,2) for numero in lista])