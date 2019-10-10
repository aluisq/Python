import math

a = float(input("Digite um número qualquer: "))

if a > 0:
    b = round(math.sqrt(a),2)
    print(f"A raíz quadrada de {a} é {b}. ")
else:
    b = round(a*a,2)
    print(f"{a} elevado ao quadrado é {b}")



