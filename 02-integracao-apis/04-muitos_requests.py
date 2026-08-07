import requests
from pprint import pprint

def obter_request(url, params=None):
    """Função para realizar uma requisição GET e retornar o resultado em JSON."""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro na requisição: {e}")
        return None

def buscar_id_estado():
    """Função para buscar o ID do estado de São Paulo."""
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    dados_estados = obter_request(url, params={"view": "nivelado"}) or []
    return { estado["UF-id"]: estado["UF-nome"] for estado in dados_estados}

def frequencia_nome(name):
    """Obtém um dicionário de frequência de um nome por estado no formato {id_estado: frequencia}."""
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    dados_frequencia = obter_request(url, params={"groupBy": "UF"}) or []
    return {int(dado["localidade"]): dado["res"][0]["proporcao"] for dado in dados_frequencia}

def main(name):
    dict_estados = buscar_id_estado()
    dict_frequencia = frequencia_nome(name)
    print(f"== Frequência do nome '{name}' nos Estados (por 100.000 habitantes) ==")
    for id_estado, frenquencia in sorted(dict_frequencia.items(),
                                         key=lambda item: item[1], reverse=True):
        print(f"-> {dict_estados.get(id_estado, 'Desconhecido')}: {frenquencia}")

if __name__ == "__main__":
    main("Germano")