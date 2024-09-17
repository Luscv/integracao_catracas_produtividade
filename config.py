DB_CONFIG = {
    'host': 'seu_host',
    'port': 5432,
    'database': 'nome_do_banco',
    'user': 'seu_usuario',
    'password': 'sua_senha'
}

# Configurações da API do sistema web de produtividade
API_CONFIG = {
    'base_url': 'https://api.sistemaprodutividade.com',
    'endpoints': {
        'register_productivity': '/produtividade/register',
        'get_activity': '/funcionarios/{id_funcionario}/atividades'
    },
    'headers': {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer seu_token_de_autenticacao'
    }
}
