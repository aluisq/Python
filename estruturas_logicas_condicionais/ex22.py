ano_nasc = int(input("Olá, insira o ano do seu nascimento: "))

tempo_serv = int(input("Digite o tempo de serviço: "))

idade = 2019 - ano_nasc

if idade >= 65 or tempo_serv == 30 or idade >= 60 and tempo_serv >= 25:
    print(f"Você já pode se aposentar!")
else:
    print("Você ainda não está enquadrado nas característica de um aposentado.")