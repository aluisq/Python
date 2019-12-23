
nome = (input("Olá estudante, infome seu nome: "))


print(f"Prezado(a) {nome}, preciso que você me informe suas notas para avaliarmos sua situação acadêmica, vamos começar!")

nota1= float(input("Insira sua primeira nota: "))
while nota1 > 10 or nota1 < 0:
    print("-------------------------")
    print("NOTA INVÁLIDA")
    print("-------------------------")
    nota1= float(input("Insira sua primeira nota: "))

nota2= float(input("Insira sua segunda nota: "))
while nota2 > 10 or nota2 < 0:
    print("-------------------------")
    print("NOTA INVÁLIDA")
    print("-------------------------")
    nota2= float(input("Insira sua segunda nota: "))

media = round((nota1+nota2)/2,2)

if media < 7:
    print(f"Sua média é {media}")
    print("REPROVADO")


"""nota2= int(input("Insira sua segunda nota: "))

while 0 > nota2 >= 10:
    nota2= int(input("Insira sua segunda nota: "))

nota3 = int(input("Insira sua terceira nota: "))

while 0 >Arthur

nota4 = int(input("Insira sua quarta nota: "))


print(f"A soma dos números é {}") """
