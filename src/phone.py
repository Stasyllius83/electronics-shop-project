from src.item import Item


class Phone(Item):
    def __init__(self, name, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    @property
    def number_of_sim(self):
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim < 1 or not isinstance(new_number_of_sim, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim = new_number_of_sim


