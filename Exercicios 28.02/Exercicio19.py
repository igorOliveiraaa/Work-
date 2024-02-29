df_vendedores = pd.read_csv("vendedores.csv")
soma_vendas_por_vendedor = df_vendedores.groupby("nome")["valor_venda"].sum()
print(soma_vendas_por_vendedor)
