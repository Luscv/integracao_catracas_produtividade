import schedule
import time
from get_turnstile_records import get_turnstile_records
from api_integration import get_employee_activity, send_productivity_data

def integrate_data():
    registros = get_turnstile_records()
    if not registros:
        print("Nenhum registro encontrado.")
        return

    for registro in registros:
        id_funcionario = registro[0]
        id_catraca = registro[1]
        horario_entrada = registro[2]
        horario_saida = registro[3]

        # Obter atividade do funcionário
        atividade = get_employee_activity(id_funcionario)

        # Preparar payload
        payload = {
            "id_funcionario": id_funcionario,
            "id_catraca": id_catraca,
            "horario_entrada": horario_entrada.isoformat(),
            "horario_saida": horario_saida.isoformat() if horario_saida else None,
            "atividade": atividade
        }

        # Enviar dados para a API
        response = send_productivity_data(payload)
        if response and response.status_code == 200:
            print(f"Dados enviados com sucesso para o funcionário {id_funcionario}.")
        else:
            print(f"Falha ao enviar dados para o funcionário {id_funcionario}.")


# Função para agendar o job
def job():
    print("Iniciando integração...")
    integrate_data()
    print("Integração concluída.")

# Agendar para rodar a cada hora
schedule.every().hour.do(job)

if __name__ == "__main__":
    print("Serviço de integração iniciado.")
    job()  # Executa imediatamente na inicialização
    while True:
        schedule.run_pending()
        time.sleep(1)







