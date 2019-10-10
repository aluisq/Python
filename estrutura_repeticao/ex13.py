numero = abs(int(input("Digite um número: ")))

while numero % 2 != 0:

    print("""
    __________________________
    
         Número inválido
    __________________________
    """)

    numero = abs(int(input("Digite um número: ")))

    if numero % 2 == 0:

        for i in range(0,numero + 2, 2):

            print(i)

    else:
        print("Algo está errado.")
