import flet as ft

class MainPageView:
    def __init__(self, page: ft.Page, animador_pagina, animador_botao, controller,main_window):
        self.page = page
        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller
        self.main_window = main_window

    def construir_main_page(self):
        self.page.title = "School Inventory"
        self.page.window_width = 500
        self.page.window_height = 400
        self.page.window_resizable = False
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 0
        self.page.margin = 0
       #
       #  F8F8F0 Cor cinza gelo 
        
  

        # -------------------
        # SIDEBAR
        # -------------------


        sidebar = ft.NavigationRail(

            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=90,
            min_extended_width=220,
            group_alignment=-0.2,
            indicator_color=ft.Colors.BLUE_GREY_100,
            indicator_shape=ft.RoundedRectangleBorder(radius=12),
            leading=ft.Container(height=80),
            on_change=lambda e: print("Selected destination:", e.control.selected_index),

            destinations=[
                ft.NavigationRailDestination(
                    icon="home",          # <-- COMPATÍVEL COM A TUA VERSÃO
                    label="Home",
                    selected_icon = ft.Icons.HOME_OUTLINED
                ),
                
                ft.NavigationRailDestination(
                    icon= ft.Icons.OUTBOX,
                    label="Emprestar",
                    selected_icon = ft.Icons.OUTBOX_OUTLINED
                ),
                 ft.NavigationRailDestination(
                    icon=ft.Icons.MOVE_TO_INBOX_ROUNDED,
                    label="Devoluçao",
                    selected_icon = ft.Icons.MOVE_TO_INBOX_OUTLINED
                ),
                ft.NavigationRailDestination(
                    icon="inventory",
                    label="Inventário",
                    selected_icon = ft.Icons.INVENTORY_2_OUTLINED
                ),
                ft.NavigationRailDestination(
                    icon="settings",
                    label="Configurações",
                    selected_icon = ft.Icons.SETTINGS_OUTLINED
                ),
            ]
            
        )

        self.tela_context =  ft.Container(
                    expand=True,
                    content=ft.Text("Conteúdo principal aqui...", size=20),
                ),

 
 

         
      

        self.controls = [
            ft.Text("Cadastro de Item", size=26, weight=ft.FontWeight.BOLD),

            ft.TextField(label="Nome do Item"),
            ft.TextField(label="Codificação"),

            ft.Dropdown(label="Categoria", options=[
                ft.dropdown.Option("Cabeça"),
                ft.dropdown.Option("Mãos"),
                ft.dropdown.Option("Corpo"),
            ]),

            ft.Dropdown(label="Tipo", options=[
                ft.dropdown.Option("Capacete"),
                ft.dropdown.Option("Luva"),
                ft.dropdown.Option("Jaleco"),
            ]),

            ft.TextField(label="Localização"),

            ft.Dropdown(label="Estado", options=[
                ft.dropdown.Option("Novo"),
                ft.dropdown.Option("Em uso"),
                ft.dropdown.Option("Danificado"),
            ]),

            ft.ElevatedButton("Salvar Item")
        ]


        layout = ft.Column(
            expand= True,
            controls= [     
         ft.Container(
            content=ft.Text(
                "School Inventory Controller ",
                size=30,
                weight=ft.FontWeight.W_900,
                selectable=True,
            ),
            margin=ft.margin.symmetric(vertical=30),
            padding=30,
            bgcolor="grey200",
            alignment=ft.alignment.center,
),
         ft.Row(
            expand=True,
            controls=[
                sidebar,
                ft.VerticalDivider(width=1),
                
                 
         
                
               
            ],
        )
        
     
            ]
        )
        self.page.add(layout)
       