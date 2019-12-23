tempo = int(input("Digite um valor inteiro de segundos(unidade de tempo): "))

h = tempo // 3600

m = (tempo%3600)//60

s = (tempo%3600)%60

print(f"""
Em {tempo} segundo(s) temos:
{h} Hora(s) {m} Minuto(s) e {s} Segundo(s) 
""")