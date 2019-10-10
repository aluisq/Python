nome = input("Olá, digite seu nome: ").title()

print(f"{nome}, para classificarmos você precisamos saber alguns dados!")

peso = round(float(input("Qual o seu peso? ")),2)

altura = round(float(input("Qual a sua altura? ")),2)

if altura < 1.2 and peso <= 60:
    print(f"{nome} sua classificação é 'A'.")

elif 1.2 <= altura <= 1.7 and peso <= 60:
    print(f"{nome} sua classificação é 'B'.")

elif altura > 1.7 and peso <= 60:
    print(f"{nome} sua classificação é 'C'.")

elif altura < 1.2 and 60 < peso <= 90:
    print(f"{nome} sua classificação é 'D'.")

elif 1.2 < altura < 1.7 and 60 < peso <= 90:
    print(f"{nome} sua classificação é 'E'.")

elif altura > 1.7 and 60 < peso <= 90:
    print(f"{nome} sua classificação é 'F'.")

elif altura < 1.2 and peso > 90:
    print(f"{nome} sua classificação é 'G'.")

elif 1.2 < altura < 1.7 and peso > 90:
    print(f"{nome} sua classificação é 'H'.")

elif altura > 1.7 and peso > 90:
    print(f"{nome} sua classificação é 'I'.")

else:
    print(f"{nome} os p é 'I'.")