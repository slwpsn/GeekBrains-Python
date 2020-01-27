class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells == other.cells:
            return 'Количество ячеек в клетках одинаково. Получается пустая клетка'
        else:
            return abs(self.cells - other.cells)

    def __mul__(self, other):
        if self.cells == 0 or other.cells == 0:
            return 'Одна из клеток была пуста. Общая клетка тоже получилась пустой'
        else:
            return self.cells * other.cells

    def __truediv__(self, other):
        if other.cells == 0:
            return 'Количество ячеек у заданной в качестве делителя клетки равно нулю. Деление невозможно'
        else:
            return self.cells // other.cells

    def make_order(self, cells_in_row):
        self.cells_in_row = cells_in_row
        self.rows = self.cells // self.cells_in_row
        self.residue = self.cells % self.cells_in_row
        if self.cells_in_row <= self.cells:
            print(*('*' * self.cells_in_row, '\n') * self.rows, '*' * self.residue,sep='', end='')
        elif self.cells_in_row > self.cells:
            print('*' * self.cells)

a = Cell(0)
b = Cell(8)
c = Cell(5)
d = Cell(8)

print(b+c)
print(c-b)
print(d*c)
print(a/b)
print(b/a)
print(b-d)
print(d*a)

b.make_order(3)
c.make_order(6)
