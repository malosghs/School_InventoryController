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
            yield conn

        except psycopg2.OperationalError as e: 
            print(f"Erro ao conectar ao Banco De Dados{e}")
    def create_table(self,conn): 
        create_tables = """
            CREATE TABLE IF NOT EXISTS school_inventory(
                id BIGSERIAL PRIMARY KEY,
                nome_item VARCHAR(100) NOT NULL,
                categoria VARCHAR(100) NOT NULL,
                tipo VARCHAR(100) NOT NULL,
                number_local VARCHAR(255) NOT NULL,
                estado_uso VARCHAR(255) NOT NULL,
                status VARCHAR(255) NOT NULL,
                descricao TEXT
                );

            CREATE TABLE IF NOT EXISTS controller_users (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL, 
                cargo_operacional VARCHAR(255) NOT NULL,
                nivel INT NOT NULL,
                senha VARCHAR(100) NOT NULL,
                nome_user VARCHAR(100) NOT NULL
                );

            CREATE TABLE IF NOT EXISTS controller_item_for_user (
                id SERIAL PRIMARY KEY,
                id_usuario INT, 
                Id_item INT
                );
            
            CREATE TABLE IF NOT EXISTS controller_local (
                id INT PRIMARY KEY,
                name_local VARCHAR(100),
                );

             CREATE TABLE IF NOT EXISTS controller_status (
                id INT PRIMARY KEY,
                name_status VARCHAR(100)
                );

            CREATE TABLE IF NOT EXISTS controller_estado (
                id INT PRIMARY KEY,
                name_estado VARCHAR(100)
                );

            CREATE TABLE IF NOT EXISTS controller_nivel (
                id INT PRIMARY KEY,
                name_nivel VARCHAR(100) 
                );

            CREATE TABLE IF NOT EXISTS controller_status_user (
                id INT PRIMARY KEY,
                name_status VARCHAR(100) 
                );
            
            ALTER TABLE controller_users ADD CONSTRAINT fk_user_level -- Nome da sua restrição (fk = foreign key) FOREIGN KEY (nivel) REFERENCES access_levels (nivel); -
            ALTER
                """
        try:
            with conn.cursor() as cursor:
                cursor.execute(create_tables)
            conn.commit()
        except psycopg2.OperationalError:
            print("ERROR DE OPERAÇÃO NA CRIAÇÃO DE TABELAS")
            cursor.rollback()
    def relacionamento(self,conn):
        pass
                