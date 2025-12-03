
import flet as ft
import psycopg2

# View imports
 
from views.main_window import MainPageView

from views.modelos_animacao.botao_animacao import AnimacoesBotao
from views.modelos_animacao.page_animacao import AnimacoesPage

from views.pages.cadastro_item_view import CadastroItemView
from views.pages.configuracoes_view import ConfiguracoesView
from views.pages.devolucao_view import DevolucaoView
from views.pages.emprestimo_view import EmprestimoView
from views.pages.home_view import HomeView
from views.pages.login_view import LoginView
from views.pages.main_view import MainView

 
# Controller imports
 
from controllers.app_controller import ControllerMain
 
# Model imports
from models.main_model import MainModel
from models.categoria_model import CategoriaModel
from models.database import Database
from models.config_database import CONFIG_DB_SCHOOL
from models.acao_model import AcaoPageItem
from models.item_model import ItemModel

def main(page: ft.Page):
    controller = ControllerMain()

    view = MainPageView(page,AnimacoesPage,AnimacoesBotao,controller,MainView(CadastroItemView,CadastroItemView,DevolucaoView,emprestimoView,HomeView,LoginView))
    models = MainModel(Database(psycopg2,CONFIG_DB_SCHOOL),CategoriaModel,ItemModel,AcaoPageItem)


    controller.view = view 
    controller.models = models

    controller.construir_page() 



if __name__ == "__main__":
    ft.app(target=main)
