
class Warehouse:
    def __init__(self):
        self.my_warehouse = []
        self.my_list = {}

    # @classmethod
    def logistic(self):
        count = None
        department = None
        while True:
            try:
                choice = input(f'{"*" * 70}\n'
                               f'Введите порядковый номер устройства или введи "Q" что бы закончить наполнение склада:'
                               f'\n1 : {p}'
                               f'\n2 : {s}'
                               f'\n3 : {x}'
                               f'\n------>: ')
                if choice.lower() != 'q':
                    if choice.isdigit() and 0 < int(choice) <= 3:
                        count = input(f'{"*" * 70}\n'
                                      f'Введите кол-во товара шт.:'
                                      f'\n------>: ')
                        if count.isdigit():
                            department = input(f'{"*" * 70}\nВведите в какой департамент отправляем:\n------>: ')
                        else:
                            print(f'{"*" * 70}\nКоличество необходимо ввести целым числом!\n{"*" * 70}\n')
                            return Warehouse.logistic(ware)
                    else:
                        print(f'{"*" * 70}\nВы ввели неверное значение!\n{"*" * 70}\n')
                        return Warehouse.logistic(ware)
                if choice == '1':
                    uniqe = {'Устройство': p.__str__(), 'Кол-во': count, 'Департамент': department}
                    self.my_list = uniqe
                    self.my_warehouse.append(self.my_list)
                    print(f'{"*" * 70}\nНа складе для передачи:\n {self.my_warehouse}\n{"*" * 70}\n')
                elif choice == '2':
                    uniqe = {'Устройство': s.__str__(), 'Кол-во': count, 'Департамент': department}
                    self.my_list = uniqe
                    self.my_warehouse.append(self.my_list)
                    print(f'{"*" * 70}\nНа складе для передачи:\n {self.my_warehouse}\n{"*" * 70}\n')
                elif choice == '3':
                    uniqe = {'Устройство': x.__str__(), 'Кол-во': count, 'Департамент': department}
                    self.my_list = uniqe
                    self.my_warehouse.append(self.my_list)
                    print(f'{"*" * 70}\nНа складе для передачи:\n {self.my_warehouse}\n{"*" * 70}\n')
                elif choice.lower() == 'q':
                    print(f'{"*" * 70}\nПополнение склада закончено\n{"*" * 70}\n')
                    break
                else:
                    raise OwnError(f'{"*" * 70}\nВведено неверное значение!\n{"*" * 70}\n')
            except OwnError as err:
                print(err)
        return f'{"*" * 70}\nНа складе хранится: {self.my_warehouse}\n{"*" * 70}\n'


class OwnError(ValueError):
    def __init__(self, val):
        self.val = val


class OffEquip:
    def __init__(self, color, can_print, scan, copy):
        self.color = color
        self.can_print = can_print
        self.scan = scan
        self.copy = copy

    def __str__(self):
        return f'Оргтехника - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


class Printer(OffEquip):
    def __str__(self):
        return f'Принтер - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


class Scaner(OffEquip):
    def __str__(self):
        return f'Сканер - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


class Xerox(OffEquip):
    def __str__(self):
        return f'Ксерокс - Цвет: {self.color}, Печатает: {self.can_print}, ' \
               f'Сканирует: {self.scan}, Копирует: {self.copy}'


o = OffEquip('Белый', 'Да', 'Да', 'Да')
p = Printer('Белый', 'Да', 'Нет', 'Нет')
s = Scaner('Белый', 'Нет', 'Да', 'Нет')
x = Xerox('Белый', 'Да', 'Да', 'Да')
print(o)
print(p)
print(s)
print(x)
ware = Warehouse()
print(Warehouse.logistic(ware))