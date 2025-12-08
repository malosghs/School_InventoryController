import time
import random


class DatabaseTemporario:
    def __init__(self):
        self.usuarios = [
            {"id": "1", "nome": "Admin", "cpf": "000.000.000-00", "user": "admin", "cargo": "Diretor", "senha": "123"}
        ]
        self.dados_aux = {
            "categorias": [ "Eletronico", "Mobiliaria"],
            "tipos": ["Item", "EPI"],
            "locais": ["Laboratorio", "Portaria", "TI"]
        }


    def get_todos_usuarios(self): return self.usuarios
    
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

    # --- Auxiliares ---
    def get_auxiliar(self, k): return self.dados_aux.get(k, [])
    def add_auxiliar(self, k, v): 
        if v and v not in self.dados_aux[k]: self.dados_aux[k].append(v); return True
        return False
    def remove_auxiliar(self, k, v): 
        if v in self.dados_aux[k]: self.dados_aux[k].remove(v); return True
        return False



class InventarioDatabase:
    def __init__(self):
  
        self.db_itens = [
            {"id": 1, "Nome": "Notebook Dell", "Cod": "IT-100", "Cat": "Hardware", "Sts": "Emprestado", "Loc": "TI", "Est": "Novo", "Tipo": "PC", "Desc": "i7 16GB", "Resp": "João"},
            {"id": 2, "Nome": "Mouse USB", "Cod": "IT-101", "Cat": "Periférico", "Sts": "Disponível", "Loc": "Almoxarifado", "Est": "Bom", "Tipo": "Mouse", "Desc": "Logitech", "Resp": ""},
        ]

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
      self.database = DatabaseTemporario() 
      self.inventario = InventarioDatabase()
      self.escolha_page_open = None 
      
   def construir_page(self):
      if self.view: self.view.construir_pagina_principal()
   def page_guia_open(self, n): pass