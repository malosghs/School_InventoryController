

class MainPageView:
    def __init__(self, page ,ft , animador_pagina, animador_botao, controller,main_window):
        self.page = page
        self.ft = ft 
        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller
        self.main_window = main_window
        self.main_window.homeView = self.main_window.homeView(self.ft,self.animador_botao,self.animador_botao,self.controller)
        self.page_status = self.animador_pagina(self.ft).carregamento_animacao()
        self.construir_main_page
         
        
      

    def open_home(self):
     
        self.page_status = self.main_window.homeView.page
        self.page_status.update()

    def open_cadastroItem(self):
    
        self.page_status = self.ft.Text("ola")  
        self.page_status.update()

    def construir_main_page(self):
        self.page.title = "School Inventory"
        self.page.window_width = 500
        self.page.window_height = 400
        self.page.window_resizable = False
        self.page.theme_mode = self.ft.ThemeMode.LIGHT
        self.page.padding = 0
        self.page.margin = 0
       #
       #  F8F8F0 Cor cinza gelo 
        
  

        # -------------------
        # SIDEBAR
        # -------------------


        sidebar = self.ft.NavigationRail(

            selected_index=0,
            label_type=self.ft.NavigationRailLabelType.ALL,
            min_width=90,
            min_extended_width=220,
            group_alignment=-0.2,
            indicator_color=self.ft.Colors.BLUE_GREY_100,
            indicator_shape=self.ft.RoundedRectangleBorder(radius=12),
            leading=self.ft.Container(height=80),
            on_change=lambda e: self.controller.page_guia_open(e.control.selected_index),

            destinations=[
                self.ft.NavigationRailDestination(
                    icon="home",          # <-- COMPATÍVEL COM A TUA VERSÃO
                    label="Home",
                    selected_icon = self.ft.Icons.HOME_OUTLINED
                ),
                
                self.ft.NavigationRailDestination(
                    icon= self.ft.Icons.OUTBOX,
                    label="Emprestar",
                    selected_icon = self.ft.Icons.OUTBOX_OUTLINED
                ),
                 self.ft.NavigationRailDestination(
                    icon=self.ft.Icons.MOVE_TO_INBOX_ROUNDED,
                    label="Devoluçao",
                    selected_icon = self.ft.Icons.MOVE_TO_INBOX_OUTLINED
                ),
                self.ft.NavigationRailDestination(
                    icon="inventory",
                    label="Inventário",
                    selected_icon = self.ft.Icons.INVENTORY_2_OUTLINED
                ),
                self.ft.NavigationRailDestination(
                    icon="settings",
                    label="Configurações",
                    selected_icon = self.ft.Icons.SETTINGS_OUTLINED
                ),
            ]
            
        )

        self.tela_context =  self.ft.Container(
                    expand=True,
                    content=self.ft.Text("Conteúdo principal aqui...", size=20),
                ),

 
 

         
      

        self.controls = [
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


        layout = self.ft.Column(
            expand= True,
            controls= [     
         self.ft.Container(
            content=self.ft.Text(
                "School Inventory Controller ",
                size=30,
                weight=self.ft.FontWeight.W_900,
                selectable=True,
            ),
            margin=self.ft.margin.symmetric(vertical=30),
            padding=30,
            bgcolor="grey200",
            alignment=self.ft.alignment.center,
),
         self.ft.Row(
            expand=True,
            controls=[
                sidebar,
                self.ft.VerticalDivider(width=1),
                self.page_status               
                 
         
                
               
            ],
        )
        
     
            ]
        )
        self.page.add(layout)
       