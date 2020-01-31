class NotANumber:
    def __init__(self, user_list):
        self.user_list = user_list
        self.user_list2 = []

    def digitcheck(self):
        for i in range(len(self.user_list)):
            if self.user_list[i].isdigit() == True:
                self.user_list2.append(self.user_list[i])
        return self.user_list2

user_list = []
userdata = None
while userdata != 'q':
    userdata = input('Введите число, которое станет элементом списка (не числа вводить нельзя). Для выхода нажмите q: ')
    user_list.append(userdata)

user_list2 = NotANumber(user_list)
print(*user_list2.digitcheck(), sep=', ')
