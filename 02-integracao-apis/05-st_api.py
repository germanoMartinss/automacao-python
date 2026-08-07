import requests
import pandas as pd
import streamlit as st

def obter_request(url, params=None):
    """Função para realizar uma requisição GET e retornar o resultado em JSON."""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro na requisição: {e}")
        return None


def frequencia_nomes(name):
    """Obtém um dicionário de frequência de um nome por década no formato {década: quantidade}."""
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    dados_nome = obter_request(url) or []
    # return {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    dados_dict = {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df 

def main():
    st.title("Frequência de Nomes no Brasil")
    st.header("Consulta de Frequência de Nomes por Década")
    in_name = st.text_input("Digite um nome: \n")
    if not in_name:
            st.warning("Por favor, insira um nome para consultar a frequência.")
            st.stop()
    df = frequencia_nomes(in_name)
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write("Frequência do nome por década")
        st.dataframe(df)
    with col2:
        st.write("Série temporal")
        st.line_chart(df)

if __name__ == "__main__":
    main()