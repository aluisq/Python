import math
alt_degrau = float(input("Insira a altura do degrau da escada em centímetros: "))

alt_desejada = float(input("Insira a altura a ser alcançada em metros: "))

x = math.ceil((alt_desejada/alt_degrau)*100)

print(f"Você precisará subir {x} degrau(s) para chegar na altura desejada.")