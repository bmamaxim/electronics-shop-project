from src.item import Item


class Phone(Item):
    """
    Phone: содержит все атрибуты класса `Item` и дополнительно атрибут,
     содержащий количество поддерживаемых сим-карт
    """
    def __init__(self, name: str,
                 price: float,
                 quantity: int,
                 number_of_sim: int
                 ):
        super().__init__(name, price, quantity)
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError(
                "Количество физических SIM-карт должно быть целым числом больше нуля."
            )
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить Phone` или `Item` с экземплярами не `Phone` или `Item` классов")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

