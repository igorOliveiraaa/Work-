def menor_string(lista):
    if not lista:
        return None
    menor = lista[0]
    for string in lista:
        if len(string) < len(menor):
            menor = string
    return menor

lista = ["gato", "elefante", "cão", "hipopótamo"]
print(menor_string(lista))
