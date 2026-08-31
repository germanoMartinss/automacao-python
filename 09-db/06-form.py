import streamlit as st
import dados

st.title("Cadastro de Filmes")

título = st.text_input("Digite o título do filme: \n")
ano = st.number_input("Digite o ano do filme: \n", min_value=1900, max_value=2026)
nota = st.slider("Digite a nota do filme: \n", min_value=0.0, max_value=10.0, step=0.1)

#1 - Conectando no banco de dados

if st.button("Cadastrar Filme"):
    dados.insere_dados(título, ano, nota)
    st.success("Filme cadastrado com sucesso!")

#2 - Listando dados
filmes = dados.lista_dados()
st.header("Filmes Cadastrados")
st.table(filmes)