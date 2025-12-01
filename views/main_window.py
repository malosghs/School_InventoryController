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

            sidebar = ft.NavigationRail()
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=90,
            min_extended_width=220,
            group_alignment=-0.2,      # Ícones mais pra baixo 👇
            indicator_color=ft.colors.BLUE_GREY_100,
            indicator_shape=ft.RoundedRectangleBorder(radius=12),
            leading=ft.Container(height=80),     # empurra o menu pra baixo
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Container(
                        width=40,
                    ))]