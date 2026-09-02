import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

PERC_COMISSAO = 0.05
COLUNAS_ANALISE = ["cidade", "vendedor", "produto", "genero_cliente", "forma_pagto"]
COLUNAS_NUMERICAS = ["preco", "comissao"]
FUNCOES_AGREGACAO = {"soma": "sum", "contagem": "count"}

caminho_datasets = "datasets"

df_compras = pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",", index_col=0, parse_dates=True)
df_lojas = pd.read_csv(f"{caminho_datasets}/lojas.csv", sep=";", decimal=",", index_col=0)
df_produtos = pd.read_csv(f"{caminho_datasets}/produtos.csv", sep=";", decimal=",", index_col=0)

df_produtos = df_produtos.rename(columns={"nome": "produto"})

df_compras = df_compras.reset_index()

# Remove a coluna 'preco' antiga antes do merge, pra não duplicar (preco_x/preco_y)
df_compras = df_compras.drop(columns=["preco"])

df_compras = pd.merge(
    left=df_compras,
    right=df_produtos[["produto", "preco"]],
    on="produto",
    how="left"
)

df_compras = df_compras.set_index("data")

# Garante que o índice é datetime antes de usar .date
df_compras.index = pd.to_datetime(df_compras.index, format="mixed")

df_compras["comissao"] = df_compras["preco"] * PERC_COMISSAO

indice_dinamico = st.sidebar.multiselect("Selecione os índices", COLUNAS_ANALISE)
colunas_filtradas = [c for c in COLUNAS_ANALISE if c not in indice_dinamico]
coluna_dinamica = st.sidebar.multiselect("Selecione as colunas", colunas_filtradas, default=colunas_filtradas, key="colunas_selecionadas")
valor_analise = st.sidebar.selectbox("Selecione o valor)", COLUNAS_NUMERICAS, key="valor_analise")
metricac_analise = st.sidebar.selectbox("Selecionar a métrica", FUNCOES_AGREGACAO.keys(), key="funcao_agregacao")

if len(indice_dinamico) > 0 and len(coluna_dinamica) > 0:
    metrica = FUNCOES_AGREGACAO[metricac_analise]
    compras_dinamica = pd.pivot_table(
        df_compras,
        index=indice_dinamico,
        columns=coluna_dinamica,
        values=valor_analise,
        aggfunc=metrica,
    )
    compras_dinamica["TOTAL_GERAL"] = compras_dinamica.sum(axis=1)
    compras_dinamica.loc["TOTAL_GERAL"] = compras_dinamica.sum(axis=0).to_list()
    st.dataframe(compras_dinamica)