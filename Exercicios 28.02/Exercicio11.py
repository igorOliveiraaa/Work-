def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_na_lista(lista):
    return [n for n in lista if eh_primo(n)]

lista = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(primos_na_lista(lista))
