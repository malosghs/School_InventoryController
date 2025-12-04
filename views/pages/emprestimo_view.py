

class EmprestimoView:
       def __init__(self,ft, animador_pagina, animador_botao, controller):
 
        
        self.ft = ft 

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller


        self.busca = self.ft.TextField(label="ID Funcionário ou Código do Item")

        self.page =self.ft.Column(
           
            
            [ 
            self.ft.Text("Registrar Empréstimo", size=26, weight=self.ft.FontWeight.BOLD),
            self.busca,

            self.ft.Dropdown(label="Categoria"),
            self.ft.Dropdown(label="Tipo"),
            self.ft.Dropdown(label="Selecionar Item"),
            self.ft.Dropdown(label="Funcionário"),

            self.ft.ElevatedButton("Registrar Empréstimo")
        ],
         expand = True,
         alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
