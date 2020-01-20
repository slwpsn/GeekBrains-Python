number = int(input('Введите какое-нибудь длинное целое число, пожалуйста! А мы покажем самую большую цифру из него! '))

digit = number % 10
number = number // 10

while number > 0:
    if number % 10 > digit:
        digit = number % 10
    number = number // 10

print(f'Самая большая цифра — {digit}! Признаюсь, решение этой задачи я подсмотрел в интернете, но я его понял!')


