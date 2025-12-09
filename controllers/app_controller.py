import time
import random
import psycopg2
from models.database import Database  
from models.config_database import CONFIG_DB_SCHOOL

class Database_oficial:
    def __init__(self):
        self.db_manager = Database(CONFIG_DB_SCHOOL) 
        self.conn = self.db_manager.get_db_connect()
        
    def _execute_select(self, query, params=None):
        """Método auxiliar para executar consultas SELECT e retornar resultados."""
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
        """Busca todos os usuários do controller_users."""
        user = """
        SELECT id, nome_user AS nome, cargo_operacional AS cargo, user_login AS user, senha 
        FROM controller_users
        WHERE status = TRUE;
        """
        return self._execute_select(user)
    def list_items(self):
        """Retorna todos os itens do inventário, chamando o método do Database."""
        if self.conn:
            return self.db_manager.list_items(self.conn)
        return []

    def get_todos_itens(self):
        """Busca todos os itens do school_inventory."""
        seila = """
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
        return self._execute_select(seila)

class DatabaseTemporario:
    def __init__(self, database_manager):
        self.database = database_manager 
        self.usuarios = self.database.get_todos_usuarios() 
        self.dados_aux = {
            "categorias": [ "Eletronico", "Mobiliaria"],
            "tipos": ["Item", "EPI"],
            "locais": ["Laboratorio", "Portaria", "TI"]
        }


    def get_todos_usuarios(self): 
        return self.database.get_todos_usuarios()
    
    def adicionar_usuario(self, nome, cpf, user, cargo, senha):
        if not nome or not user: return False, "Preencha dados!"
        for u in self.usuarios:
            if u["user"] == user: return False, "Login existe!"
        self.usuarios.append({"id": str(int(time.time())), "nome": nome, "cpf": cpf, "user": user, "cargo": cargo, "senha": senha})
        return True, "Sucesso!"

    def atualizar_usuario(self, id_u, nome, cpf, user, cargo, senha):
        for u in self.usuarios:
            if u["id"] == id_u:
                u.update({"nome": nome, "cpf": cpf, "user": user, "cargo": cargo, "senha": senha if senha else u["senha"]})
                return True, "Atualizado!"
        return False, "Erro."

    def remover_usuario(self, id_u):
        ini = len(self.usuarios)
        self.usuarios = [u for u in self.usuarios if u["id"] != id_u]
        return len(self.usuarios) < ini, "Removido."

    def get_auxiliar(self, k): return self.dados_aux.get(k, [])
    def add_auxiliar(self, k, v): 
        if v and v not in self.dados_aux[k]: self.dados_aux[k].append(v); return True
        return False
    def remove_auxiliar(self, k, v): 
        if v in self.dados_aux[k]: self.dados_aux[k].remove(v); return True
        return False



class InventarioDatabase:
    def __init__(self, db_manager): 
        self.db_manager = db_manager
        self.db_itens = self.db_manager.list_items()

    def get_todos_itens(self): return self.db_itens

    def salvar_novos_itens(self, nome, cat, qtd, local):
        ids = []
        try: q = int(qtd)
        except: q = 1
        for _ in range(q):
            cod = f"IT-{random.randint(1000,9999)}"
            self.db_itens.append({
                "id": int(time.time())+random.randint(1,10000), 
                "Nome": nome, "Cod": cod, "Cat": cat, 
                "Sts": "Disponível", "Loc": local, 
                "Est": "Novo", "Tipo": "Item", "Desc": "Recém criado", "Resp": ""
            })
            ids.append(cod)
        return ids

    def deletar_item(self, uid):
        self.db_itens = [i for i in self.db_itens if i['id'] != uid]
        return True

    def alternar_status(self, uid):
        for i in self.db_itens:
            if i['id'] == uid:
                if i['Sts'] == "Disponível":
                    i['Sts'] = "Emprestado"
                    i['Resp'] = "Usuario Genérico"
                    return True, "Item Emprestado!"
                else:
                    i['Sts'] = "Disponível"
                    i['Resp'] = ""
                    return True, "Item Devolvido!"
        return False, "Item não encontrado"

class ControllerMain:
   def __init__(self):
      self.view = None
      self.db_manager = Database_oficial()
      self.database = DatabaseTemporario(self.db_manager) 
      self.inventario = InventarioDatabase(self.db_manager)
      self.escolha_page_open = None
      
   def construir_page(self):
      if self.view: self.view.construir_pagina_principal()
   def page_guia_open(self, n): pass