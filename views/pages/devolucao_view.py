
class DevolucaoView:
    def __init__(self, ft, animador_pagina, animador_botao, controller_main):
        self.ft = ft
 
        self.db_inv = controller_main.inventario if hasattr(controller_main, 'inventario') else controller_main
        
        self.dd_item = self.ft.Dropdown(
            label="Selecione o Item a Devolver",
            width=450,
            prefix_icon=self.ft.Icons.INVENTORY_2,
            hint_text="Apenas itens emprestados aparecem aqui"
        )
        
        self.input_obs = self.ft.TextField(
            label="Observações / Relato de Avarias",
            width=450,
            prefix_icon=self.ft.Icons.NOTE,
            multiline=True,
            min_lines=1,
            max_lines=3
        )

        self.btn_confirmar = self.ft.ElevatedButton(
            "Confirmar Devolução",
            icon=self.ft.Icons.CHECK_CIRCLE,
            width=450,
            height=50,
            bgcolor=self.ft.Colors.ORANGE_700, 
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
                        self.ft.Icon(self.ft.Icons.MOVE_TO_INBOX, size=40, color=self.ft.Colors.ORANGE_800),
                        self.ft.Text("Registrar Devolução", size=26, weight=self.ft.FontWeight.BOLD, color="#333"),
                    ], alignment="center"),
                    
                    self.ft.Divider(height=30, color="transparent"),
                    
                    self.dd_item,
                    
                    self.ft.Divider(height=10, color="transparent"),
                    
                    self.input_obs,
                    
                    self.ft.Divider(height=30, color="transparent"),
                    
                    self.btn_confirmar
                    
                ], horizontal_alignment="center", spacing=10, width=500)
            )
        )

    def carregar_dados(self):
       
        try:
            todos_itens = self.db_inv.get_todos_itens()

            itens_emprestados = [i for i in todos_itens if i.get('Sts') == "Emprestado"]
            
            if not itens_emprestados:
                self.dd_item.options = []
                self.dd_item.hint_text = "Nenhum item pendente de devolução"
                self.dd_item.disabled = True
            else:
                self.dd_item.disabled = False
                self.dd_item.hint_text = "Selecione..."
               
                self.dd_item.options = [
                    self.ft.dropdown.Option(
                        key=str(i['id']), 
                        text=f"{i['Cod']} - {i['Nome']} (Com: {i.get('Resp', 'Unknown')})"
                    ) for i in itens_emprestados
                ]
            
            self.dd_item.update()
        except Exception as e:
            print(f"Erro ao carregar devoluções: {e}")

    def salvar(self, e):
     
        if not self.dd_item.value:
            self._notificar(e.page, "Erro: Selecione um item para devolver!", "red")
            return

        id_item = int(self.dd_item.value)
        obs = self.input_obs.value

        ok, msg = self.db_inv.realizar_devolucao(id_item, obs)

        if ok:
            self._notificar(e.page, msg, "green")
            
        
            self.dd_item.value = None
            self.input_obs.value = ""
            
            self.carregar_dados()
            self.page.update()
        else:
            self._notificar(e.page, msg, "red")

    def _notificar(self, page, texto, cor):
        if page:
            page.snack_bar = self.ft.SnackBar(self.ft.Text(texto), bgcolor=cor)
            page.snack_bar.open = True
            page.update()