real = float(input('Digite a quantia em real: '))
dolar = float(input('Digite a cotação do dólar: '))

valor = round(real/dolar,2)

print(f'Para a quantia de R$ {real} reais é possível comprar U$ {valor} dólares')