my_list = []
my_list2 = []

with open ('text2.txt') as f:
    for line in f:
        my_list.append(line)
        my_list2.append(len(line.split()))

print('Количество строк:', len(my_list))

for i in range(len(my_list2)):
    print(f'Количество символов в строке №{i+1}: {my_list2[i]}')



