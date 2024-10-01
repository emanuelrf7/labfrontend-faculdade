class Conferencia():
    def __init__(self, id, tema, titulo, descricao, palestrante):
        self.id = id
        self.tema = tema
        self.titulo = titulo
        self.descricao = descricao
        self.palestrante = palestrante
    

    def get_id(self):
        return self.id
    

    def get_tema(self):
        return self.tema
    

    def get_titulo(self):
        return self.titulo
    

    def get_descricao(self):
        return self.descricao
    

    def get_palestrante(self):
        return self.palestrante
