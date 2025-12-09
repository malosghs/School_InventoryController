import psycopg2
import psycopg2.extras

class Database:
    def __init__(self, config): 
        self.config = config

    def get_db_connect(self):
        """Tenta estabelecer a conexão com o banco de dados."""
        try:
            conn = psycopg2.connect(**self.config)
            conn.autocommit = True
            print("Conexão com o banco de dados estabelecida com sucesso!")
            self.create_tables(conn)
            self.inserir_dados(conn)
            return conn
        except psycopg2.OperationalError as e:
            print(f"❌ Erro ao conectar ao Banco De Dados: {e}")
            return None
    def create_tables(self, conn):
        """Cria todas as tabelas, incluindo as auxiliares e as relações (FOREIGN KEY)."""
        create_tables_query = """
        CREATE TABLE IF NOT EXISTS controller_local (
            id SERIAL PRIMARY KEY,
            name_local VARCHAR(100) NOT NULL UNIQUE 
        );

        CREATE TABLE IF NOT EXISTS controller_estado (
            id SERIAL PRIMARY KEY,
            name_estado VARCHAR(100) NOT NULL UNIQUE 
        );

        CREATE TABLE IF NOT EXISTS controller_nivel (
            id SERIAL PRIMARY KEY,
            name_nivel VARCHAR(100) NOT NULL UNIQUE 
        );

        CREATE TABLE IF NOT EXISTS controller_users (
            id SERIAL PRIMARY KEY,
            nome_user VARCHAR(100) NOT NULL, 
            cargo_operacional VARCHAR(255) NOT NULL,
            -- O campo 'user_login' já estava correto com UNIQUE
            user_login VARCHAR(100) UNIQUE NOT NULL,
            nivel INT NOT NULL,
            status BOOLEAN NOT NULL,
            senha VARCHAR(100) NOT NULL,
            CONSTRAINT fk_user_level FOREIGN KEY (nivel) REFERENCES controller_nivel(id)
        );

        CREATE TABLE IF NOT EXISTS school_inventory(
            id BIGSERIAL PRIMARY KEY,
            nome_item VARCHAR(100) NOT NULL,
            cod_item VARCHAR(50) UNIQUE, -- Já estava correto com UNIQUE
            categoria VARCHAR(100) NOT NULL, 
            tipo VARCHAR(100) NOT NULL,
            number_local INT NOT NULL REFERENCES controller_local(id),
            estado_uso INT NOT NULL REFERENCES controller_estado(id),
            -- TRUE = Emprestado/Indisponível, FALSE = Disponível
            status BOOLEAN NOT NULL DEFAULT FALSE, 
            descricao TEXT
        );

        CREATE TABLE IF NOT EXISTS controller_item_for_user (
            id SERIAL PRIMARY KEY,
            id_usuario INT NOT NULL REFERENCES controller_users(id), 
            id_item INT NOT NULL REFERENCES school_inventory(id),
            data_pegou DATE NOT NULL DEFAULT CURRENT_DATE,
            data_entrega DATE,
            ativo BOOLEAN NOT NULL DEFAULT TRUE 
        );
        """
        try:
            with conn.cursor() as cursor:
                cursor.execute(create_tables_query)
        except Exception as e:
            print(f"❌ Erro ao criar tabelas: {e}")


    def inserir_dados(self, conn):
        """Insere dados padrão (estados, níveis, admin) se não existirem."""
        inserir = """
        INSERT INTO controller_estado (name_estado)
        VALUES ('NOVO'), ('SEMI NOVO'), ('ESTRAGADO')
        ON CONFLICT (name_estado) DO NOTHING;
    
        INSERT INTO controller_nivel (name_nivel)
        VALUES ('Usuário'), ('Colaborador'), ('Analista'), ('Coordenador'), ('Admin')
        ON CONFLICT (name_nivel) DO NOTHING;

        INSERT INTO controller_local (name_local)
        VALUES ('Laboratório'), ('Portaria'), ('TI'), ('Almoxarifado'), ('Escritório')
        ON CONFLICT (name_local) DO NOTHING;

        INSERT INTO controller_users (nome_user, cargo_operacional, user_login, nivel, status, senha)
        VALUES ('Admin', 'Diretor', 'admin', 5, TRUE, '123')
        ON CONFLICT (user_login) DO NOTHING;
        """
        try:
            with conn.cursor() as cursor:
                cursor.execute(inserir)
        except Exception as e:
            if "duplicate key value violates unique constraint" not in str(e):
                print("Erro ao inserir dados iniciais:", e)
                
    def alternar_status(self, conn, item_id, id_usuario, nome_usuario):
        """
        Altera o status de disponibilidade do item na school_inventory 
        E registra/fecha o empréstimo em controller_item_for_user.
        """
        select = "SELECT status FROM school_inventory WHERE id = %s;"
        try:
            with conn.cursor() as cursor:
                cursor.execute(select, (item_id,))
                result = cursor.fetchone()
                if not result:
                    return False, "Item não encontrado."
                    
                status_emprestado = result[0]
                if not status_emprestado:
                    update_item = "UPDATE school_inventory SET status = TRUE WHERE id = %s"
                    cursor.execute(update_item, (item_id,))
                    insert_emprestimo = """
                        INSERT INTO controller_item_for_user (id_usuario, id_item, data_pegou, ativo)
                        VALUES (%s, %s, CURRENT_DATE, TRUE)
                    """
                    cursor.execute(insert_emprestimo, (id_usuario, item_id))
                    msg = f"Item Emprestado para {nome_usuario}!"             
                else:
                    update_item = "UPDATE school_inventory SET status = FALSE WHERE id = %s"
                    cursor.execute(update_item, (item_id,))
                    update_emprestimo_query = """
                        UPDATE controller_item_for_user 
                        SET data_entrega = CURRENT_DATE, ativo = FALSE
                        WHERE id_item = %s AND id_usuario = %s AND ativo = TRUE
                        ORDER BY data_pegou DESC LIMIT 1
                    """
                    cursor.execute(update_emprestimo_query, (item_id, id_usuario))
                    msg = "Item Devolvido!"
                
            conn.commit()
            return True, msg
            
        except Exception as e:
            print(f"❌ Erro ao alternar status: {e}")
            conn.rollback()
            return False, f"Erro na operação: {e}"
    def add_items(self, inventario):
        """inventario: lista de dicionários. Campos esperados por item:
           'Nome_do_Item','Categoria','Tipo','Localizacao'(int id),
           'Estado_de_Uso'(int id),'Status'(bool),'Descricao' e opcional 'Quantidade'
        """
        inserir = (
            "INSERT INTO school_inventory (nome_item, categoria, tipo, number_local, estado_uso, status, descricao)"
            " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )

        for item in inventario:
            quantidade = int(item.get("Quantidade", 1) or 1)
            nome = item.get("Nome_do_Item")
            categoria = item.get("Categoria")
            tipo = item.get("Tipo")
            local = item.get("Localizacao")
            estado = item.get("Estado_de_Uso")
            status = item.get("Status", True)
            descricao = item.get("Descricao")
            params = (nome, categoria, tipo, local, estado, status, descricao)

            for _ in range(quantidade):
                try:
                    with self.conn.cursor() as cursor:
                        cursor.execute(inserir, params)
                    self.conn.commit()
                except Exception as e:
                    print("Erro ao adicionar item:", e)
                    try:
                        self.conn.rollback()
                    except Exception:
                        pass

    def add_users(self, usuarios):
        """usuarios: lista de dicionários com chaves 'Nome','Cargo','Nivel_Acesso','Senha','Status'"""
        inserir = (
            "INSERT INTO controller_users (nome_user, cargo_operacional, nivel, status, senha)"
            " VALUES (%s, %s, %s, %s, %s)"
        )
        for users in usuarios:
            nome = users.get("Nome")
            cargo = users.get("Cargo")
            nivel = users.get("Nivel_Acesso")
            senha = users.get("Senha")
            status = users.get("Status", True)
            params = (nome, cargo, nivel, status, senha)

            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(inserir, params)
                self.conn.commit()
            except Exception as e:
                print("Erro ao adicionar usuário:", e)
                try:
                    self.conn.rollback()
                except Exception:
                    pass

    def list_users(self):
        """Retorna todos os usuários como lista de tuplas."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM controller_users")
                return cursor.fetchall()
        except Exception as e:
            print("Erro ao listar usuários:", e)
            return []

    def list_items(self, conn): 
        item = """
        SELECT 
            id, nome_item, cod_item, categoria, tipo, status, descricao,
            number_local, estado_uso
        FROM school_inventory;
        """
        try:
        
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(item)
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"❌ Erro ao listar itens no Database: {e}")
            return []

