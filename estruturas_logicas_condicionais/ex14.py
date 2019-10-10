nome = input("Olá! Digite seu nome: ")
print(f"""{nome},
Bem-vindo(a) ao sistema de cálculo de notas!
Coloque as notas das respectivas avaliações, lembre-se que as notas devem ser de 0 a 10.
""")

trab_lab = float(input('Digite a nota do Trabalho de Laboratório: '))

ava_semestral = float(input('Digite a nota da Avaliação Semestral: '))

ex_final = float(input('Digite a nota do Exame Final: '))

media = round((trab_lab*2 + ava_semestral*3 + ex_final*5)/10,2)

if 0<= trab_lab <= 10 and 0<= ava_semestral <= 10 and 0<= ex_final <= 10:
    if 0 <= media <= 2.9:
        print(f'Sua média foi {media}. Você foi REPROVADO.')
    elif 3 <= media <= 4.9:
        print(f'Sua média foi {media}. Você está na RECUPERAÇÃO.')
    else:
        print(f'Sua média foi {media}. Parabéns, você está APROVADO.')
else:
    print('Você precisa inserir as notas de 0 a 10. TENTE NOVAMENTE!')