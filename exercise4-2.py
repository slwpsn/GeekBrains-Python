# К сожалению, не понял, как создать нужный генератор. Посмотрю в лекции.

my_list = list(input('Введите элементы списка через пробел: ').split())
new_list = []
check = float('inf')

for el in my_list:
    if int(el) > check:
        new_list.append(el)
    check = int(el)

print(new_list)
