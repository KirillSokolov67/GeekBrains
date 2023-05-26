from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        return round(self.v / 6.5 + 0.5, 1)

    @property
    def costume(self):
        return round(2 * self.h + 0.3, 1)


clothes = Clothes(111, 55)

print(f'Для пошива пальто нужно: {clothes.coat()} метров ткани')
print(f'Для пошива костюма нужно: {clothes.costume} метров ткани')
print(f'Общий подсчет расхода ткани: {clothes.coat() + clothes.costume} метров ткани')
