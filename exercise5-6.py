my_list = []
my_digits = []
my_digits2 = []
my_subjects = []
my_subjects2 = []
my_dict = {}

with open('text6.txt') as f:
    for line in f:
        my_list.append(line)

for i in range(len(my_list)):
    my_subjects.append(my_list[i].split(':'))
    my_subjects2.append(my_subjects[i][0])

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if my_list[i][j].isdigit():
            if my_list[i][j-2].isdigit() and my_list[i][j-1].isdigit() and my_list[i][j-1].isdigit():
                my_digits.append(my_list[i][j-2] + my_list[i][j-1] + my_list[i][j])
            elif my_list[i][j-2].isdigit() == False and my_list[i][j-1].isdigit() and my_list[i][j-1].isdigit() and my_list[i][j+1].isdigit() == False:
                my_digits.append(my_list[i][j-1] + my_list[i][j])
            elif my_list[i][j].isdigit() and my_list[i][j-1].isdigit() == False and my_list[i][j+1].isdigit() == False:
                my_digits.append(my_list[i][j])
        elif my_list[i][j] == '—':
            my_digits.append('—')

c = 0
while c + 3 <= len(my_digits):
    if my_digits[c].isdigit() == False and my_digits[c+1].isdigit() and my_digits[c+2].isdigit():
        my_digits2.append(int(my_digits[c+1]) + int(my_digits[c+2]))
    elif my_digits[c+1].isdigit() == False and my_digits[c].isdigit() and my_digits[c+2].isdigit():
        my_digits2.append(int(my_digits[c]) + int(my_digits[c+2]))
    elif my_digits[c+2].isdigit() == False and my_digits[c].isdigit() and my_digits[c+1].isdigit():
        my_digits2.append(int(my_digits[c]) + int(my_digits[c+1]))
    elif my_digits[c].isdigit() == False and my_digits[c+1].isdigit() == False and my_digits[c+2].isdigit():
        my_digits2.append(int(my_digits[c+2]))
    elif my_digits[c].isdigit() == False and my_digits[c+1].isdigit() and my_digits[c+2].isdigit() == False:
        my_digits2.append(int(my_digits[c+1]))
    elif my_digits[c].isdigit() and my_digits[c+1].isdigit() == False and my_digits[c+2].isdigit() == False:
        my_digits2.append(int(my_digits[c]))
    elif my_digits[c].isdigit() == False and my_digits[c+1].isdigit() == False and my_digits[c+2].isdigit() == False:
        my_digits2.append(0)
    else:
        my_digits2.append(int(my_digits[c]) + int(my_digits[c+1]) + int(my_digits[c+2]))
    c += 3

for i in range(len(my_digits2)):
    my_dict[my_subjects2[i]] = int(my_digits2[i])
print(my_dict)
