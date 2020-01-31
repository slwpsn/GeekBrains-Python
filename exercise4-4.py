user_list = list(input('Введите элементы списка через пробел, мы уберём повторы: ').split())

new_list = [el for el in user_list if user_list.count(el) == 1]

print(new_list)
