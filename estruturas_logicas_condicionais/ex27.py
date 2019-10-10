idade = int(input("Nadador, informe sua idade: "))

if  5 <= idade <= 7:
    print('Sua categoria é INFANTIL A.' )

elif 8 <= idade <= 10:
    print("Sua categoria é INFANTIL B")

elif 11 <= idade <13:
    print("Sua categoria é JUVENIL A")

elif 14 <= idade <= 17:
    print("Sua categoria é JUVENIL B")

else:
    print("Sua categoria é SÊNIOR")