import random

def embaralhar_lista(lista):
    random.shuffle(lista)
    return lista

minha_lista = [1, 2, 3, 4, 5]
print(embaralhar_lista(minha_lista))
