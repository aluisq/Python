ano = int(input("Coloque um ano qualquer e vamos verificar se ele é bissexto: "))

if ano % 4 == 0 or ano % 4 == 0 and ano / 100 is not int:
    print(f"O ano de {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto.")