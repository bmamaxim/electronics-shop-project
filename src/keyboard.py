from src.item import Item


class Language:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard(Item, Language):
        def __init__(self, name: str, price: float, quantity: int):
            super().__init__(name, price, quantity)
            Language.__init__(self)

