import flet as ft

class MainPageView:
    def __init__(self, page: ft.Page, animador_pagina, animador_botao, controller):
        self.page = page
        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller

    def construir_main_page(self):

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

            destinations=[
                ft.NavigationRailDestination(
                    icon="home",          # <-- COMPATÍVEL COM A TUA VERSÃO
                    label="Início",
                ),
                ft.NavigationRailDestination(
                    icon="inventory",
                    label="Inventário",
                ),
                ft.NavigationRailDestination(
                    icon="settings",
                    label="Configurações",
                ),
            ]
        )

        # -------------------
        # LAYOUT
        # -------------------

        layout = ft.Row(
            expand=True,
            controls=[
                sidebar,
                ft.VerticalDivider(width=1),
                ft.Container(
                    expand=True,
                    content=ft.Text("Conteúdo principal aqui...", size=20),
                ),
            ],
        )

        return layout
