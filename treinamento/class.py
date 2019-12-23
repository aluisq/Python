
#definindo a classe pessoa
class Person:
    greet = "Saudações" #atributo
    def __init__(self, name, age): #atributos de instância
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is" + " " + self.name)

    def aprovarContrato(self):
        x = range(100)
        y = []
        print("contratos aprovados")
        z = list(filter(lambda x: x % 2 ==0, x))
        y.extend(z)
        print(y)



#passando a classe pessoa para a variável p1
p1 = Person("Arthur", 27)

#consultando

print(p1.greet)

print(p1.name)


print(p1.age)

p1.myfunc()

p1.aprovarContrato()
