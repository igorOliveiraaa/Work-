def encontrar_par_soma(lista, soma):
    hash_map = {}

    for i, numero in enumerate(lista):
        complemento = soma - numero
        if complemento in hash_map:
            return (lista[hash_map[complemento]], lista[i])
        hash_map[numero] = i

    return None
minha_lista = [1, 2, 3, 4, 5]
soma_desejada = 7
print(encontrar_par_soma(minha_lista, soma_desejada))
