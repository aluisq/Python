produto = input("Qual o produto desejado para consulta? ")
preco = float(input("Qual o preço vigente do produto? "))

desconto = round(preco * 0.88,2)
economia = round(preco - desconto,2)
print(f'Parece que esse produto está em promoção! De {preco} por apenas {desconto}, uma economia de {economia} '
      f'reais')