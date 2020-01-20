list1 = []
list2 = []
sum = 0

with open('text3.txt') as f:
    for line in f:
        list1.append(line.split())

for i in range(len(list1)):
    sum += int(list1[i][1])
    if int(list1[i][1]) < 20000:
        list2.append(list1[i][0])

print('Вот кто получает меньше 20 тысяч рублей: ', end='')
print(*list2)
print(f'А вот средняя зарплата сотрудников: {sum // len(list1)} руб.')


