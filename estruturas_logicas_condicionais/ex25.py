
import math

print("""
Olá, sabemos que uma equação do segundo grau é estruturada da seguinte maneira: ax² + bx + c = 0
Esse programa foi desenvolvido para calcular suas possíveis raízes!
Vamos começar!?
""")

a = float(input("""Insira o valor correspondente ao parâmetro "a" da equação do segundo grau: """))

b = float(input("""Insira o valor correspondente ao parâmetro "b" da equação do segundo grau: """))

c = float(input("""Insira o valor correspondente ao parâmetro "c" da equação do segundo grau: """))

print(f"Sua equação é : {a}x² + {b}x + {c}")

delta = (b ** 2) - 4*a*c


if delta >= 0:
    raiz_delta = math.sqrt(delta)

    x1 = round((-b + raiz_delta)/ (2*a),2)

    x2 = round((-b - raiz_delta)/(2*a),2)

    print(f"Sua equação tem duas raízes reais e distintas, sendo x1 = {x1} e x2 = {x2}.")

elif delta == 0:

    x = round((- b)/2*a ,2)

    print(f" Sua equação tem duas raízes reais e iguais, sendo x1 e x2 igual a {x} .")

else:
    print("Não existem raízes para sua equação.")
