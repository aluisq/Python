sal_base = float(input("Qual é o seu salário base? "))

sal_grat = round((sal_base)*1.05,2)

imposto = round((sal_base)*0.07,2)

salario = sal_grat - imposto

print(f'O salário a receber pelo funcionário é: R$ {salario}.')