dia = int(input("Digite o número de dias trabalhado pelo encanador: "))

salario = 30 * dia

salario_liquido = salario * 0.92

imposto = salario * 0.08

print(f"O salário pago ao encanador será: R$ {salario_liquido}")
print(f"O imposto de renda será: R$ {imposto}")