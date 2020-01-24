class Stationery:

    def __init__(self, title):
        self.title = title.lower()

    def draw(self):
        print(f'Запуск отрисовки. Пишущий предмет: {self.title}')

class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки. Пишущий предмет: {self.title}')

class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки. Пишущий предмет: {self.title}')

class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки. Пишущий предмет: {self.title}')

a = input('Чем рисуете? Наберите слово карандаш, ручка или маркер, ну или введите название другого пишущего предмета: ')

if a == 'Ручка' or a == 'ручка':
    a = Pen('Ручка')

elif a == 'Карандаш' or a == 'карандаш':
    a = Pencil('Карандаш')

elif a == 'Маркер' or a == 'маркер':
    a = Handle('Маркер')

else:
    a = Stationery(a)

a.draw()
