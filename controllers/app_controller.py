class ControllerMain:
   
   def __init__(self):
      self.view =   None
      self.models = None
   
   def construir_page(self):
       self.view.construir_page_home()