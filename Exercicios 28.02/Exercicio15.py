import json

nome_arquivo = "dados.json"

with open(nome_arquivo, "r") as arquivo:
    dados = json.load(arquivo)

print(dados)
