import requests
from pprint import pprint
from urllib.parse import quote

nome = input("Digite um nome: \n")
nome_codificado = quote(nome)  # Codifica o nome para ser usado na URL
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome_codificado}"
params = {
    "localidade": 35
}

response = requests.get(url, params=params)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Erro na requisição: {e}")
    resultado = None
else:
    resultado = response.json()
    print("URL usada:", url)
    print("Resultado bruto:", resultado)
    if resultado:
        pprint(resultado[0]["res"])
    else:
        print("Nenhum resultado encontrado para esse nome.")