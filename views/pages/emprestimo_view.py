import flet as ft

class EmprestimoView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.busca = ft.TextField(label="ID Funcionário ou Código do Item")

        self.controls = [
            ft.Text("Registrar Empréstimo", size=26, weight=ft.FontWeight.BOLD),
            self.busca,

            ft.Dropdown(label="Categoria"),
            ft.Dropdown(label="Tipo"),
            ft.Dropdown(label="Selecionar Item"),
            ft.Dropdown(label="Funcionário"),

            ft.ElevatedButton("Registrar Empréstimo")
        ]
