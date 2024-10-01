class Artigo():
    def __init__(self, id, titulo, texto):
        self.id = id
        self.titulo = titulo
        self.texto = texto
    

    def get_id(self):
        return self.id
    

    def get_titulo(self):
        return self.titulo
    

    def get_texto(self):
        return self.texto
