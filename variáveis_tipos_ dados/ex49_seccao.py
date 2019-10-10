print("Desejo todo o sucesso em seu experimento biológico, deixe que eu registre o tempo de inicio e de duração.")

h = int(input("Digite a hora (H): "))

m = int(input("Digite o(s) minuto(s): "))

s = int(input("Digite o(s) segundo(s): "))


print("Por gentileza, informe a duração do experimento")


dh = int(input("Digite a hora (H): "))

dm = int(input("Digite o(s) minuto(s): "))

ds = int(input("Digite o(s) segundo(s): "))

print(f"""
O seu experimento está marcado para terminar às {h+dh} hora(s) {m + dm} minuto(s) e {s + ds} segundo(s).
""")