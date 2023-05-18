from time import sleep


class Trafficlight:
    def __init__(self, color):
        self._color = color

    def running(self):
        for i, value in self._color.items():
            sleep(value)
            print(i)


Trafficlight = Trafficlight(color={"Красный": 7, "Желтый": 2, "Зеленый": 7})

Trafficlight.running()