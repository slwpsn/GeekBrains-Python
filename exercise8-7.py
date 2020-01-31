class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        add_str = str(f'{self.number} {other.number}')
        self.add_list = add_str.split()
        for i in range(len(self.add_list)):
            try:
                if self.add_list[i] == '-':
                    self.add_list[i+1] = self.add_list[i] + self.add_list[i+1]
            except:
                continue
        i = 0
        while i < len(self.add_list):
            if self.add_list[i] == '-':
                del self.add_list[i]
            elif self.add_list[i] == '+':
                del self.add_list[i]
            else:
                i += 1
        sum_int = 0
        self.list_i = []
        i = 0
        for i in range(len(self.add_list)):
            try:
                self.add_list[i] = int(self.add_list[i])
                sum_int += int(self.add_list[i])
            except:
                self.list_i.append(self.add_list[i])
                continue
        i = 0
        list_i2 = []
        for i in range(len(self.list_i)):
            list_i2.append(self.list_i[i].replace('i', ''))
        i = 0
        sum_i = 0
        for i in range(len(list_i2)):
            sum_i += int(list_i2[i])
        if sum_i < 0:
            return f'{sum_int} - {abs(sum_i)}i'
        elif sum_i > 0:
            return f'{sum_int} + {sum_i}i'

    def __mul__(self, other):
# К сожалению, не успел

a = ComplexNumber('-1 + 6i')
b = ComplexNumber('3 - 1i')
c = ComplexNumber('-50 - 12i')
d = ComplexNumber('5 + 5i')
print(a + b)
print(a + c)
print(a + d)

