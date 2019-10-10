import math

nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))

nota3 = float(input("Digite a sua terceira nota: "))


media = round((1*nota1 + 1*nota2 + 2*nota3)/4, 2)

if nota1 <= 100 and nota2 <= 100 and nota3 <= 100:
    if media > 60:
        print(f"Sua média foi {media}. Parabéns, você foi APROVADO.")
    else:
        print(f"Sua média foi {media}. Você foi REPROVADO.")
else:
    print("Por gentileza, reinicie o programa e lembre-se que cada nota não pode ser superior a 100!")