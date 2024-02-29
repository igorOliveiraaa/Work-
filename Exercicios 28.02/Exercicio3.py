def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

texto = "Olá, como você está?"
print(contar_palavras(texto)) 
