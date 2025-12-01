import psycopg2

class Database():
    def __init__(self, config):
        self.config = config

    def get_db_connect(self):
        try:
            conn = self.config
            return conn
        except psycopg2.OperationalError:
            print("Erro ao conectar ao Banco De Dados")

    def create_table(self, conn):
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
            );
        """

        create_table_usuario_query = """
            CREATE TABLE IF NOT EXISTS controller_users (
                id SERIAL PRIMARY KEY, 
                nome_user VARCHAR(100) NOT NULL,
                cargo_operacional VARCHAR(255) NOT NULL,
                limitador INT NOT NULL
            );
        """

        try:
            with conn.cursor() as cursor:
                cursor.execute(create_table_itens_query)
                cursor.execute(create_table_usuario_query)
            conn.commit()
        except psycopg2.OperationalError:
            print("ERROR DE OPERAÇÃO NA CRIAÇÃO DE TABELAS")
            conn.rollback()

    def add_itens_in_table(self, conn):
        "Adiciona os itens padrão na tabela"
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM school_inventory")
                if cursor.fetchone()[0] > 0:
                    print("Dados base já estão no Postgre.")
                    return

                # ---------------------------
                # INVENTÁRIO
                # ---------------------------
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
                    }
                ]

                # ---------------------------
                # USUÁRIOS
                # ---------------------------
                usuarios = [
                    {
                        "Nome": "Carlos",
                        "Cargo": "Coordenador Administrativo",
                        "Nivel_Acesso": 4,
                        "Senha": "123456",
                        "Status": "Ativo",
                        "Usuario": "Carlos@exemplo.com"
                    }
                ]

                # Processa itens
                for item in inventario:
                    quantidade = item["Quantidade"]
                    nome = item["Nome_do_Item"]
                    codigo = item["Codificacao"]
                    categoria = item["Categoria"]
                    tipo = item["Tipo"]
                    local = item["Localizacao"]
                    estado = item["Estado_de_Uso"]
                    status = item["Status"]
                    descricao = item["Descricao"]

                    for i in range(quantidade):
                        print(codigo, nome, categoria, tipo, local, status, descricao)

                # Processa usuários
                for item in usuarios:
                    nome = item["Nome"]
                    cargo = item["Cargo"]
                    nivel = item["Nivel_Acesso"]
                    senha = item["Senha"]
                    status = item["Status"]
                    usuario = item["Usuario"]   # ← CORRIGIDO
                    print(nome, cargo, nivel, status, usuario)

        except Exception as e:
            print("Erro ao inserir itens:", e)
