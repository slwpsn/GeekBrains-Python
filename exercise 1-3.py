number = int(input('Введите-ка какое-нибудь число! Кое-что посчитаем. '))

numbstr = str(number) + str(number)
numbstr2 = str(number) + str(number) + str(number)

sum = number + int(numbstr) + int(numbstr2)

print(f'Поколдовали! Получилось число {sum}')
