storage = []        #список кортежей
titles = []         #список с названиями
prices = []         #список с ценами
quantities = []     #список с количеством товара
units = []          #список с единицами измерения
i = 1

while True:
    title = input('Когда ваши товары закончатся, наберите "end". Введите название товара: ')
    if title == 'end':
        break
    price = int(input('Сколько он стоит? Введите число: '))
    quantity = int(input('Сколько его у вас? введите число: '))
    unit = input('А в чём измеряется? Введите, например, "шт.": ')
    good = (i, {'название': title, 'цена': price, 'количество': quantity, 'eд.': unit})
    storage.append(good)
    titles.append(title)
    prices.append(price)
    quantities.append(quantity)
    units.append(unit)
    i += 1

for i in range(len(storage)): #структура данных по строчке (подзадача №1)
    print(storage[i])

storage_dict = {'название': titles, 'цена': prices, 'количество': quantities, 'ед.': units}

for key, value in storage_dict.items(): #аналитика данных (подзадача №2)
    print(f'{key}: {value}')

