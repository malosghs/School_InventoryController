import flet as ft
from views.componentes.topbar_menu import TopBarMenu
from views.componentes.card_item import CardItem

class HomeView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.expand = True

        self.controls = [
            TopBarMenu(page),
            ft.Text("Dashboard", size=26, weight=ft.FontWeight.BOLD),

            ft.Row([
                CardItem("Itens em Estoque", "120"),
                CardItem("Empréstimos Ativos", "32"),
                CardItem("Itens em Manutenção", "5"),
            ])
        ]
