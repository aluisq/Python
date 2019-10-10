import math

a = float(input("Digite um número qualquer: "))

if a > 0:
    print(f"A raíz quadrada de {a} é {round(math.sqrt(a),2)}")
else:
    print("Número inválido, insira um número positivo.")