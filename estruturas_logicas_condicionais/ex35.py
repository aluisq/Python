ano = int(input("Informe o ano: "))

if ano % 4 == 0 or ano % 4 == 0 and ano / 100 is not int:
    mes = int(input("Insira o mês: "))

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = int(input("Insira a data: "))
        if 1 <= dia <= 30:
            print(f"A data {dia}/{mes}/{ano} é válida")
        else:
            print(f"A data {dia}/{mes}/{ano} é inválida")

    elif mes == 2:
        dia = int(input("Insira a data: "))
        if 1 <= dia <= 29:
            print(f"A data {dia}/{mes}/{ano} é válida")
        else:
            print(f"A data {dia}/{mes}/{ano} é inválida.")
    else:
        dia = int(input("Insira a data: "))
        if 1 <= dia <= 31:
            print(f"A data {dia}/{mes}/{ano} é válida.")
        else:
            print(f"A data {dia}/{mes}/{ano} é inválida.")
else:
    mes = int(input("Insira o mês: "))
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = int(input("Insira a data: "))
        if 1 <= dia <= 30:
            print(f"A data {dia}/{mes}/{ano} é válida")
        else:
            print(f"A data {dia}/{mes}/{ano} é inválida")
    elif mes == 2:
        dia = int(input("Insira a data: "))
        if 1 <= dia <= 28:
            print(f"A data {dia}/{mes}/{ano} é válida")
        else:
            print(f"A data {dia}/{mes}/{ano} é inválida.")
    else:
        dia = int(input("Insira a data: "))
        if 1 <= dia <= 31:
            print(f"A data {dia}/{mes}/{ano} é válida.")
        else:
            print(f"A data {dia}/{mes}/{ano} é inválida.")
