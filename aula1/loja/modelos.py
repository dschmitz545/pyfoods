class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    
    publico = 0
    _protegido = 1
    __privado = 2
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria