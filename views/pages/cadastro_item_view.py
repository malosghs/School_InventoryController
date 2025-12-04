
class CadastroItemView:
    
    def __init__(self,ft, animador_pagina, animador_botao, controller):
 
        
        self.ft = ft 

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller

        self.expand = True

        self.page =self.ft.Column(
           
            scroll=self.ft.ScrollMode.AUTO,
            controls=[
                self.ft.Text("Cadastro de Item", size=26, weight=self.ft.FontWeight.BOLD),
                self.ft.TextField(label="Nome do Item"),
                self.ft.TextField(label="Codificação"),
                self.ft.Dropdown(label="Categoria", options=[
                    self.ft.dropdown.Option("Cabeça"),
                    self.ft.dropdown.Option("Mãos"),
                    self.ft.dropdown.Option("Corpo"),
                ]),
                self.ft.Dropdown(label="Tipo", options=[
                    self.ft.dropdown.Option("Capacete"),
                    self.ft.dropdown.Option("Luva"),
                    self.ft.dropdown.Option("Jaleco"),
                ]),
                self.ft.TextField(label="Localização"),
                self.ft.Dropdown(label="Estado", options=[
                    self.ft.dropdown.Option("Novo"),
                    self.ft.dropdown.Option("Em uso"),
                    self.ft.dropdown.Option("Danificado"),
                ]),
                self.ft.ElevatedButton("Salvar Item")
            ]
        )

    def salvar(self, e):
        print("Item salvo!")  # aqui vai ao DB
