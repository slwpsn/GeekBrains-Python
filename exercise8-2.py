class ZeroDiv:

    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def division(self):
        try:
            return f'Результат деления: {self.dividend / self.divisor}'
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'

division = ZeroDiv(int(input('Введите делимое: ')), int(input('Введите делитель: ')))
print(division.division())
