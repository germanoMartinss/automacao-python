import requests

def cotacao_moeda(moeda):
    if moeda == "Dólar":
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        cotacao = requisicao.json()
        nome = cotacao["USDBRL"]["name"]
        valor = cotacao["USDBRL"]["bid"]
        data = cotacao["USDBRL"]["create_date"]
        mensagem = f"O valor de {nome} em {data} foi de {valor}"
    elif moeda == "Euro":
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
        cotacao = requisicao.json()
        nome = cotacao["EURBRL"]["name"]
        valor = cotacao["EURBRL"]["bid"]
        data = cotacao["EURBRL"]["create_date"]
        mensagem = f"O valor de {nome} em {data} foi de {valor}"
    elif moeda == "Bitcoin":
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
        cotacao = requisicao.json()
        nome = cotacao["BTCBRL"]["name"]
        valor = cotacao["BTCBRL"]["bid"]
        data = cotacao["BTCBRL"]["create_date"]
        mensagem = f"O valor de {nome} em {data} foi de {valor}"
        
    return mensagem