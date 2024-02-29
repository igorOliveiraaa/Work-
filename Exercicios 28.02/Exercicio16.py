import os

diretorio = "/caminho/do/diretorio" 

conteudo_total = ""

for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_arquivo, "r") as arquivo:
            conteudo_total += arquivo.read()

print(conteudo_total)
