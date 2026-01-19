import time
import random
import psycopg2
import psycopg2.extras
from models.database import Database  
from models.config_database import CONFIG_DB_SCHOOL

class Database_oficial:
    def __init__(self):
        self.db_manager = Database(CONFIG_DB_SCHOOL) 
        self.conn = self.db_manager.get_db_connect()

    def list_items(self, conn=None):
        return self.db_manager.list_items(conn or self.conn)

    def list_users(self, conn=None):
        return self.db_manager.list_users()

    def alternar_status(self, conn, item_id, id_usuario, nome_usuario):
        return self.db_manager.alternar_status(conn, item_id, id_usuario, nome_usuario)

    def add_items(self, inventario):
        return self.db_manager.add_items(inventario)

    def add_users(self, usuarios):
        return self.db_manager.add_users(usuarios)

    def _execute_select(self, query, params=None):
        if not self.conn:
            return []
        try:
            with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute(query, params)
                return [dict(row) for row in cursor.fetchall()] 
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            return []

    def get_todos_usuarios(self):
        user = """
        SELECT id, nome_user AS "Nome", cargo_operacional AS "Cargo", 
               user_login AS "User", senha  
        FROM controller_users
        WHERE status = TRUE;
        """
        return self._execute_select(user)

    def get_todos_itens(self):
        query = """
        SELECT  
            id,  
            nome_item AS "Nome",  
            cod_item AS "Cod",  
            categoria AS "Cat",  
            CASE  
                WHEN status = TRUE THEN 'Emprestado'  
                ELSE 'Disponível'  
            END AS "Sts",  
            tipo AS "Tipo",  
            descricao AS "Desc",  
            number_local AS "Loc_ID",  
            estado_uso AS "Est_ID"
        FROM school_inventory;
        """
        return self._execute_select(query)
    

import time
import psycopg2.extras

class DatabaseTemporario:
    def __init__(self, database_manager):
        self.database = database_manager
        # cache opcional para evitar múltiplas leituras iniciais
        self.usuarios = self.database.get_todos_usuarios()

    # ------------------ Usuários ------------------
    def get_todos_usuarios(self): 
        return self.database.get_todos_usuarios()
    
    def adicionar_usuario(self, nome, cargo, user, senha):
        if not nome or not user: 
            return False, "Preencha os dados obrigatórios!"
        # verifica duplicidade de login
        for u in self.get_todos_usuarios():
            if u["User"] == user:
                return False, "Login já existe!"
        try:
            query = """
                INSERT INTO controller_users (nome_user, cargo_operacional, user_login, senha, status)
                VALUES (%s, %s, %s, %s, TRUE)
            """
            with self.database.conn.cursor() as cursor:
                cursor.execute(query, (nome, cargo, user, senha))
            self.database.conn.commit()
            return True, "Usuário cadastrado com sucesso!"
        except Exception as e:
            self.database.conn.rollback()
            return False, f"Erro ao cadastrar usuário: {e}"

    def atualizar_usuario(self, id_u, nome, cargo, user, senha):
        try:
            query = """
                UPDATE controller_users
                SET nome_user = %s, cargo_operacional = %s, user_login = %s, senha = %s
                WHERE id = %s
            """
            with self.database.conn.cursor() as cursor:
                cursor.execute(query, (nome, cargo, user, senha, id_u))
            self.database.conn.commit()
            return True, "Usuário atualizado com sucesso!"
        except Exception as e:
            self.database.conn.rollback()
            return False, f"Erro ao atualizar usuário: {e}"

    def remover_usuario(self, id_u):
        try:
            query = "DELETE FROM controller_users WHERE id = %s"
            with self.database.conn.cursor() as cursor:
                cursor.execute(query, (id_u,))
            self.database.conn.commit()
            return True, "Usuário removido com sucesso!"
        except Exception as e:
            self.database.conn.rollback()
            return False, f"Erro ao remover usuário: {e}"

    def get_auxiliar(self, k):
        """
        k: 'locais' | 'categorias' | 'tipos' | 'estados' (opcional)
        """
        try:
            with self.database.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                if k == "locais":
                    cursor.execute("SELECT name_local FROM controller_local ORDER BY name_local")
                    return [row["name_local"] for row in cursor.fetchall()]
                elif k == "categorias":
                    cursor.execute("SELECT DISTINCT categoria FROM school_inventory WHERE categoria IS NOT NULL ORDER BY categoria")
                    return [row["categoria"] for row in cursor.fetchall()]
                elif k == "tipos":
                    cursor.execute("SELECT DISTINCT tipo FROM school_inventory WHERE tipo IS NOT NULL ORDER BY tipo")
                    return [row["tipo"] for row in cursor.fetchall()]
                elif k == "estados":
                    cursor.execute("SELECT nome_estado FROM controller_estado ORDER BY nome_estado")
                    return [row["nome_estado"] for row in cursor.fetchall()]
                else:
                    return []
        except Exception as e:
            print(f"Erro ao buscar auxiliar '{k}': {e}")
            return []

    def add_auxiliar(self, k, v):
        """
        Adiciona apenas onde faz sentido:
        - 'locais' -> controller_local(name_local)
        - 'categorias' e 'tipos' vêm do inventário; não adicionamos direto aqui
        - 'estados' -> controller_estado(nome_estado) (se desejar)
        """
        if not v:
            return False
        try:
            with self.database.conn.cursor() as cursor:
                if k == "locais":
                    cursor.execute("INSERT INTO controller_local (name_local) VALUES (%s)", (v,))
                elif k == "estados":
                    cursor.execute("INSERT INTO controller_estado (nome_estado) VALUES (%s)", (v,))
                else:
                    return False
            self.database.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar auxiliar '{k}': {e}")
            self.database.conn.rollback()
            return False

    def remove_auxiliar(self, k, v):
        """
        Remove apenas onde faz sentido:
        - 'locais' -> controller_local(name_local)
        - 'estados' -> controller_estado(nome_estado)
        """
        try:
            with self.database.conn.cursor() as cursor:
                if k == "locais":
                    cursor.execute("DELETE FROM controller_local WHERE name_local = %s", (v,))
                elif k == "estados":
                    cursor.execute("DELETE FROM controller_estado WHERE nome_estado = %s", (v,))
                else:
                    return False
            self.database.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao remover auxiliar '{k}': {e}")
            self.database.conn.rollback()
            return False



class InventarioDatabase:
    def __init__(self, db_manager):  
        self.db_manager = db_manager

    def realizar_devolucao(self, item_id, obs=None):
        try:
            with self.db_manager.conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE school_inventory SET status = FALSE WHERE id = %s",
                    (item_id,)
                )

                cursor.execute("""
                    UPDATE controller_item_for_user
                    SET data_entrega = CURRENT_DATE, ativo = FALSE
                    WHERE id_item = %s AND ativo = TRUE
                """, (item_id,))

            self.db_manager.conn.commit()
            return True, "Item devolvido e empréstimos ativos encerrados."
        except Exception as e:
            self.db_manager.conn.rollback()
            return False, f"Erro ao devolver item: {e}"
        
    def get_todos_itens(self): 
        return self.db_manager.get_todos_itens()


    def realizar_emprestimo(self, item_id, id_usuario):
        with self.db_manager.conn.cursor() as cursor:
            cursor.execute("SELECT nome_user FROM controller_users WHERE id = %s", (id_usuario,))
            result = cursor.fetchone()
            if not result:
                return False, "Usuário não encontrado."
            nome_usuario = result[0]

        return self.db_manager.alternar_status(self.db_manager.conn, item_id, id_usuario, nome_usuario)

    def deletar_item(self, uid):
        try:
            with self.db_manager.conn.cursor() as cursor:
                cursor.execute("DELETE FROM school_inventory WHERE id = %s", (uid,))
            self.db_manager.conn.commit()
            return True, "Item excluído com sucesso!"
        except Exception as e:
            self.db_manager.conn.rollback()
            return False, f"Erro ao excluir item: {e}"

    def salvar_novos_itens(self, dados):
        query = """
        INSERT INTO school_inventory 
            (nome_item, cod_item, categoria, tipo, number_local, estado_uso, status, descricao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            dados['Nome'],     
            dados['Cod'],       
            dados['Cat'],       
            dados['Tipo'],      
            dados['Loc'],      
            dados['Estado'],   
            dados['Sts'],       
            dados['Desc']       
        )
        with self.db_manager.conn.cursor() as cursor:
            cursor.execute(query, params)
        self.db_manager.conn.commit()

        


class ControllerMain:
    def __init__(self):
        self.view = None
        self.db_manager = Database_oficial()
        self.database = DatabaseTemporario(self.db_manager) 
        self.inventario = InventarioDatabase(self.db_manager)
        self.escolha_page_open = None
      
    def construir_page(self):
        if self.view: 
            self.view.construir_pagina_principal()

    def page_guia_open(self, n): 
        pass
