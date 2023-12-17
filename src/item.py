import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self,
                 name: str,
                 price: float,
                 quantity: int
                 ) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        pass

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.pay_rate

    @property
    def name(self, ):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, data):
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        cls.all.clear()
        with open(data, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_data = cls(row['name'], row['price'], row['quantity'])
                cls.all.append(new_data)

    @staticmethod
    def string_to_number(x):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(x))
