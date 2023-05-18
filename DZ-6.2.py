class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 0.05

    def all_weight(self):
        all_weight = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(all_weight)} тонн асфальта')


road = Road(5000, 20)
road.all_weight()
