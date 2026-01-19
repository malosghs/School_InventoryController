from datetime import datetime

class HomeView:
    def __init__(self, ft, animador_pagina, animador_botao, controller_main):
        self.ft = ft
        self.controller = controller_main

        self.db_inv = controller_main.inventario if hasattr(controller_main, 'inventario') else None
        self.db_user = controller_main.database if hasattr(controller_main, 'database') else None

        self.card_total, self.txt_total = self._build_card("Total Itens", "0", self.ft.Icons.INVENTORY_2, "blue")
        self.card_disp, self.txt_disp = self._build_card("Disponíveis", "0", self.ft.Icons.CHECK_CIRCLE, "green")
        self.card_emp, self.txt_emp = self._build_card("Emprestados", "0", self.ft.Icons.OUTBOX, "orange")
        self.card_users, self.txt_users = self._build_card("Usuários", "0", self.ft.Icons.PEOPLE, "purple")

        self.lista_alertas = self.ft.ListView(expand=True, spacing=10, padding=10)

        self.page = self.build()
        self.atualizar_dados()

    def build(self):
        return self.ft.Container(
            expand=True,
            padding=30,
            bgcolor="#f4f7f6",
            content=self.ft.Column([
                self.ft.Text("Dashboard Geral", size=30, weight="bold", color="#2c3e50"),
                self.ft.Divider(height=20, color="transparent"),

                self.ft.Row([
                    self.card_total,
                    self.card_disp,
                    self.card_emp,
                    self.card_users
                ], alignment="spaceBetween"),

                self.ft.Divider(height=30, color="transparent"),

                self.ft.Container(
                    expand=True,
                    bgcolor="white",
                    border_radius=15,
                    padding=20,
                    shadow=self.ft.BoxShadow(blur_radius=10, color=self.ft.Colors.BLACK12),
                    content=self.ft.Column([
                        self.ft.Row([
                            self.ft.Icon(self.ft.Icons.WARNING_AMBER_ROUNDED, color="red", size=28),
                            self.ft.Text("Alertas & Status", size=20, weight="bold", color="#333")
                        ]),
                        self.ft.Divider(),
                        self.lista_alertas
                    ])
                )
            ])
        )

    def _build_card(self, titulo, valor, icone, cor):
        numero = self.ft.Text(valor, size=32, weight="bold", color="#333")
        card = self.ft.Container(
            width=220, height=120,
            bgcolor="white",
            border_radius=15,
            padding=20,
            shadow=self.ft.BoxShadow(blur_radius=10, color=self.ft.Colors.BLACK12),
            content=self.ft.Column([
                self.ft.Row([
                    self.ft.Icon(icone, color=cor, size=30),
                    self.ft.Text(titulo, color="grey", weight="bold")
                ], alignment="spaceBetween"),
                numero
            ], alignment="spaceBetween")
        )
        return card, numero

    def atualizar_dados(self):
        if not self.db_inv or not self.db_user:
            return

        itens = self.db_inv.get_todos_itens()
        users = self.db_user.get_todos_usuarios()

        total = len(itens)
        emp = len([i for i in itens if i.get('Sts') == "Emprestado"])
        disp = total - emp
        total_users = len(users)

        self.txt_total.value = str(total)
        self.txt_disp.value = str(disp)
        self.txt_emp.value = str(emp)
        self.txt_users.value = str(total_users)

        self.lista_alertas.controls.clear()
        emprestados = [i for i in itens if i.get('Sts') == "Emprestado"]

        if not emprestados:
            self.lista_alertas.controls.append(
                self.ft.Text("Nenhum item pendente de devolução.", color="green")
            )
        else:
            for item in emprestados:
                resp = item.get('Resp', 'Desconhecido')
                nome = item.get('Nome', 'Sem nome')
                cod = item.get('Cod', '-')
                self.lista_alertas.controls.append(
                    self.ft.ListTile(
                        leading=self.ft.Icon(self.ft.Icons.CIRCLE, color="orange", size=15),
                        title=self.ft.Text(f"{nome} ({cod})"),
                        subtitle=self.ft.Text(f"Responsável: {resp}"),
                        trailing=self.ft.Icon(self.ft.Icons.ARROW_FORWARD_IOS, size=14)
                    )
                )

        try:
            self.page.update()
        except:
            pass
