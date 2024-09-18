class Conferencia:
    def __init__(self, id, title, theme, date, details):
        self.__id = id
        self.__title = title
        self.__theme = theme
        self.__date = date
        self.__details = details
    
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_theme(self):
        return self.__theme

    def get_date(self):
        return self.__date
    
    def get_details(self):
        return self.__details