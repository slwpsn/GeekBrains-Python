def my_func(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num2 + num3
    elif num2 <= 1 and num2 <= num3:
        return num1 + num3
    else:
        return num1 + num2

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(my_func(a, b, c))
