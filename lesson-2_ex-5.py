my_list = []

number = input('Введите число. Чтобы закончить, наберите любые буквенные символы: ')

while True:
    try:
       my_list.append(int(number))
       number = input('Введите новое число, мы добавим его в список: ')
    except ValueError:
        break


print(sorted(my_list, reverse=True))
