# Пришлось немного подсмотреть решение, потому что не очень понял условие. Вроде разобрался.

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

c = 0
for el in fibo_gen():
    if c >= 15:
        break
    else:
        print(el)
        c += 1

