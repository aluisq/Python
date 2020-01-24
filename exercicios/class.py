
#definindo a classe pessoa
class Person:
    #todos aquele que são instanciados pelo Person recebem o Greet
    #atributo global

    greet = "Saudações"

    def __init__(self, name, age): #atributos de instância, lembrando que o init é o método construtor, faz a abstração
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is" + " " + self.name)

    def aprovarContrato(self):
        #colocar o range até 100
        x = range(100)
        #criar uma lista
        y = []
        print("contratos aprovados")
        #criando um filtro junto com a funcao lambda
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
