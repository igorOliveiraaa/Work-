import pandas as pd

df = pd.read_csv("vendas.csv")
mes_mais_vendas = df.loc[df["valor"].idxmax()]["mês"]
print(f"O mês com mais vendas foi {mes_mais_vendas}.")
