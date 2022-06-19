class Worker:
    def __init__(self, name, surname, position, wage, bonus, months):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
        self.months = months


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname} работает в должности {self.position}')

    def get_total_income(self):
        print(f'Общая прибыль сотрудника за {self.months} месяц(ев) составила:\
 {sum(self._income.values()) * self.months} долларов {self._income}')


worker = Position('Петр', 'Петров', 'Programmer', 1200, 3000, 2)

worker.get_full_name()
worker.get_total_income()
print(worker.name)
print(worker.position)