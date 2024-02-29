def intersecao_listas(lista1, lista2):
    intersecao = [valor for valor in lista1 if valor in lista2]
    return intersecao

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(intersecao_listas(lista1, lista2)) 
