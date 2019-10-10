from random import random

def jogar_moeda():
    if random() < 0.5:
        return "Cara"
    return "Coroa"

print(jogar_moeda())