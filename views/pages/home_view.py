

class HomeView:
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
      
      

    
async def gerador_cards(self,list_items):
        self.itens =  self.animador_pagina.carregamento_animacao()    
        banco = [{
        "id":0,
        "Nome_do_Item": "Mouse USB",
        "Codificacao": "IT-001",
        "Categoria": "Periférico",
        "Tipo": "Mouse",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Mouse USB padrão para estações de trabalho.",
        "":"Emprestar"
    },
    {  
        "id":1,
        "Nome_do_Item": "Teclado USB",
        "Codificacao": "IT-002",
        "Categoria": "Periférico",
        "Tipo": "Teclado",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Teclado USB padrão ABNT2.",
        "":"Emprestar"
    },
    {
        "id":2,
        "Nome_do_Item": "Headset com Microfone",
        "Codificacao": "IT-003",
        "Categoria": "Áudio",
        "Tipo": "Headset",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Headset com microfone para reuniões e chamadas.",
        "":"Emprestar"
    },
    { 
        "id":3,
        "Nome_do_Item": "Cabo HDMI 1.8m",
        "Codificacao": "IT-004",
        "Categoria": "Cabos",
        "Tipo": "HDMI",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Cabo HDMI de 1.8 metros para vídeo.",
        "":"Emprestar"
    },
    {
         "id":4,
        "Nome_do_Item": "Cabo VGA 1.5m",
        "Codificacao": "IT-005",
        "Categoria": "Cabos",
        "Tipo": "VGA",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Cabo VGA de 1.5 metros para monitores antigos.",
        "":"Emprestar"
    },
    {
         "id":5,
        "Nome_do_Item": "Adaptador USB-C → HDMI",
        "Codificacao": "IT-006",
        "Categoria": "Adaptadores",
        "Tipo": "USB-C para HDMI",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Adaptador para conectar USB-C a HDMI.",
        "":"Emprestar"
    },
    {
         "id":6,
        "Nome_do_Item": "Pen Drive 32GB",
        "Codificacao": "IT-007",
        "Categoria": "Armazenamento",
        "Tipo": "Pen Drive",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Pen drive de 32GB.",
        "":"Emprestar"
    },
    {
         "id":7,
        "Nome_do_Item": "Roteador Wi-Fi",
        "Codificacao": "IT-008",
        "Categoria": "Rede",
        "Tipo": "Roteador",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Roteador Wi-Fi padrão para redes locais.",
        "":"Emprestar"
    },
    {
         "id":8,
        "Nome_do_Item": "Switch 24 portas",
        "Codificacao": "IT-009",
        "Categoria": "Rede",
        "Tipo": "Switch",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Switch gerenciável de 24 portas.",
        "":"Emprestar"
    },
    {
        "id":9,
        "Nome_do_Item": "Patch Cords diversos",
        "Codificacao": "IT-010",
        "Categoria": "Cabos de Rede",
        "Tipo": "Patch Cord",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Patch cords de vários tamanhos e cores.",
        "":"Emprestar"
    },
    {
        "id":10, 
        "Nome_do_Item": "Nobreak 1400VA",
        "Codificacao": "IT-011",
        "Categoria": "Energia",
        "Tipo": "Nobreak",
        "Localizacao": "Almoxarifado",
        "Estado_de_Uso": "Novo",
        "Status": "Disponível",
        "Descricao": "Nobreak 1400VA para proteção de equipamentos.",
        "":"Emprestar"
    }
        ]
       
        itens = [i for i in banco ]

        
        for modelItem in itens:#list_items:
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

    
