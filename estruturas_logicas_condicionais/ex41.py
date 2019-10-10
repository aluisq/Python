dado_imc = round(float(input("Informe qual é o seu IMC: ")), 2)

if dado_imc <= 18.5:
    print("Abaixo do Peso")

elif 18.6 <= dado_imc <= 24.9:
    print("Saudável")

elif 25 <= dado_imc <= 29.9:
    print("Peso em Excesso")

elif 30 <= dado_imc <= 34.9:
    print("Obesidade Grau I")

elif 35 <= dado_imc <= 39.9:
    print("Obesidade Grau II (Severa)")

elif dado_imc > 40:
    print("Obesidade Grau III (Mórbida)")

else:
    print("IMC inválido.")
