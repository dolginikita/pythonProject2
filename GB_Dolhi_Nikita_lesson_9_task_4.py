class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f'{self.color} {self.name} поехал')

    def stop(self):
        print(f'{self.color} {self.name} остановился')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} повернул на {self.direction} градусов')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed} км/ч') if self.speed <= 60 else \
            print(f'Скорость для {self.name} превышена')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed} км/ч')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed} км/ч') if self.speed <= 40 else \
            print(f'Скорость для {self.name} превышена')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


c, t, s, w, p = Car(80, 'Blue', 'BMW'), TownCar(60, 'White', 'Citroen'), SportCar(180, 'Red', 'Ferrari'), \
                WorkCar(50, 'Grey', 'Ford'), PoliceCar(130, 'White/Blue', 'Dodge')

car = p

car.go(), car.turn('90'), car.show_speed(), car.stop()
print(f'Марка: {car.name}, Цвет: {car.color}, Скорость: {car.speed} км/ч, Полицейская: {car.is_police}')