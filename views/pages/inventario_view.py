

class InventarioView:
    def __init__(self, ft, animador_pagina, animador_botao, controller_main):
        self.ft = ft
      
        self.db = controller_main.inventario if hasattr(controller_main, 'inventario') else controller_main
        
        self.grid = self.ft.GridView(expand=True, runs_count=5, max_extent=300, child_aspect_ratio=0.8, spacing=10)
        self.txt_total = self.ft.Text("0", size=24, weight="bold")
        
       
        self.input_nome = self.ft.TextField(label="Nome")
        self.input_qtd = self.ft.TextField(label="Qtd", value="1")
        self.input_cat = self.ft.Dropdown(label="Categoria", options=[self.ft.dropdown.Option("Geral"), self.ft.dropdown.Option("Hardware")])
        self.input_loc = self.ft.Dropdown(label="Local", options=[self.ft.dropdown.Option("Depósito"), self.ft.dropdown.Option("TI")])
        
        self.page = self.build()
        self.carregar()

    def build(self):
        return self.ft.Container(expand=True, padding=20, bgcolor="#f4f7f6", content=self.ft.Column([
            self.ft.Container(padding=15, bgcolor="white", border_radius=10, content=self.ft.Row([
                self.ft.Icon(self.ft.Icons.INVENTORY, size=30), self.ft.Column([self.ft.Text("Total no Inventário"), self.txt_total])
            ])),
            self.ft.Divider(height=20, color="transparent"),
            self.ft.ElevatedButton("Adicionar Item", icon=self.ft.Icons.ADD, height=50, bgcolor="blue", color="white", on_click=self.abrir_add),
            self.ft.Divider(),
            self.grid
        ]))

    def carregar(self):
        self.grid.controls.clear()
        itens = self.db.get_todos_itens()
        self.txt_total.value = str(len(itens))
        for i in itens: self.grid.controls.append(self._card(i))
        try: self.page.page.update()
        except: pass

    def _card(self, i):
       
        disp = i['Sts'] == "Disponível"
        cor = "green" if disp else "red"
        txt_btn = "Emprestar" if disp else "Devolver"
        cor_btn = "blue" if disp else "orange"
        
        return self.ft.Card(elevation=4, content=self.ft.Container(padding=10, bgcolor="white", border_radius=10, content=self.ft.Column([
        
            self.ft.Row([
                self.ft.Container(bgcolor="#f0f0f0", padding=5, border_radius=5, content=self.ft.Text(i['Cod'], size=10, weight="bold")),
                self.ft.Container(expand=True),
             
                self.ft.IconButton(self.ft.Icons.INFO, icon_size=20, icon_color="blue", tooltip="Ver Detalhes", on_click=lambda e: self.ver_info(e, i)),
              
                self.ft.IconButton(self.ft.Icons.DELETE, icon_size=20, icon_color="red", tooltip="Remover", on_click=lambda e: self.deletar(i['id']))
            ]),
            
          
            self.ft.Text(i['Nome'], weight="bold", size=16, max_lines=1),
            self.ft.Text(f"Loc: {i['Loc']}", size=12, color="grey"),
            self.ft.Container(padding=5, bgcolor=cor+"100", border_radius=15, content=self.ft.Text(i['Sts'], color=cor, size=11)),
            self.ft.Divider(height=10, color="transparent"),
            
           
            self.ft.ElevatedButton(text=txt_btn, width=float("inf"), bgcolor=cor_btn, color="white", on_click=lambda e: self.acao(e, i['id']))
        ])))

    def ver_info(self, e, i):
        conteudo = [
            self.ft.Text(f"Nome: {i['Nome']}", size=16, weight="bold"),
            self.ft.Text(f"Código: {i['Cod']}"),
            self.ft.Text(f"Categoria: {i['Cat']}"),
            self.ft.Text(f"Local: {i['Loc']}"),
            self.ft.Divider(),
            self.ft.Text(f"Status: {i['Sts']}", color="green" if i['Sts']=="Disponível" else "red", weight="bold"),
        ]
        if i['Sts'] == "Emprestado":
            conteudo.append(self.ft.Text(f"Responsável: {i['Resp']}", size=14, weight="bold", color="blue"))

        dlg = self.ft.AlertDialog(title=self.ft.Text("Detalhes"), content=self.ft.Column(conteudo, height=200))
        e.page.dialog = dlg; dlg.open = True; e.page.update()

    def acao(self, e, uid):
        ok, msg = self.db.alternar_status(uid)
        if ok: 
            self.carregar()
            e.page.show_snack_bar(self.ft.SnackBar(self.ft.Text(msg), bgcolor="green"))

    def abrir_add(self, e):
        def salvar(evt):
            self.db.salvar_novos_itens(self.input_nome.value, self.input_cat.value, self.input_qtd.value, self.input_loc.value)
            evt.page.dialog.open = False; evt.page.update(); self.carregar()

        dlg = self.ft.AlertDialog(title=self.ft.Text("Novo Item"), content=self.ft.Column([self.input_nome, self.input_cat, self.input_loc, self.input_qtd], height=250), actions=[self.ft.ElevatedButton("Salvar", on_click=salvar)])
        e.page.dialog = dlg; dlg.open = True; e.page.update()

    def deletar(self, uid):
        self.db.deletar_item(uid); self.carregar()