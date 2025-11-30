class Database():
    def __init__(self,psycopg2,config):
        self.config =   config
        self.psycopg2 = psycopg2

    def get_db_connect(self):
        try: 
            conn = self.config
            return conn
        except self.psycopg2.OperationalError as e: 
            print(f"Erro ao conectar ao Banco De Dados")
    def create_table(self,conn): 
        create_table_itens_query = """
            CREATE TABLE IF NOT EXISTS school_inventory(
                id BIGSERIAL PRIMARY KEY,
                nome_item VARCHAR(100) NOT NULL,
                categoria VARCHAR(100) NOT NULL,
                tipo VARCHAR(100) NOT NULL,
                localizacao VARCHAR(255) NOT NULL,
                estado_uso VARCHAR(255) NOT NULL,
                status VARCHAR(255) NOT NULL,
                descricao TEXT
                );"""
        create_table_usuario_query = """
            CREATE TABLE IF NOT EXISTS controller_users (
                id SERIAL PRIMARY KEY, 
                nome_user VARCHAR(100) NOT NULL,
                cargo_operacional VARCHAR(255) NOT NULL,
                limitador INT NOT NULL
                );"""
        try:
            with conn.cursor() as cursor:
                cursor.execute(create_table_itens_query)
                cursor.execute(create_table_usuario_query)
            conn.commit()
        except self.psycopg2.OperationalError:
            print("ERROR DE OPERAÇÃO NA CRIAÇÃO DE TABELAS")
            cursor.rollback()
    """
    
    def add_itens_in_table(self,conn):
        "Adiciona os itens padrão na tabela"
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM school_inventory")
                if cursor.fetchone()[0]>0:
                    print("Dados base já estão no Postgre.")
                    return
                inventario = [
    {
        "Nome_do_Item": "Mouse USB",
        "Codificacao": "IT-001",
        "Categoria": "Periférico",
        "Tipo": "Mouse",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 60,
        "Descricao": "Mouse USB padrão para estações de trabalho."
    },
    {
        "Nome_do_Item": "Teclado USB",
        "Codificacao": "IT-002",
        "Categoria": "Periférico",
        "Tipo": "Teclado",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 55,
        "Descricao": "Teclado USB padrão ABNT2."
    },
    {
        "Nome_do_Item": "Headset com Microfone",
        "Codificacao": "IT-003",
        "Categoria": "Áudio",
        "Tipo": "Headset",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 35,
        "Descricao": "Headset com microfone para reuniões e chamadas."
    },
    {
        "Nome_do_Item": "Cabo HDMI 1.8m",
        "Codificacao": "IT-004",
        "Categoria": "Cabos",
        "Tipo": "HDMI",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 30,
        "Descricao": "Cabo HDMI de 1.8 metros para vídeo."
    },
    {
        "Nome_do_Item": "Cabo VGA 1.5m",
        "Codificacao": "IT-005",
        "Categoria": "Cabos",
        "Tipo": "VGA",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 15,
        "Descricao": "Cabo VGA de 1.5 metros para monitores antigos."
    },
    {
        "Nome_do_Item": "Adaptador USB-C → HDMI",
        "Codificacao": "IT-006",
        "Categoria": "Adaptadores",
        "Tipo": "USB-C para HDMI",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 12,
        "Descricao": "Adaptador para conectar USB-C a HDMI."
    },
    {
        "Nome_do_Item": "Pen Drive 32GB",
        "Codificacao": "IT-007",
        "Categoria": "Armazenamento",
        "Tipo": "Pen Drive",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 40,
        "Descricao": "Pen drive de 32GB."
    },
    {
        "Nome_do_Item": "Roteador Wi-Fi",
        "Codificacao": "IT-008",
        "Categoria": "Rede",
        "Tipo": "Roteador",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 8,
        "Descricao": "Roteador Wi-Fi padrão para redes locais."
    },
    {
        "Nome_do_Item": "Switch 24 portas",
        "Codificacao": "IT-009",
        "Categoria": "Rede",
        "Tipo": "Switch",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 6,
        "Descricao": "Switch gerenciável de 24 portas."
    },
    {
        "Nome_do_Item": "Patch Cords diversos",
        "Codificacao": "IT-010",
        "Categoria": "Cabos de Rede",
        "Tipo": "Patch Cord",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 50,
        "Descricao": "Patch cords de vários tamanhos e cores."
    },
    {
        "Nome_do_Item": "Nobreak 1400VA",
        "Codificacao": "IT-011",
        "Categoria": "Energia",
        "Tipo": "Nobreak",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Quantidade": 5,
        "Descricao": "Nobreak 1400VA para proteção de equipamentos."
    },
]

                usuarios = [
                {
                    "Nome": "Carlos",
                    "Cargo": "Coordenador Administrativo",
                    "Nivel_Acesso": 4,  # Cadastro e  exclusão
                    "Senha": "123456",
                    "Status": "Ativo",
                    "Usuario": "Carlos@exemplo.com"
                },
                {
                    "Nome": "Ana",
                    "Cargo": "Auxiliar da Biblioteca",
                    "Nivel_Acesso": 3,  # empréstimos e devoluções
                    "Senha": "123456",
                    "Status": "Ativo",
                    "Usuario": "Ana@exemplo.com"
                },
                {
                    "Nome": "Roberto",
                    "Cargo": "Técnico de TI",
                    "Nivel_Acesso": 5,  # Configurações e manutenção
                    "Senha": "123456",
                    "Status": "Ativo",
                    "Usuario": "Rorberto@exemplo.com"
                }
            ]


                for item in inventario:
                  quantidade = item["Quantidade"]
                  nome  = item["Nome_do_Item"]
                  codigo = item["Codificacao"]
                  categoria  = item["Categoria"]
                  tipo  =  item["Tipo"]
                  local  = item["Localizacao"]
                  estado = item["Estado_de_Uso"]
                  status = item["Status"]
                  descricao  = item["Descricao"]
                  for i in range(quantidade):
                     print(codigo,nome,categoria,tipo,local,status,descricao)

                for item in usuarios:
                     nome  = item["Nome"]
                     cargo = item["Cargo"]
                     nivel  = item["Nivel_Acesso"]
                     senha  =  item["Senha"]
                     status = item["Status"]
                     descricao  = item["Descricao"]
    
                """