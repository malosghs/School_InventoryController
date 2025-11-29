import flet as ft

class CadastroItemView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True

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

            ft.ElevatedButton("Salvar Item", on_click=self.salvar)
        ]

    def salvar(self, e):
        print("Item salvo!")  # aqui vai ao DB
