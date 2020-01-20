from itertools import count
from itertools import cycle
import time

start_number = int(input('Укажите число, мы продолжим отсчёт до бесконечности: '))

for el in count(start_number):
    print(el)

print('Готовим второй скрипт...')
time.sleep(2)

user_list = list(input('Введите элементы списка через пробел, мы бесконечно повторим и их: ').split())

for el in cycle(user_list):
    print(el)
