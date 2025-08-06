import os
import pandas as pd

# ~~ Carregar os dados do arquivo CSV
df = pd.read_csv("/Users/thaluanegomes/analise-transacoes/dados/transacoes.csv")

# ~~ Regra 1: Transações com valor acima de R$ 3.000
suspeitas_valor = df[df["valor"] > 3000]

# ~~ Regra 2: Mesmo cliente fazendo transações em cidades diferentes no mesmo dia
fraudes_local = df.groupby(["cliente_id", "data"])["localizacao"].nunique()
clientes_suspeitos = fraudes_local[fraudes_local > 1].index.get_level_values(0)
suspeitas_local = df[df["cliente_id"].isin(clientes_suspeitos)]

# ~~ Juntar transações suspeitas e evitar duplicação com drop_duplicates
resultado = pd.concat([suspeitas_valor, suspeitas_local]).drop_duplicates()

print(resultado)
# ~~ Salvar o relatório
caminho_output = "/Users/thaluanegomes/analise-transacoes/output"
os.makedirs(caminho_output,exist_ok=True)
resultado.to_csv(f"{caminho_output}/relstorio_fraudes.csv", index=False)
print("Análise concluída! Relatório gerado em /output/relatorio_fraudes.csv")
