vetor = []

x = 0

while x < 5:

    num = float(input("Digite um número: "))

    if 0 <= num <= 10:

        valor = vetor.append(num)

        x += 1
    else:
        print("Nota Inválida, por favor, insira um valor entre 0 e 10.")
        num = float(input("Digite um número: "))


print(f"Notas: {vetor}")

media = round((sum(vetor)) / x, 2)

print(f"A média geral dos alunos foi: {media}")
