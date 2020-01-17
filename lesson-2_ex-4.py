user_str = input('Введите какие-нибудь слова через пробел: ').split()

for i, el in enumerate(user_str, start=1):
    if len(el) > 10:
        el = el[:10]
    print(i, el)
