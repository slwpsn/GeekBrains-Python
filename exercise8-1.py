class Data:

    def __init__(self, param):
        self.datalist = param.split('-')
        self.day = self.datalist[0]
        self.month = self.datalist[1]
        self.year = self.datalist[2]

    @classmethod
    def strtonum(cls, param):
        cls.datalist = param.split('-')
        cls.day = int(cls.datalist[0])
        cls.month = int(cls.datalist[1])
        cls.year = int(cls.datalist[2])
        return cls.day, cls.month, cls.year

    @staticmethod
    def valid(param):
        datalist = param.split('-')
        if int(datalist[0]) > 31:
            return 'Неправильное число'
        elif int(datalist[0]) > 30 and int(datalist[1]) == 4 or int(datalist[1]) == 6 or int(datalist[1]) == 9 or int(datalist[1]) == 11:
            return 'Неправильное число'
        elif int(datalist[2]) % 4 != 0 or int(datalist[2]) % 100 == 0 and int(datalist[2]) % 400 != 0 and int(datalist[0]) > 28:
            return 'Неправильное число'
        elif int(datalist[1]) == 2 and int(datalist[0]) > 29:
            return 'Неправильное число'
        elif int(datalist[1]) < 1 or int(datalist[1] > 12):
            return 'Неправильный месяц'

userdata = input('Введите дату в формате ДД-ММ-ГГГГ: ')
print(*Data.strtonum(userdata))
a = Data(userdata)
print()
print(a.valid(userdata))

