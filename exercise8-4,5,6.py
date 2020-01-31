class Storage:
    def __init__(self, name, price, quantity, type, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.type = type

    def __dict__(self):
        return {name: [price, quantity, type]}

    def redirect(self):
        if self.type == 'p':
            return 'p'

        elif self.type == 's':
            return 's'

        elif self.type == 'x':
            return 'x'

class OfficeEquipment(Storage):
    def __init__(self, name, price, quantity, type, *args):
        super().__init__(name, price, quantity, type)

class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, type, dpi, type_of_p):
        super().__init__(name, price, quantity, type)
        self.dpi = dpi
        self.type_of_p = type_of_p

class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, type, dpi, color):
        super().__init__(name, price, quantity, type)
        self.dpi = dpi
        self.color = color

class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, type, dpi, bw_or_color):
        super().__init__(name, price, quantity, type)
        self.dpi = dpi
        self.bw_or_color = bw_or_color

y_or_n = None
dict_storage = {}

while y_or_n != 'q':
    name = input('Введите название товара: ')
    while True:
        price = input('Сколько стоит товар: ')
        if price.isdigit():
            price = int(price)
            break
        else:
            print('Введите число в качестве цены!')
            continue
    while True:
        quantity = input('Сколько единиц товара на складе: ')
        if quantity.isdigit():
            quantity = int(quantity)
            break
        else:
            print('Введите число!')
            continue
    type = input('Введите тип товара. Если принтер, наберите p, если сканер — s, если ксерокс — x: ')
    while True:
        dpi = input('Введите DPI: ')
        if dpi.isdigit():
            dpi = int(dpi)
            break
        else:
            print('Введите число!')
            continue
    if type == 'p':
        type_of_p = input('Если принтер матричный, введите m, если струйный — s, если лазерный — l: ')
    elif type == 's':
        color = input('Какой цвет сканера: ')
    elif type == 'x':
        bw_or_color = input('Если ксерокс чёрно-белый, введите bw, если цветной — clr: ')

    item = Storage(name, price, quantity, type)
    dict_storage.update(item.__dict__())
    if item.redirect() == 'p':
        item = Printer(name, price, quantity, type, dpi, type_of_p)
    elif item.redirect() == 's':
        item = Scanner(name, price, quantity, type, dpi, color)
    elif item.redirect() == 'x':
        item = Xerox(name, price, quantity, type, dpi, bw_or_color)

    y_or_n = input('Если товары закончились, нажмите q. Если хотите продолжить, любые символы: ')

print(dict_storage)
