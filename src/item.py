# Class
import csv


class InstantiateCSVError(Exception):
    """
    Исключение при повреждении файла
    """

    def __init__(self):
        self.message = 'Файл items.csv поврежден'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_set):
        if len(name_set) >= 10:
            raise ValueError('Более чем 10 символов в имени')
        else:
            self.__name = name_set

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return int(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = int(self.price * self.pay_rate)

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Проверка наличия и целостности файла
        """
        if Item.instantiate_from_csv_test(path) is True:
            Item.all = []
            with open(path, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                for line in csv_data:
                    cls(line['name'], float(line['price']), int(line['quantity']))

    @staticmethod
    def instantiate_from_csv_test(path):
        """
        Проверка наличия и целостности файла
        """
        try:
            with open(path, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                csv_data_list = list(csv_data)
                for line in csv_data_list:
                    if (line.get('name') and line.get('price') and line.get('quantity')) in ['', None]:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print('Отсутствует файл items.csv')
            return 'Отсутствует файл items.csv'
        except InstantiateCSVError as exep:
            print(exep.message)
            return exep.message
        else:
            return True
