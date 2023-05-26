class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if isinstance(other, Cell) and self.quantity - other.quantity > 0:
            return self.quantity - other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(24)
cell_2 = Cell(2)

print('Сложение: ', cell + cell_2)
print('Вычитание: ', cell - cell_2)
print('Деление: ', cell / cell_2)
print('Умножение: ', cell * cell_2)
print(cell.make_order(10))
