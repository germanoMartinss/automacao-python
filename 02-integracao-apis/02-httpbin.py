import requests

url = "https://httpbin.org/get"
response = requests.get(url)
print(response)
print(response.text)


url = "https://httpbin.org/post"
data = {
    "pessoa": {
        "nome": "Germano",
        "profissao": "Programador"
    }
}

params = {
    "dataIni": "2023-01-01",
    "dataFim": "2023-12-31"
}



response = requests.post(url, json=data, params=params)
print(response.request.url)
print(response.text)