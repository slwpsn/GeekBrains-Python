from sys import argv

script_name, hours, rate, premium = argv

print(f'Заработная плата сотрудника: {(int(hours) * int(rate)) + int(premium)} рублей.')
