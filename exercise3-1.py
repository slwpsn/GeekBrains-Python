def division(number1, number2):
    return number1 / number2

while True:
    a = int(input('Введите первое число (делимое): '))
    b = int(input('Введите второе число (делитель): '))
    if b == 0:
        print('Делить на ноль нельзя!')
    else:
        print(division(a, b))
        break
