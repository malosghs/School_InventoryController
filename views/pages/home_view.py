

class HomeView:
    def __init__(self,animador_pagina, animador_botao, controller):

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller

        self.dict_status_tela = None 
        self.filters = None
        self.itens = None

        self.page = ft.Conteiner(
            alignment=ft.MainAxisAlignment.CENTER,
            controls = [
            ft.Container( # Filtros
                controls=self.filters,
                expand = True,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                width=400,
                height=100,
                border_radius=10,
        ), 
            ft.Conteiner( # Itens 
                expand = True,
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                width=450,
                height=350,
                content = ft.Row(
                    controls =  self.itens
                )
        )
        
            ],
        )

      
    def page_open():
        self.controls = [
            
            ft.Text("Dashboard", size=26, weight=ft.FontWeight.BOLD),

            ft.Row([
               
            ])
        ]
async def gerador_cards(self,list_items):
        self.itens =  self.animador_pagina.carregamento_animacao()    
        
        itens = []

        
        for modelItem in list_items:
                self.itens.append(
                    ft.Card(
                    leading=ft.IconButton(
                    icon = ft.Icons.INFO,
                   # on_click = 
                    ),
                    content=ft.Container(
                    content=ft.Column(
                    [
                        ft.ListTile(
                           
                            title=ft.Text(modelItem.item.nome),
                            subtitle=ft.Text(
                            "# Depois preencher "
                        ),
                        bgcolor=ft.Colors.GREY_400,
                        ),
                        ft.Row(
                             [ 
                            [ft.TextButton(modelItem.item.status_butao)]
                             ],
                             alignment=ft.MainAxisAlignment.Center,
                        ),
                    ]
                    ),
                    width=100,
                    height=150,
                    padding=10,
                    ),
                    shadow_color=ft.Colors.ON_SURFACE_VARIANT,
                    )
                )
        self.itens = itens

    
