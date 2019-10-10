salario = float(input("Qual o seu salário atual? "))

if salario <= 500:

    salario_reajuste = salario * 1.25

    tempo = int(input("Quanto anos de serviço você tem na empresa? Se menor que um ano, digite 1. "))

    if tempo == 1:

        bonus = 0

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 1 < tempo <= 3:

        bonus = 100

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 3 < tempo <= 6:

        bonus = 200

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 6 < tempo <= 10:

        bonus = 300

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif tempo > 10:

        bonus = 500

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    else:
        print("tempo de serviço inválido.")

elif 500 < salario <= 1000:

    salario_reajuste = salario * 1.20

    tempo = int(input("Quanto anos de serviço você tem na empresa? Se menor que um ano, digite 1. "))

    if tempo == 1:

        bonus = 0

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 1 < tempo <= 3:

        bonus = 100

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 3 < tempo <= 6:

        bonus = 200

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 6 < tempo <= 10:

        bonus = 300

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif tempo > 10:

        bonus = 500

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    else:
        print("tempo de serviço inválido.")

elif 1000 < salario <= 1500:

    salario_reajuste = salario * 1.15

    tempo = int(input("Quanto anos de serviço você tem na empresa? Se menor que um ano, digite 1. "))

    if tempo == 1:

        bonus = 0

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 1 < tempo <= 3:

        bonus = 100

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 3 < tempo <= 6:

        bonus = 200

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 6 < tempo <= 10:

        bonus = 300

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif tempo > 10:

        bonus = 500

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    else:
        print("tempo de serviço inválido.")

elif 1500 < salario <= 2000:

    salario_reajuste = salario * 1.10

    tempo = int(input("Quanto anos de serviço você tem na empresa? Se menor que um ano, digite 1. "))

    if tempo == 1:

        bonus = 0

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 1 < tempo <= 3:

        bonus = 100

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 3 < tempo <= 6:

        bonus = 200

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 6 < tempo <= 10:

        bonus = 300

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif tempo > 10:

        bonus = 500

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    else:
        print("tempo de serviço inválido.")

elif salario > 2000:

    salario_reajuste = salario

    tempo = int(input("Quanto anos de serviço você tem na empresa? Se menor que um ano, digite 1. "))

    if tempo == 1:

        bonus = 0

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 1 < tempo <= 3:

        bonus = 100

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 3 < tempo <= 6:

        bonus = 200

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif 6 < tempo <= 10:

        bonus = 300

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    elif tempo > 10:

        bonus = 500

        novo_salario = round(salario_reajuste + bonus, 2)

        print(f"Seu novo salário é R$ {novo_salario}")

    else:
        print("tempo de serviço inválido.")

else:

    print(f"Valor inválido")
