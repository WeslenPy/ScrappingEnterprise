import requests

url = "https://api.casadosdados.com.br/v2/public/cnpj/search"

payload = {
    "query": {
        "termo": [],
        "atividade_principal": [],
        "natureza_juridica": [],
        "uf": [],
        "municipio": [],
        "situacao_cadastral": "ATIVA",
        "cep": ["65204000"],
        "ddd": []
    },
    "range_query": {
        "data_abertura": {
            "lte": None,
            "gte": None
        },
        "capital_social": {
            "lte": None,
            "gte": None
        }
    },
    "extras": {
        "somente_mei": False,
        "excluir_mei": False,
        "com_email": False,
        "incluir_atividade_secundaria": False,
        "com_contato_telefonico": False,
        "somente_fixo": False,
        "somente_celular": False,
        "somente_matriz": False,
        "somente_filial": False
    },
    "page": 1
}
headers = {
    "authority": "api.casadosdados.com.br",
    "accept": "application/json, text/plain, */*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://casadosdados.com.br",
    "referer": "https://casadosdados.com.br/",
    "sec-ch-ua": ""Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": ""Linux"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)