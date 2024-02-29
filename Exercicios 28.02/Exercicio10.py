def calcular_frequencia(texto, palavra):
    frequencia = 0
    palavras = texto.split()
    
    for p in palavras:
        if p == palavra:
            frequencia += 1
            
    return frequencia
meu_texto = "O rato roeu a roupa do rei de Roma"
minha_palavra = "roeu"
print(calcular_frequencia(meu_texto, minha_palavra))
