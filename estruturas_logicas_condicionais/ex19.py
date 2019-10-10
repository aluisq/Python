x = int(input("Insira um número: "))


if x%3 == 0 and x%5 == 0:
    print("Número não desejado")
elif x%3 == 0:
    print("Número divisível por 3")
elif x%5 == 0:
    print("Número divisível por 5")

else:
    print(f" {x} nem é divisível por 3 nem por 5.")