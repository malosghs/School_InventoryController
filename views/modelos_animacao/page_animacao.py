class AnimacoesPage:
   def __init__(self,ft):
      self.ft = ft 
   def carregamento_animacao(self):
      return  self.ft.Column(
            [self.ft.ProgressRing(), self.ft.Text("Carregando banco de dados")],
            horizontal_alignment=self.ft.CrossAxisAlignment.CENTER,
        ),

