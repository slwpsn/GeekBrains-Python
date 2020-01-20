sum = 0
a = 0

while a == 0:
    numbers = list(input('Введите числа через пробел. Чтобы закончить введите q: ').split())

    for i in range(len(numbers)):
        if numbers[i] == 'q':
            a = 1
            break
        sum += int(numbers[i])
    print(sum)
