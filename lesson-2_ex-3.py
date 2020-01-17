month = int(input('Введите номер месяца: '))

while month > 12 or month < 1:
    month = int(input('Номер месяца может быть от 1 до 12, попробуйте ещё: '))

list_winter = [1, 2, 12]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]

if month in list_winter:
    season = 'Холодная зима'
elif month in list_spring:
    season = 'Солнечная весна'
elif month in list_summer:
    season = 'Жаркое лето'
else:
    season = 'Ненастная осень'

months_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь',
               10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

print(f'{month}-й месяц это {months_dict.get(month)}. {season}.')
