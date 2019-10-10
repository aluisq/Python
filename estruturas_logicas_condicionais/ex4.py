import  math

a = float(input("Digite um número qualquer: "))

if a > 0:
    b = round(a*a,2)
    c = round(math.sqrt(a),2)
    print(f"""
    O número {a} elevado ao quadrado é: {b}
    A raíz quadrada do número {a} é: {c}
    """)
else:
    print("Insira um número positivo")

