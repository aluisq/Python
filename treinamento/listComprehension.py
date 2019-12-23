
#list_variable = [x for x in iterable]

#OR

#list_variable = [x for x in iterable]


x = [variavel for variavel in ("Arthur",25,45.9,True)]

print(x)



number = range(50)

print("TODOS OS NÚMEROS QUE SÃO PAR ATÉ 50")
y = [num for num in number if num%2==0] #também serve como um filtro

print(y)


#divisores em comum
print("NUMEROS QUE TEM O DIVISOR COMUM 3 E 5")
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)
