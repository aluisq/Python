salario = float(input("Informe o salário do cliente: "))

valor_emprestimo = float(input("Informe o valor do empréstimo : "))

if valor_emprestimo > 0.2*salario:
    print(f"Empréstimo não concedido.")
else:
    print("Empréstimo concedido")