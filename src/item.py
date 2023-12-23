import csv

class InstantiateCSVError(Exception):
    """
    Класс-исключение если файл `item.csv` поврежден.
    """
    def __init__(self, *args):
        self.message = args

    def __str__(self):
        return f"Ошибка: {self.message}"

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
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, data=""):
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """

        cls.all.clear()
        try:
            with open(data, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if 'name' not in reader or 'price' not in reader or 'quantity' not in reader:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                for row in reader:
                    new_data = cls(row['name'], row['price'], row['quantity'])
                    cls.all.append(new_data)
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError:
            print('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(x):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(x))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            return None

