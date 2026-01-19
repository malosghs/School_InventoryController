
class EmprestimoView:
    def __init__(self, ft, animador_pagina, animador_botao, controller_main):
        self.ft = ft 
        
        self.db_inv = controller_main.inventario if hasattr(controller_main, 'inventario') else controller_main
        self.db_user = controller_main.database if hasattr(controller_main, 'database') else controller_main
        
        self.dd_item = self.ft.Dropdown(
            label="Selecione o Item Disponível", 
            width=400,
            prefix_icon=self.ft.Icons.DEVICES,
            hint_text="Apenas itens com status 'Disponível' aparecem aqui"
        )
        
        self.dd_user = self.ft.Dropdown(
            label="Selecione o Responsável", 
            width=400,
            prefix_icon=self.ft.Icons.PERSON
        )
        
        self.btn_confirmar = self.ft.ElevatedButton(
            "Confirmar Empréstimo",
            icon=self.ft.Icons.CHECK,
            width=400,
            height=50,
            bgcolor=self.ft.Colors.BLUE_600,
            color=self.ft.Colors.WHITE,
            style=self.ft.ButtonStyle(shape=self.ft.RoundedRectangleBorder(radius=8)),
            on_click=self.salvar
        )

        self.page = self.build()
        self.carregar_dados()

    def build(self):
        return self.ft.Container(
            expand=True, 
            padding=30, 
            bgcolor="#f4f7f6", 
            alignment=self.ft.alignment.center,
            content=self.ft.Container(
                padding=40, 
                bgcolor="white", 
                border_radius=15, 
                shadow=self.ft.BoxShadow(blur_radius=20, color=self.ft.Colors.BLACK12),
                content=self.ft.Column([
                    self.ft.Row([
                        self.ft.Icon(self.ft.Icons.OUTBOX, size=40, color=self.ft.Colors.BLUE_800),
                        self.ft.Text("Registrar Empréstimo", size=26, weight=self.ft.FontWeight.BOLD, color="#333"),
                    ], alignment="center"),
                    
                    self.ft.Divider(height=30, color="transparent"),
                    
                    self.dd_item,
                    
                    self.ft.Divider(height=10, color="transparent"),
                    
                    self.dd_user,
                    
                    self.ft.Divider(height=30, color="transparent"),
                    
                    self.btn_confirmar
                    
                ], horizontal_alignment="center", spacing=10, width=450)
            )
        )

    def carregar_dados(self):
        try:
            todos_itens = self.db_inv.get_todos_itens()
            itens_disponiveis = [i for i in todos_itens if i.get('Sts') == "Disponível"]
            
            self.dd_item.options = [
                self.ft.dropdown.Option(
                    key=str(i['id']), 
                    text=f"{i['Cod']} - {i['Nome']} ({i['Cat']})"
                ) for i in itens_disponiveis
            ]
        except Exception as e:
            print(f"Erro ao carregar itens: {e}")
            self.dd_item.options = []

      
        try:
            todos_users = self.db_user.get_todos_usuarios()
            self.dd_user.options = [
                self.ft.dropdown.Option(
                    key=u['Nome'], 
                    text=f"{u['Nome']} - {u['Cargo']}"
                ) for u in todos_users
            ]
        except Exception as e:
            print(f"Erro ao carregar usuários: {e}")
            self.dd_user.options = []

        try: 
            self.page.update()
        except: 
            pass

    def salvar(self, e):
        if not self.dd_item.value:
            self._notificar(e.page, "Erro: Selecione um item!", "red")
            return
                
        if not self.dd_user.value:
            self._notificar(e.page, "Erro: Selecione um responsável!", "red")
            return

        try:
            item_id = int(self.dd_item.value)

            nome_usuario = self.dd_user.value

            with self.db_user.database.conn.cursor() as cursor:
                cursor.execute("SELECT id FROM controller_users WHERE nome_user = %s", (nome_usuario,))
                result = cursor.fetchone()
                if not result:
                    self._notificar(e.page, "Erro: Usuário não encontrado!", "red")
                    return
                id_usuario = result[0]

            ok, msg = self.db_inv.realizar_emprestimo(item_id, id_usuario)
            if ok:
                self._notificar(e.page, msg, "green")
                self.dd_item.value = None
                self.dd_user.value = None
                self.carregar_dados()
            else:
                self._notificar(e.page, msg, "red")

        except Exception as ex:
            self._notificar(e.page, f"Erro ao salvar empréstimo: {ex}", "red")

        e.page.update()


    def _notificar(self, page, texto, cor):
        if page:
            page.snack_bar = self.ft.SnackBar(self.ft.Text(texto), bgcolor=cor)
            page.snack_bar.open = True
            page.update()