n = int(input("digite um número: "))

if n % 2 == 0:

    x = 1

    y = n - 1
    
    while x <= n:

        x += 1

        y += 2

        print(y)

elif n % 2 != 0:

    x = 1

    y = n

    while x <= n:

        x += 1

        y += 2

        print(y)

else:
    print("Valor Inválido.")
