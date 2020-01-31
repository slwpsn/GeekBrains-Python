class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list
        self.matrixx = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __str__(self):
        return f'матрица:\n{self.my_list[0]}\n{self.my_list[1]}\n{self.my_list[2]}'

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                self.matrixx[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return f'Сумма двух матриц:\n{self.matrixx[0]}\n{self.matrixx[1]}\n{self.matrixx[2]}'

my_list_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_list_2 = Matrix([[18, 5, 3], [2, 7, 12], [5, 3, 7]])

print(f'Первая {my_list_1}')
print()
print(f'Вторая {my_list_2}')
print()
print(my_list_1 + my_list_2)
