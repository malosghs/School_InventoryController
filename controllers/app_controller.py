import time


class DatabaseTemporario:
    def __init__(self):

        self.usuarios = [
            {"id": "1", "nome": "GABRIEL", "cpf": "000.000.000-00", "user": "admin", "cargo": "Diretor", "senha": "123"}
        ]
        self.dados_aux = {
            "categorias": ["eletronico"],
            "tipos": ["adiminiotrativo"],
            "locais": ["cozinha 1"]
        }

    def get_todos_usuarios(self):
        return self.usuarios

    def adicionar_usuario(self, nome, cpf, user, cargo, senha):  
        
        if not nome or not user:
            return False, "Erro: Nome e Login são obrigatórios!"
        
     
        for u in self.usuarios:
            if u["user"] == user:
                return False, "Erro: Este Login já existe!"
        
        novo_id = str(int(time.time()))
        self.usuarios.append({
            "id": novo_id, "nome": nome, "cpf": cpf, 
            "user": user, "cargo": cargo, "senha": senha
        })
        return True, "Sucesso: Usuário criado!"

    def atualizar_usuario(self, id_func, nome, cpf, user, cargo, senha):

        for u in self.usuarios:
            if u["id"] == id_func:
              
                nova_senha = senha if senha else u.get("senha", "")
                
                u.update({
                    "nome": nome, "cpf": cpf, 
                    "user": user, "cargo": cargo, "senha": nova_senha
                })
                return True, "Sucesso: Dados atualizados!"
        return False, "Erro: Usuário não encontrado."

    def remover_usuario(self, id_func):
        ini = len(self.usuarios)
        self.usuarios = [u for u in self.usuarios if u["id"] != id_func]
        if len(self.usuarios) < ini:
            return True, "Sucesso: Usuário removido."
        return False, "Erro ao remover."

   
    def get_auxiliar(self, chave):
      return self.dados_aux.get(chave, [])
    
    def add_auxiliar(self, c, v): 
        if v and v not in self.dados_aux[c]:
          self.dados_aux[c].append(v)
          return True

    def remove_auxiliar(self, c, v):
        if v in self.dados_aux[c]:
          self.dados_aux[c].remove(v)
          return True



class ControllerMain:
   def __init__(self):
      self.view = None
      self.database = DatabaseTemporario() 
      self.escolha_page_open = None 
      
   def construir_page(self):
      if self.view: self.view.construir_pagina_principal()
  
   def page_guia_open(self, escolha_page_num):
      pass