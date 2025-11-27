import Flet as ft 
# View imports 

from views.main_window import MainPageView
from views.modelos_animacao.botao_animacao import AnimacoesBotao
from views.modelos_animacao.page_animacao import AnimacoesPage

# Controller imports 

from controllers.app_controller import ControllerMain

# Model imports 
from models.main_model import MainModel
from models.categoria_model import CategoriaModel
from models.database import Database
from models.emprestimo_model import EmprestimoModel
from models.item_model import ItemModel




def main(page: ft.Page):
    controller = ControllerMain()
    view = MainPageView(page,AnimacoesPage(),AnimacoesBotao(),controller)
    models = MainModel(Database,CategoriaModel,ItemModel,EmprestimoModel)

    controller.view = view 
    controller.models = models

    controller.construir_page() # Imprementar funcao 
    
    

if __name__ == "__main__":
    ft.app(target=main)
