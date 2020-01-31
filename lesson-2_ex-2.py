user_list = input('Введите элементы списка через пробел и нажмите Enter: ').split()

if len(user_list) == 1:
    print(user_list)

else:
    i = 0
    while len(user_list) != 1:
        if i + 1 == len(user_list):
            break
        user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
        if i + 2 == len(user_list):
            break
        i += 2
    print(user_list)


