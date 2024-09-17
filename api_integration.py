import requests
from config import API_CONFIG

def get_employee_activity(id_funcionario):
    url = API_CONFIG['base_url'] + API_CONFIG['endpoints']['get_activity'].format(id_funcionario=id_funcionario)
    headers = API_CONFIG['headers']
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            atividade_data = response.json()
            atividade = atividade_data.get('atividade', 'Atividade não registrada')
            return atividade
        else:
            print(f"Erro ao obter atividade do funcionário {id_funcionario}: {response.text}")
            return 'Atividade não registrada'
    except requests.RequestException as e:
        print(f"Erro na requisição da atividade: {e}")
        return 'Atividade não registrada'

def send_productivity_data(payload):
    url = API_CONFIG['base_url'] + API_CONFIG['endpoints']['register_productivity']
    headers = API_CONFIG['headers']
    try:
        response = requests.post(url, json=payload, headers=headers)
        return response
    except requests.RequestException as e:
        print(f"Erro ao enviar dados de produtividade: {e}")
        return None
