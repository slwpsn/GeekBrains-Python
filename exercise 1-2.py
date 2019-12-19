seconds = int(input('Приветики! Введите время в секундах '))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds2 = seconds - (minutes * 60 + hours * 3600)

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds2 < 10:
    seconds2 = '0' + str(seconds2)

print(f'Это {hours}:{minutes}:{seconds2}. Спасибо')
