import math

print("Olá!")

sexo = input("Qual é o seu sexo? [M/F]").lower()

altura = round(float(input("Informe sua altura:  ")),2)

if sexo == "m":
    p = round((72.7*altura) - 58,2)
    print(f"Sua peso ideal é: {p}")
elif sexo == "f":
    p = round((62.1 * altura) - 44.7,2)
    print(f"Seu peso ideal é: {p}")
else:
    print("Você não colocou o seu sexo.")