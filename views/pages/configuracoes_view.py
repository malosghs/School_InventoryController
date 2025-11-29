import flet as ft

class ConfiguracoesView(ft.Tabs):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.tabs = [
            ft.Tab(text="Usuários", content=self.usuarios_tab()),
            ft.Tab(text="Dados de Itens", content=self.config_item_tab())
        ]

    def usuarios_tab(self):
        return ft.Column([
            ft.Text("Gerenciamento de Usuários", size=22, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Adicionar Usuário")
        ])

    def config_item_tab(self):
        return ft.Column([
            ft.Text("Configurações de Itens", size=22, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton("Adicionar Categoria / Tipo")
        ])
