

class DevolucaoView:
    def __init__(self,ft, animador_pagina, animador_botao, controller):
 
        
        self.ft = ft 

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller



        self.filtro = self.ft.TextField(label="Buscar Item ou Funcionário")
        self.page = self.ft.Column([
            self.ft.Text("Devolução de Item", size=26, weight=self.ft.FontWeight.BOLD),

            self.filtro,

            self.ft.Dropdown(label="Categoria"),
            self.ft.Dropdown(label="Tipo"),

            self.ft.Text("Estado ao retornar"),
            self.ft.Dropdown(label="Teve dano?", options=[
                self.ft.dropdown.Option("Sim"),
                self.ft.dropdown.Option("Não"),
            ]),

            self.ft.TextField(label="Relato de uso / observações"),

            self.ft.ElevatedButton("Confirmar Devolução")
        ],
        expand = True,
        alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.START
)