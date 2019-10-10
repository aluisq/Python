print("Teste do consumo veícular")

km = float(input("Informe quantos kilometros você percorreu: "))

litro = float(input("Informe quantos litros de gasolina você utilizou: "))

consumo = round(km/litro,2)

print(f"O carro está fazendo {consumo} km por litro.")

if consumo <= 8:
    print("VENDA o carro!")

elif 8 <= consumo <= 12:
    print("Econômico!")

else:
    print("Super econômico!")