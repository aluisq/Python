a = float(input("""Insira o valor do lado "A" do triângulo: """))

b = float(input("""Insira o valor do lado "B" do triângulo: """))

c = float(input("""Insira o valor do lado "C" do triângulo."""))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Esse triângulo é Equilátero.")
    elif a == b or a == c or b == c:
        print("Esse trinângulo é Isósceles.")
    else:
        print("Esse triângulo é Escaleno.")

else:
    print("Não é um triângulo.")