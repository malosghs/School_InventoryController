

class LoginView:
    def __init__(self,ft, animador_pagina, animador_botao, controller):
 
        
        self.ft = ft 

        self.animador_pagina = animador_pagina
        self.animador_botao = animador_botao
        self.controller = controller


    
        self.expand = True
        self.alignment = self.ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = self.ft.CrossAxisAlignment.CENTER

        self.username = self.ft.TextField(label="Usuário / Email / CPF", width=300)
        self.password = self.ft.TextField(label="Senha", password=True, width=300)

        self.page =self.ft.Column([
            self.ft.Text("Sistema de Controle de Itens", size=32, weight=self.ft.FontWeight.BOLD),
            self.username,
            self.password,
            self.ft.ElevatedButton("Acessar", width=200, on_click=self.login)
        ],
         expand = True,
         alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

    def login(self, e):
        # Validação mínima para teste
        self.page.go("/home")
