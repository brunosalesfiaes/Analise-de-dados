import pandas as pd
from pathlib import Path

base = Path(r"c:\Users\BRUNO\OneDrive\Documentos\Desktop\Impresorajava\Analise de dados")
arquivo_original = base / "dados" / "base_clientes.csv"
arquivo_saida = base / "dados" / "base_clientes_import.csv"

try:
    df = pd.read_excel(arquivo_original, sheet_name='Clientes')
except Exception as exc:
    raise RuntimeError(f"Não foi possível abrir o arquivo '{arquivo_original}'. Verifique se ele é um Excel real ou um CSV normal. Detalhe: {exc}")

colunas = ['Nome', 'Telefone', 'Valor Contribuído (R$)', 'Forma de Pagamento']
if not all(c in df.columns for c in colunas):
    raise ValueError(f"Colunas esperadas não encontradas: {list(df.columns)}")

df = df[colunas].copy()
df.columns = ['nome', 'telefone', 'valor_contribuido', 'forma_pagamento']
df['valor_contribuido'] = df['valor_contribuido'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)

df.to_csv(arquivo_saida, index=False, encoding='utf-8', sep=',', quotechar='"')
print(f"Arquivo gerado: {arquivo_saida}")
print(f"Linhas: {len(df)}")
print(df.head(3).to_dict(orient='records'))
