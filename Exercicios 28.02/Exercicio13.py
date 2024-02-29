def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

nome_arquivo = "meu_arquivo.txt"
print(ler_arquivo(nome_arquivo))
