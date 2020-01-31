def userinfo(*args):
    return args

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthyear = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите адрес электронной почты: ')
phone = input('Введите номер телефона: ')

print(*userinfo(name, ' ', surname, ' родился в ', birthyear, ' году, город проживания — ', city,
                ', связаться можно по электронной почте ',
                email, ' или по телефону ', phone), sep='')
