def k_maiores_elementos(lista, k):
    lista_indexada = list(enumerate(lista))
    lista_ordenada = sorted(lista_indexada, key=lambda x: x[1], reverse=True)
    k_maiores = lista_ordenada[:k]
    k_maiores_ordenados = sorted(k_maiores, key=lambda x: x[0])
    return [valor for indice, valor in k_maiores_ordenados]

lista = [1, 3, 4, 2, 7, 5, 6, 8, 9]

k = 3

print(k_maiores_elementos(lista, k))  
