

class InventarioView:
    def __init__(self,ft, animador_pagina, animador_botao, controller):
 
        
        self.ft = ft 

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller

        self.dict_status_tela = None 
        self.filters = self.ft.Text("OLa")
        self.itens = None

        self.page = self.ft.Column(
           
            
            [
            self.ft.Container( # Filtros
              
                content=self.filters,
                margin=10,
                padding=10,
                alignment=self.ft.alignment.center,
                bgcolor=self.ft.Colors.GREY,
                width=1100,
                height=120,
             
                border_radius=10,
        ), 
            self.ft.Container( # Itens 
                expand = True,
                margin=10,
                padding=10,
                alignment=self.ft.alignment.center,
                bgcolor=self.ft.Colors.GREY,
                width=1350,
                border_radius=7,
                content = self.ft.Row(
                    controls =  self.itens
                )
        )
        
            ],
            expand = True,
            alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
           
        )
      
      
    def page_open():
        self.controls = [
            
            self.ft.Text("Dashboard", size=26, weight=self.ft.FontWeight.BOLD),

            self.ft.Row([
               
            ])
        ]
    
async def gerador_cards(self,list_items):
        self.itens =  self.animador_pagina.carregamento_animacao()    
        
        itens = []

        
        for modelItem in list_items:
                self.itens.append(
                    self.ft.Card(
                    leading=self.ft.IconButton(
                    icon = self.ft.Icons.INFO,
                   # on_click = 
                    ),
                    content=self.ft.Container(
                    content=self.ft.Column(
                    [
                        self.ft.ListTile(
                           
                            title=self.ft.Text(modelItem.item.nome),
                            subtitle=self.ft.Text(
                            "# Depois preencher "
                        ),
                        bgcolor=self.ft.Colors.GREY_400,
                        ),
                        self.ft.Row(
                             [ 
                            [self.ft.TextButton(modelItem.item.status_butao)]
                             ],
                             alignment=self.ft.MainAxisAlignment.Center,
                        ),
                    ]
                    ),
                    width=100,
                    height=150,
                    padding=10,
                    ),
                    shadow_color=self.ft.Colors.ON_SURFACE_VARIANT,
                    )
                )
        self.itens = itens

    
