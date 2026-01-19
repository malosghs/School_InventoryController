

class UsuariosTab:
    def __init__(self, ft, controller_main, animador_pagina):
        self.ft = ft 
        self.db = controller_main.database 
        self.animador_pagina = animador_pagina
        self.id_em_edicao = None 

     
        self.input_nome = self.ft.TextField(label="Nome", prefix_icon=self.ft.Icons.PERSON)
        self.input_cpf = self.ft.TextField(label="CPF", prefix_icon=self.ft.Icons.BADGE)
        self.input_user = self.ft.TextField(label="Login", prefix_icon=self.ft.Icons.ALTERNATE_EMAIL)
        self.input_senha = self.ft.TextField(label="Senha", password=True, can_reveal_password=True, prefix_icon=self.ft.Icons.LOCK)
        self.dropdown_cargo = self.ft.Dropdown(
            label="Cargo", 
            options=[
                self.ft.dropdown.Option("Diretor"),
                self.ft.dropdown.Option("Professor"),
                self.ft.dropdown.Option("Secretaria")
            ],
            value="Professor"
        )

     
        self.lista_view = self.ft.ListView(expand=True, spacing=10, padding=20)

    def build(self):
        self.renderizar_lista()

    
        fab = self.ft.FloatingActionButton(
            icon=self.ft.Icons.ADD,
            text="Novo",
            bgcolor=self.ft.Colors.BLUE_600,
            on_click=lambda e: self.abrir_modal(e, None) 
        )

        return self.ft.Container(
            expand=True,
            bgcolor="#f4f7f6",
            content=self.ft.Stack([
                self.ft.Column([
                    self.ft.Container(
                        padding=15, bgcolor="white",
                        content=self.ft.Row([
                            self.ft.Icon(self.ft.Icons.MANAGE_ACCOUNTS, size=28, color="blue"),
                            self.ft.Text("Gerenciar Usuários", size=20, weight="bold")
                        ])
                    ),
                    self.ft.Divider(height=1),
                    self.ft.Container(content=self.lista_view, expand=True)
                ], expand=True),
                
               
                self.ft.Container(content=fab, right=20, bottom=20)
            ])
        )

   
    def renderizar_lista(self):
        self.lista_view.controls.clear()
        dados = self.db.get_todos_usuarios()

        if not dados:
            self.lista_view.controls.append(
                self.ft.Container(
                    alignment=self.ft.alignment.center, padding=50, 
                    content=self.ft.Text("Nenhum usuário cadastrado.", color="grey")
                )
            )
        else:
            for u in dados:
                self.lista_view.controls.append(self._criar_card(u))
        
        try:
            if self.lista_view.page: self.lista_view.update()
        except: pass

    def _criar_card(self, u):
        return self.ft.Container(
            padding=10, bgcolor="white", border_radius=8,
            shadow=self.ft.BoxShadow(blur_radius=5, color=self.ft.Colors.BLACK12),
            content=self.ft.Row([
                self.ft.Icon(self.ft.Icons.PERSON, color="blue", size=30),

                self.ft.Column([
                    self.ft.Text(u['Nome'], weight="bold"),
                    self.ft.Text(f"{u['Cargo']} | {u['User']}", size=12, color="grey")
                ], expand=True),

                self.ft.Row([
                    self.ft.IconButton(
                        icon=self.ft.Icons.EDIT, icon_color="blue", tooltip="Editar",
                        data=u,
                        on_click=lambda e: self.abrir_modal(e, e.control.data)
                    ),
                    self.ft.IconButton(
                        icon=self.ft.Icons.DELETE, icon_color="red", tooltip="Excluir",
                        data=u['id'],
                        on_click=lambda e: self.deletar(e, e.control.data)
                    )
                ])
            ])
        )



    def abrir_modal(self, e, usuario):
        self.id_em_edicao = usuario['id'] if usuario else None
        titulo = "Editar Usuário" if usuario else "Novo Usuário"
        
      
        self.input_nome.value = usuario['nome'] if usuario else ""
        self.input_cpf.value = usuario['cpf'] if usuario else ""
        self.input_user.value = usuario['user'] if usuario else ""
        self.input_senha.value = "" 
        self.dropdown_cargo.value = usuario['cargo'] if usuario else "Professor"

  
        self.dialog = self.ft.AlertDialog(
            title=self.ft.Text(titulo),
            content=self.ft.Container(
                width=400, height=350,
                content=self.ft.Column([
                    self.input_nome, 
                    self.input_cpf, 
                    self.input_user, 
                    self.input_senha, 
                    self.dropdown_cargo
                ], scroll=self.ft.ScrollMode.AUTO)
            ),
            actions=[
                self.ft.TextButton("Cancelar", on_click=self.fechar_modal),
                # Botão SALVAR chama a função salvar(e)
                self.ft.ElevatedButton("Salvar", on_click=lambda e: self.salvar(e), bgcolor="blue", color="white")
            ],
            actions_alignment=self.ft.MainAxisAlignment.END
        )
        
        e.control.page.dialog = self.dialog
        self.dialog.open = True
        e.control.page.update()

    def fechar_modal(self, e):
        self.dialog.open = False
        e.control.page.update()

    def salvar(self, e):
       
        dados = (
            self.input_nome.value, 
            self.input_cpf.value, 
            self.input_user.value, 
            self.dropdown_cargo.value, 
            self.input_senha.value
        )

        if self.id_em_edicao:
            ok, msg = self.db.atualizar_usuario(self.id_em_edicao, *dados)
        else:
            ok, msg = self.db.adicionar_usuario(*dados)

     
        if ok:
            self.fechar_modal(e)    
            self.renderizar_lista() 
            self.notificar(e.control.page, msg, "green") 
        else:
        
            self.notificar(e.control.page, msg, "red")

    def deletar(self, e, uid):
        ok, msg = self.db.remover_usuario(uid)
        if ok:
            self.renderizar_lista()
            self.notificar(e.control.page, msg, "grey")

    def notificar(self, page, texto, cor):
        if page:
            page.snack_bar = self.ft.SnackBar(self.ft.Text(texto), bgcolor=cor)
            page.snack_bar.open = True
            page.update()



class DadosItensTab:
    def __init__(self, ft, controller_main):
        self.ft = ft
        self.db = controller_main.database 

    def build(self):
        return self.ft.Container(
            expand=True, bgcolor="#f4f7f6", padding=20,
            content=self.ft.Column([
                self.ft.Text("Dados Auxiliares", size=22, weight="bold"),
                self.ft.Divider(),
                self._secao("Categorias", "categorias"),
                self._secao("Tipos de Item", "tipos"),
                self._secao("Locais", "locais"),
            ], scroll=self.ft.ScrollMode.AUTO, expand=True)
        )

    def _secao(self, titulo, chave):
        input_novo = self.ft.TextField(label=f"Novo {titulo}", expand=True, height=40, bgcolor="white")
        coluna = self.ft.Column()

        def render():
            coluna.controls.clear()
            for item in self.db.get_auxiliar(chave):
                coluna.controls.append(
                    self.ft.Container(
                        padding=10, bgcolor="white", border_radius=6, margin=2,
                        content=self.ft.Row([
                            self.ft.Text(item),
                            self.ft.IconButton(self.ft.Icons.DELETE, icon_color="red", 
                                          on_click=lambda e, i=item: remover(e, i))
                        ], alignment=self.ft.MainAxisAlignment.SPACE_BETWEEN)
                    )
                )
            try: 
                if coluna.page: coluna.update()
            except: pass

        def add(e):
            if input_novo.value:
                if self.db.add_auxiliar(chave, input_novo.value):
                    input_novo.value = ""
                    input_novo.update()
                    render()

        def remover(e, val):
            if self.db.remove_auxiliar(chave, val):
                render()

        render() 

        return self.ft.ExpansionTile(
            title=self.ft.Text(titulo, weight="bold"),
            leading=self.ft.Icon(self.ft.Icons.LIST, color="blue"),
            controls=[
                self.ft.Container(
                    padding=10,
                    content=self.ft.Column([
                        self.ft.Row([
                            input_novo, 
                            self.ft.IconButton(self.ft.Icons.ADD_CIRCLE, icon_color="green", on_click=add)
                        ]),
                        coluna
                    ])
                )
            ]
        )



class ConfiguracoesView:
    def __init__(self, ft, anim1, anim2, controller):
        self.ft = ft
        self.controller = controller
        
        self.tab_usuarios = UsuariosTab(ft, self.controller, anim1)
        self.tab_dados = DadosItensTab(ft, self.controller)

      
        self.page = self.build()

    def build(self):
        return self.ft.Tabs(
            selected_index=0, 
            expand=True,
            tabs=[
                self.ft.Tab(text="Usuários", icon=self.ft.Icons.PEOPLE, content=self.tab_usuarios.build()),
                self.ft.Tab(text="Dados Auxiliares", icon=self.ft.Icons.LIST, content=self.tab_dados.build())
            ]
        )