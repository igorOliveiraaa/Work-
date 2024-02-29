def contar_ocorrencias(frase, palavra):
    palavras = frase.split()
    return palavras.count(palavra)

frase = "O gato está no telhado e o outro gato está no jardim."
palavra = "gato"
print(contar_ocorrencias(frase, palavra))  
