ano = int(input("Informe o ano: "))

if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:

    mes = int(input("Informe o mês: "))

    if mes == 2:

        dia = int(input("Informe o dia: "))

        if 1 <= dia < 30:

            print(f"A data de {dia}/{mes}/{ano} é válida.")

        else:

            print("Data Inválida")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:

        dia = int(input("Informe o dia: "))

        if 1 <= dia < 31:

            print(f"A data de {dia}/{mes}/{ano} é válida.")

        else:

            print("Data Inválida.")

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

        dia = int(input("Informe o dia: "))

        if 1 <= dia < 32:

            print(f"A data de {dia}/{mes}/{ano} é válida.")

        else:

            print("Data Inválida.")

    else:

        print("Data Inválida.")

# caso seja alguma ano normal:

else:
    mes = int(input("Informe o mês: "))

    if mes == 2:

        dia = int(input("Informe o dia: "))

        if 1 <= dia < 29:

            print(f"A data de {dia}/{mes}/{ano} é válida.")

        else:

            print("Data Inválida")

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:

        dia = int(input("Informe o dia: "))

        if 1 <= dia < 31:

            print(f"A data de {dia}/{mes}/{ano} é válida.")

        else:

            print("Data Inválida.")

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

        dia = int(input("Informe o dia: "))

        if 1 <= dia < 32:

            print(f"A data de {dia}/{mes}/{ano} é válida.")

        else:

            print("Data Inválida.")

    else:

        print("Data Inválida.")
