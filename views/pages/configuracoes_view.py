

class ConfiguracoesView:
    def __init__(self,ft, animador_pagina, animador_botao, controller):
 
        
        self.ft = ft 

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller




        self.page =self.ft.Column( [
            self.ft.Tab(text="Usuários", content=self.usuarios_tab()),
            self.ft.Tab(text="Dados de Itens", content=self.config_item_tab())
        ],
        expand = True,
        alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

    def usuarios_tab(self):
        return self.ft.Column([
            self.ft.Text("Gerenciamento de Usuários", size=22, weight=self.ft.FontWeight.BOLD),
            self.ft.ElevatedButton("Adicionar Usuário")
        ])

    def config_item_tab(self):
        return self.ft.Column([
            self.ft.Text("Configurações de Itens", size=22, weight=self.ft.FontWeight.BOLD),
            self.ft.ElevatedButton("Adicionar Categoria / Tipo")
        ])
