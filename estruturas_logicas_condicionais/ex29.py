nome = input("Digite seu nome: ").title()

print(f"""
Olá {nome}, 
Seja bem-vindo(a) ao sistema de aprendizagem Galaxy Adventure!

Hoje vamos conhecer um pouco sobre uma operação matemática: a ADIÇÃO. 

Vamos brincar com dois números [78] e [56].

""")

a = 78

b = 56

ready_play = input("Para começar aperte ENTER.")

q1 = int(input("""Qual o resultado da soma 78 + 56?  
[105] [134] ou [114]: """))

print(f"A soma de {a} + {b} é igual a 134.")
print("----------------------")

if q1 == 134:
    x = 1
else:
    x = 0

q2 = input("O resultado é maior que 100? [SIM/NÃO] ").upper()

print("A reposta é: SIM.")
print("----------------------")

if q2 == "SIM" or q2 == "S" or q2 == "[SIM]":
    y = 1
else:
    y = 0

q3 = input("O resultado é uma centena? [SIM] ou [NÃO]").upper()

print("Sim. Todo numéro entre 100 e 999 é uma centena, logo 134 é uma centena.")
print("----------------------")

if q3 == "SIM" or q3 == "S" or q3 == "[SIM]":
    z = 1
else:
    z = 0

q4 = int(input("Quantos dígitos tem o resultado? [1], [2] ou [3] "))

if q4 == 3:
    w = 1
else:
    w = 0

print("3 dígitos")
print("----------------------")

q5 = input("134 é o mesmo que somar 100 + 34? [SIM] ou [NÃO]").upper()
print("Sim")
print("----------------------")

if q5 == "SIM" or q5 == "S" or q5 == "[SIM]":
    k = 1
else:
    k = 0

soma = x + y + z + w + k

if soma <= 3:
    print(f"Sua pontuação foi {soma}/5, você pode melhorar, tente novamente!")
elif  3 < soma <= 5:
    print(f"""Sua pontuação foi {soma}/5, você etá no caminho certo!
Lembre-se que conhecimento nunca é demais. Quanto é 234 + 450?
""")

