class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        income_number = self._income.get('wage') + self._income.get('bonus')
        print(f'Доход с учётом премии: {income_number}')

name = input('Введите имя сотрудника: ')
surname = input('Введите фамилию сотрудника: ')
position = input('Введите должность сотрудника: ')
wage = int(input('Введите оклад сотрудника: '))
bonus = int(input('Введите размер премии: '))
income = {'wage': wage, 'bonus': bonus}

a = Position(name, surname, position, income)
a.get_full_name()
a.get_total_income()
