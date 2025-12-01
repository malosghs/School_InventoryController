class ItemModel:
   def __init__(self,item,acao_models):
      self.item =        Item([i for i in item])
      self.acao_models = acao_models
   def req_atualizacao(self):
      pass
   def req_pedido_acao(self,):
       pass
   def req_deletar(self):
      pass


class Item:
   def __init__(self,id,nome,codigo,categoria,tipo,localizacao,estado,status,descrisao):
      self.id =          id 
      self.nome =        nome
      self.codigo =      codigo
      self.categoria =   categoria 
      self.tipo =        tipo
      self.localizacao = localizacao 
      self.estado =      estado
      self.status =      status 
      self.descrisao =   descrisao 
   

