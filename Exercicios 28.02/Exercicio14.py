import pandas as pd

def ler_csv(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    return df

nome_arquivo = "meu_arquivo.csv"
print(ler_csv(nome_arquivo))
