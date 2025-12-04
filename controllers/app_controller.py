class ControllerMain:
   
   def __init__(self):
      self.view =   None
      self.models = None
      self.escolha_page_open = None 
      
   
   def construir_page(self):
      self.view.construir_pagina_principal()
  
   def page_guia_open(self,escolha_page_num):
      if escolha_page_num == 0:
         self.view.open_home()
      else:
         self.view.open_cadastroItem()
      
      
      

  
       