import flet as ft

class AnimacoesBotao(ft.ElevatedButton):

    def __init__(self, texto="Botão"):
        super().__init__(
            text=texto,
            animate_scale=300,
            scale=1,
            on_hover=self.hover_animacao
        )

    def hover_animacao(self, e):
        if e.data == "true":
            self.scale = 1.10
        else:
            self.scale = 1
        self.update()


