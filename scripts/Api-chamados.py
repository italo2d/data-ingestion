import os
import requests
from dotenv import load_dotenv

def processa_chamados():
    load_dotenv()

    url = os.getenv('API_URL')
    headers = {'x-api-key': os.getenv('API_KEY')}
    params = {'status': 'opened',
              }
    
    ## Caso falhe a requisição
   
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

    response = requests.get(url, headers=headers, params=params)
    
    # Garante que a resposta foi bem-sucedida
    response.raise_for_status()
    
    # Retorna os dados crus da API (formato JSON como vem)
    return response.json()

chamados = processa_chamados()

if chamados:
    print(chamados)
    
else:
    print("Não foi possível obter os chamados.")