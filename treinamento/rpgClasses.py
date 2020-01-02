class Humano:
    contador = 0

    def __init__(self,nome,idade,peso,altura):

        self.id = Humano.contador + 1
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        Humano.contador = id

    def profissao(self,forca,sabedoria,velocidade):

        if 7 <= forca and 2 >= sabedoria and 3 >= velocidade:
            return "Bárbaro"
        elif 5 <= forca < 7 and 5 <= sabedoria <= 7 and velocidade >= 7:
            return "Ladino"
        elif  forca <= 2 and sabedoria >= 7 and velocidade <= 3:
            return "Feiticeiro"
        else:
            return "Rooker"

jogador1 = Humano("Victor",26,102,1.91)


print(jogador1.__dict__)
print(f"{jogador1.nome} é da classe {jogador1.profissao(7,1,1)}")
