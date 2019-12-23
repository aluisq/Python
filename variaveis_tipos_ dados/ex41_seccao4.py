valor_hora = float(input("Digite o valor por hora de trabalho: "))
hora_trabalhada = float(input("Quantas horas foram trabalhadas? "))

salario = round((valor_hora * hora_trabalhada)*1.1,2)

print(f'O seu salário foi atualizado com uma bonificação de 10% passando para R$ {salario}')