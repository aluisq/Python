ref_arquivo = open("teste_python.txt","r")

for linha in ref_arquivo:
    valores = linha.split(",")
    print(valores)
