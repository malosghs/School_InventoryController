class MainModel:
    def __init__(self,database,categoria_model,item_model,emprestimo_model):
        self.database = database
        self.categoria_model = categoria_model
        self.item_model = item_model
        self.emprestimo_model = emprestimo_model
        