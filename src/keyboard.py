from src.item import Item

class Mixin_lang:
    """
     классе-миксин c дополнительным функционалом
     по хранению и изменению раскладки клавиатуры ,
     который “подмешивается” в цепочку наследования класса `Keyboard`.
    """
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language


    def change_lang(self):
        """
        метод для изменения языка (раскладки клавиатуры)
        """
        if self.language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, Mixin_lang):
    """
    Класс товара "клавиатура" с теми же атрибутами что и класс Item
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        Mixin_lang.__init__(self)
