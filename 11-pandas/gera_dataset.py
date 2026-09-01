import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

pasta_datasets = Path(__file__).parent / "datasets"
pasta_datasets.mkdir(parents=True, exist_ok=True)

LOJAS = [
    { "estado": "SP", "cidade": "São Paulo", 
     "vendedores": ["Germano Martins", "Fernanda Soares"] },
    { "estado": "MG", "cidade": "Belo Horizonte", 
     "vendedores": ["Juliana Ferreira", "Bim da Ambulância"] },
    { "estado": "SC", "cidade": "Florianópolis", 
     "vendedores": ["Magrinho Mrl", "Léco"] },
    { "estado": "RJ", "cidade": "Rio de Janeiro", 
     "vendedores": ["Gabriel Flash", "Jaqueline Carneiro"] },
    { "estado": "CE", "cidade": "Fortaleza", 
     "vendedores": ["José Maria", "Maria das Graças"] },
]

PRODUTOS = [
    { "nome": "Camiseta", "preco": 29.90 },
    { "nome": "Calça Jeans", "preco": 99.90 },
    { "nome": "Tênis Esportivo", "preco": 149.90 },
    { "nome": "Jaqueta de Couro", "preco": 199.90 },
    { "nome": "Vestido", "preco": 79.90 },
    { "nome": "Saia", "preco": 49.90 },
    { "nome": "Blusa de Frio", "preco": 89.90 },
    { "nome": "Shorts", "preco": 39.90 },
    { "nome": "Chapéu", "preco": 19.90 },
    { "nome": "Óculos de Sol", "preco": 59.90 },
]

FORMA_PAGTO = [
    "Dinheiro",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Pix",
]

GENERO_CLIENTE = [
    "Masculino",
    "Feminino",
]

compras = []

for _ in range(2000):
    loja = random.choice(LOJAS)
    produto = random.choice(PRODUTOS)
    vendedor = random.choice(loja["vendedores"])
    forma_pagto = random.choice(FORMA_PAGTO)
    genero_cliente = random.choice(GENERO_CLIENTE)
    
    data_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
        )
    nome_cliente = names.get_full_name(genero_cliente)
    
    compras.append({
        "data": data_compra.strftime("%Y-%m-%d"),
        "id_compra": 0,
        "estado": loja["estado"],
        "cidade": loja["cidade"],
        "vendedor": vendedor,
        "produto": produto["nome"],
        "preço": produto["preço"],
        "forma_pagto": forma_pagto,
        "genero_cliente": genero_cliente,
        "nome_cliente": nome_cliente
    })

df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras["id_compra"] = [i for i in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

#Exportando Dataframes
df_compras.to_csv(pasta_datasets / "compras.csv", decimal=",", sep=";")
df_lojas.to_csv(pasta_datasets / "lojas.csv", decimal=",", sep=";")
df_produtos.to_csv(pasta_datasets / "produtos.csv", decimal=",", sep=";")

df_compras.to_excel(pasta_datasets / "compras.xlsx")
df_lojas.to_excel(pasta_datasets / "lojas.xlsx")
df_produtos.to_excel(pasta_datasets / "produtos.xlsx")