import math

a = int(input("Digite a coordenada X: "))

b = int(input("Digite a coordenada Y: "))


distancia = round(math.sqrt(a*a + b*b),2)


print(f"A distância do ponto, com coordenadas ({a},{b}), para o centro da circunferência (0,0) é: {distancia} ")


