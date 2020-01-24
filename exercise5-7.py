import json
my_list = []
my_dict = {}
my_dict2 = {}
sum = 0
profitfirms = 0

with open('text7.txt') as f:
    for line in f:
        my_list.append(line.split())

for i in range(len(my_list)):
    my_dict[my_list[i][0]] = int(my_list[i][2]) - int(my_list[i][3])
    if int(my_list[i][2]) > int(my_list[i][3]):
        profitfirms += 1
        sum += int(my_list[i][2]) - int(my_list[i][3])

my_dict2['average_profit'] = sum // profitfirms

my_list2 = [my_dict, my_dict2]

with open("my_file.json", "w") as write_f:
    json.dump(my_list2, write_f)
