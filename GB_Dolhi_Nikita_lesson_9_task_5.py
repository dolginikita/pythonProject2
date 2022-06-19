class Stationery:
    title = 'Parent'

    def draw(self):
        print(f'Запуск отрисовки: {self.title}')

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Пишем с помощью: {self.title}')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Обводим с помощью: {self.title}')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Выделяем с помощью: {self.title}')


s, p, pe, h = Stationery(), Pen(), Pencil(), Handle()
s.draw(), p.draw(), pe.draw(), h.draw()
