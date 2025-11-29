import flet as ft

class DevolucaoView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.filtro = ft.TextField(label="Buscar Item ou Funcionário")
        self.controls = [
            ft.Text("Devolução de Item", size=26, weight=ft.FontWeight.BOLD),

            self.filtro,

            ft.Dropdown(label="Categoria"),
            ft.Dropdown(label="Tipo"),

            ft.Text("Estado ao retornar"),
            ft.Dropdown(label="Teve dano?", options=[
                ft.dropdown.Option("Sim"),
                ft.dropdown.Option("Não"),
            ]),

            ft.TextField(label="Relato de uso / observações"),

            ft.ElevatedButton("Confirmar Devolução")
        ]
