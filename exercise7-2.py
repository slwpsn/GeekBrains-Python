from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name, X):
        self.name = name
        self.X = X

    @abstractmethod
    def textile(self):
        pass

class Coat(Clothes):

    @property
    def textile(self):
        return self.X / 6.5 + 0.5

class Suit(Clothes):

    @property
    def textile(self):
        return 2 * self.X + 0.3

sum = 0
type_of_clothes = None
while type_of_clothes != 'q':
    type_of_clothes = input('Если пальто, введите "c", если костюм, то "s". Для выхода нажмите "q": ')
    if type_of_clothes == 'c':
        name = input('Введите название пальто: ')
        size = int(input('Введите размер (в числах): '))
        a = Coat(name, size)
        sum += a.textile
        print(f'На {a.name} уйдёт {a.textile:.2f} кв.м. ткани')
    elif type_of_clothes == 's':
        name = input('Введите название костюма: ')
        size = int(input('Введите рост (в числах): '))
        a = Suit(name, size)
        sum += a.textile
        print(f'На {a.name} уйдёт {a.textile:.2f} кв.м. ткани')

print(f'На всю одежду уйдёт {sum:.2f} кв.м. ткани')
