def my_func(x, y):
    exponent = -y
    denominator = x
    for i in range(exponent - 1):
        denominator = denominator * x
    return 1 / denominator

def my_func1(x, y):
    exponent = -y
    denominator = x
    if exponent == 2:
        for i in range(x - 1):
            denominator += x
    elif exponent > 2:
        for i in range(x - 1):
            denominator += x
            den_part = denominator
        for i in range(exponent - 1):
            denominator += den_part
    return 1 / denominator

while True:
    a = int(input('Введите положительное число, которое будем возводить в степень: '))
    if a <= 0:
        print('Положительное!')
    else:
        break
while True:
    b = int(input('Введите отрицательное число, в такую степень возведём число: '))
    if b >= 0:
        print('Отрицательное!')
    else:
        break

print(my_func(a, b))
print(my_func1(a, b))
