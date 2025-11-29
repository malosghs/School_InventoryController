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
from models.config_database import CONFIG_DB_SCHOOL
from models.emprestimo_model import EmprestimoModel
from models.item_model import ItemModel
 



def main(page: ft.Page):
    controller = ControllerMain()
    view = MainPageView(page,AnimacoesPage(),AnimacoesBotao(),controller)
    models = MainModel(Database(CONFIG_DB_SCHOOL),CategoriaModel,ItemModel,EmprestimoModel)

 # Instância da VIEW sem controller
    view = MainPageView(
        page,
        AnimacoesPage(),
        AnimacoesBotao(),
        controller=None   # <-- REMOVIDO
    )

    # Models (tu podes ou não precisar disto agora)
    models = MainModel(Database, CategoriaModel, ItemModel, EmprestimoModel)

    # Constrói a página principal diretamente
    layout = view.construir_main_page()

    # Renderiza conteúdo
    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)
