class Cell:
    def __init__(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            raise ValueError

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell(self.number - other.number) if self.number - other.number >= 0 \
            else f'Клетка не может быть меньше нуля'

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, n):
        for _ in range(self.number // n):
            print('*' * n)
        print('*' * (self.number % n))


"""Обьявление объектов (клеток)"""
a = Cell(10)
b = Cell(13)
c = Cell(8)

"""Работа операторов перегрузки"""
print((a + b).number)
print(a - b)
print((a - c).number)
print((a * b).number)
print((a / c).number)
print((a // c).number)

"""Работа метода make_order"""
a.make_order(3)