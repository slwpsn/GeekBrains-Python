a = 'none'
my_list = []
while a != '':
    a = input('Введите строки по порядку. Чтобы закончить, введите пустую строку: ')
    my_list.append(a)
    my_list.append('\n')
my_list.pop(-1)
my_list.pop(-1)

f = open('text1.txt', 'w')
f.writelines(my_list)
f.close()
