class ObrasDeArte:
    def __init__(self, id, titulo, data, descricao, foto):
        self.id = id
        self.titulo = titulo
        self.data = data
        self.descricao = descricao
        self.foto = foto
    

    def get_id(self):
        return self.id


    def get_titulo(self):
        return self.titulo
    

    def get_data(self):
        return self.data
    

    def get_descricao(self):
        return self.descricao
    

    def get_foto(self):
        return self.foto