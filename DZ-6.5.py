class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашем: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером: {self.title}")


pen = Pen('Шариковая ручка')
pen.draw()

pencil = Pencil('Графитовый карандаш')
pencil.draw()

handle = Handle('Ярко-желтый маркер\n')
handle.draw()

print(f"Ученики записывают конспект с помощью: {pen.title}\n")
print(f"Для наброска рисунка художнику необходим: {pencil.title}")
