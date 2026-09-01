import streamlit as st
import pandas as pd

caminho_compras = "datasets/compras.csv"

df_compras = pd.read_csv(caminho_compras, sep=";", decimal=",", index_col=0)

colunas = list(df_compras.columns)

colunas_selecionadas = st.sidebar.multiselect("Selecione as colunas que deseja visualizar", colunas, default=colunas, key="colunas_selecionadas")

col1 , col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox("Selecione a coluna", [c for c in colunas if c not in ["id_compra"]])

valor_filtro = col2.selectbox("Selecione o valor", list(df_compras[col_filtro].unique()))

st_filtra = col1.button("Filtrar", key="filtrar")
st_limpar = col2.button("Limpar Filtro", key="limpar_filtro")

if st_filtra:
    st.dataframe(df_compras.loc[df_compras[col_filtro] == valor_filtro, colunas_selecionadas])
elif st_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
else:
    st.dataframe(df_compras[colunas_selecionadas])