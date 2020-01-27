my_list = (input('Введите числа через пробел: ')).split()

with open('text5.txt', 'w+') as f:
    for el in my_list:
        f.write(el)
        f.write(' ')
    for line in f:
        my_list.append(line.split())

sum = int(my_list[0])
for i in range(1, len(my_list)):
    sum += int(my_list[i])

print(sum)



