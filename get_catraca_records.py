from db_connection import get_db_connection

def get_turnstile_records():
    conn = get_db_connection()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        query = """
            SELECT
                id_funcionario,
                id_catraca,
                horario_entrada,
                horario_saida
            FROM
                registros_catracas
            WHERE
                horario_entrada >= CURRENT_DATE
        """
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records
    except Exception as e:
        print(f"Erro ao obter registros das catracas: {e}")
        return []
