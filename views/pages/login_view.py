import flet as ft

class LoginView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.expand = True
        self.alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.username = ft.TextField(label="Usuário / Email / CPF", width=300)
        self.password = ft.TextField(label="Senha", password=True, width=300)

        self.controls = [
            ft.Text("Sistema de Controle de Itens", size=32, weight=ft.FontWeight.BOLD),
            self.username,
            self.password,
            ft.ElevatedButton("Acessar", width=200, on_click=self.login)
        ]

    def login(self, e):
        # Validação mínima para teste
        self.page.go("/home")
