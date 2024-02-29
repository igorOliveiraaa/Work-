mes_menos_vendas = df.loc[df["valor"].idxmin()]["mês"]
print(f"O mês com menos vendas foi {mes_menos_vendas}.")
