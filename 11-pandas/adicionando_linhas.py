from datetime import datetime
import streamlit as st
import pandas as pd

caminho_datasets = "datasets"

df_compras = pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",", index_col=0)
df_lojas = pd.read_csv(f"{caminho_datasets}/lojas.csv", sep=";", decimal=",")
df_produtos = pd.read_csv(f"{caminho_datasets}/produtos.csv", sep=";", decimal=",")

df_lojas["cidade/estado"] = df_lojas["cidade"] + "/" + df_lojas["estado"]
lista_lojas = df_lojas["cidade/estado"].to_list()



loja_secionada = st.sidebar.selectbox("Selecione a loja", lista_lojas, key="loja_selecionada")

lista_vendedores = df_lojas.loc[df_lojas["cidade/estado"] == loja_secionada, "vendedores"].iloc[0]
lista_vendedores = lista_vendedores.strip("][").replace("'", "").split(", ")
vendedor_selecionado = st.sidebar.selectbox("Selecione o vendedor", lista_vendedores, key="vendedor_selecionado")

lista_produtos = df_produtos["nome"].to_list()
produto_selecionado = st.sidebar.selectbox("Selecione o produto", lista_produtos, key="produto_selecionado")

nome_cliente = st.sidebar.text_input("Digite o nome do cliente", key="nome_cliente")
genero_cliente = st.sidebar.selectbox("Selecione o gênero do cliente", ["Masculino", "Feminino"], key="genero_cliente")

forma_pagto = st.sidebar.selectbox("Selecione a forma de pagamento", ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"], key="forma_pagto")

if st.sidebar.button("Adicionar Compra", key="adicionar_compra"):
    cidade, estado = loja_secionada.split("/")
    preco_produto = df_produtos.loc[df_produtos["nome"] == produto_selecionado, "preco"].iloc[0]

    lista_adicionar = [
        df_compras["id_compra"].max() + 1 if not df_compras.empty else 1,
        estado,
        cidade,
        vendedor_selecionado,
        produto_selecionado,
        preco_produto,
        forma_pagto,
        genero_cliente,
        nome_cliente,
    ]
    df_compras.loc[datetime.now()] = lista_adicionar
    df_compras.to_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",")
    st.success("Compra adicionada com sucesso!")


st.dataframe(df_compras)