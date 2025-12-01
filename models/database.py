import psycopg2
from config_database import *
class Database():
    def __init__(self,config):
        self.config = config


    def get_db_connect(self):
        try: 
            conn = psycopg2.connect(self.config)
            db = Database
            db.create_table(conn)
            db.inserir_dados(conn)
            return
        except psycopg2.OperationalError as e: 
            print(f"Erro ao conectar ao Banco De Dados{e}")

    def create_table(conn): 
        create_tables = """
        CREATE TABLE IF NOT EXISTS controller_local (
            id SERIAL PRIMARY KEY,
            name_local VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS controller_estado (
            id SERIAL PRIMARY KEY,
            name_estado VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS controller_nivel (
            id SERIAL PRIMARY KEY,
            name_nivel VARCHAR(100) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS controller_users (
            id SERIAL PRIMARY KEY,
            nome_user VARCHAR(100) NOT NULL, 
            cargo_operacional VARCHAR(255) NOT NULL,
            nivel INT NOT NULL,
            status BOOLEAN NOT NULL,
            senha VARCHAR(100) NOT NULL,
            CONSTRAINT fk_user_level FOREIGN KEY (nivel) REFERENCES controller_nivel(id)
        );

        CREATE TABLE IF NOT EXISTS school_inventory(
            id BIGSERIAL PRIMARY KEY,
            nome_item VARCHAR(100) NOT NULL,
            categoria VARCHAR(100) NOT NULL, 
            tipo VARCHAR(100) NOT NULL,
            number_local INT NOT NULL REFERENCES controller_local(id),
            estado_uso INT NOT NULL REFERENCES controller_estado(id),
            status BOOLEAN NOT NULL,
            descricao TEXT
        );

        CREATE TABLE IF NOT EXISTS controller_item_for_user (
            id SERIAL PRIMARY KEY,
            id_usuario INT NOT NULL REFERENCES controller_users(id), 
            id_item INT NOT NULL REFERENCES school_inventory(id),
            data_pegou DATE,
            data_entrega DATE
    """

        try:
            with conn.cursor() as cursor:
                cursor.execute(create_tables)
            conn.commit()
        except psycopg2.OperationalError:
            print("ERROR DE OPERAÇÃO NA CRIAÇÃO DE TABELAS")
            cursor.rollback()
    def inserir_dados(self, conn):
        inserir = """
        INSERT INTO controller_estado (name_estado)
        VALUES ('NOVO'), ('SEMI NOVO'), ('ESTRAGADO')
        ON CONFLICT DO NOTHING;

        INSERT INTO controller_nivel (name_nivel)
        VALUES ('Usuário'), ('Colaborador'), ('Analista'), ('Coordenador'), ('Admin')
        ON CONFLICT DO NOTHING;

        INSERT INTO controller_users (nome_user, cargo_operacional, nivel, status, senha)
        VALUES ('Admin', 'Admin', 5, True, '123456')
        ON CONFLICT DO NOTHING;
        """

        try:
            with conn.cursor() as cursor:
                cursor.execute(inserir)
            conn.commit()
        except Exception as e:
            print("Erro ao inserir dados:", e)
            conn.rollback() 
    def delete_item(self, conn, item_id):
        deleta_item = "DELETE FROM school_inventory WHERE id = %s"
        try:
            with conn.cursor() as cursor:
                cursor.execute(deleta_item, (item_id,))
            conn.commit()
            print("Item que foi escolhido foi deletado")
        except Exception as e:
            print("Erro ao deletar:", e)
            conn.rollback()
    def delete_user(self,conn,user_id):
        "Entrada é um id do usuario que deseja deletar" 
        deleta_user = "DELETE FROM controller_users WHERE id = %s"
        try:
            with conn.cursor() as cursor:
                cursor.execute(deleta_user, (user_id,))
            conn.commit()
            print("Item deletado!")
        except Exception as e:
            print("Erro ao deletar:", e)
            conn.rollback()
    def chamar_item(self, conn, item_id):
        "Chama o usuario para visualização"
        chamar_item = "SELECT * FROM school_inventory WHERE id = %s"

        try:
            with conn.cursor() as cursor:
                cursor.execute(chamar_item, (item_id,))
                return cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar item:", e)
    def chamar_user(self,conn,user_id):
        "Chama o usuario para visualização"
        chamar_user = "SELECT * FROM school_inventory WHERE id = %s"

        try:
            with conn.cursor() as cursor:
                cursor.execute(chamar_user, (user_id,))
                return cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar item:", e)
    def chamar_periodo_emprestimo(self,conn,user_id, item_id):
        "Chama o periodo de emprestimo para visualização"
        chamar_emprestimo = "SELECT * FROM school_inventory WHERE id = %s"

        try:
            if user_id >1:
                with conn.cursor() as cursor:
                    cursor.execute(chamar_emprestimo, (user_id,))
                    return cursor.fetchone()
            elif item_id >1:
                with conn.cursor() as cursor:
                    cursor.execute(chamar_emprestimo, (item_id ,))
                    return cursor.fetchone()
        except Exception as e:
            print("Erro ao buscar item:", e)
            
"""
    def add_item(conn,dict):
        "Entrada é um dicionario dos Itens que já foram cadastrados"
        = 
        INSERT INTO school_inventory 
        (nome_item, categoria, tipo, number_local, estado_uso, status, descricao)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        
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
                       try:
                            with conn.cursor() as cursor:
                                cursor.execute(seila, values)
                            conn.commit()
                            print("Item adicionado com sucesso!")
                        except Exception as e:
                            print("Erro ao adicionar item:", e)
                            conn.rollback()



    def add_user(conn,dict):
        "Entrada é um dicionario dos users que já foram cadastrados"
                for item in usuarios:
                     nome  = item["Nome"]
                     cargo = item["Cargo"]
                     nivel  = item["Nivel_Acesso"]
                     senha  =  item["Senha"]
                     status = item["Status"]
                     descricao  = item["Descricao"]
                     """