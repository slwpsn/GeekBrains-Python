revenue = int(input('Какая у вас выручка? '))
costs = int(input('А сколько тратите? '))

if revenue > costs:
    employees = int(input(f'Здорово, но не расслабляйтесь. Вы зарабатываете на {revenue - costs} больше, чем тратите, '
          f'а рентабельность вашей выручки составляет {((revenue - costs) / revenue):.2f}! А сотрудников у вас сколько? '))
    print(f'Прибыль на каждого вашего сотрудника — {((revenue - costs) / employees):.2f}!')

if revenue < costs:
    print(f'Срочно что-нибудь придумайте! Вы зарабатываете на {costs - revenue} меньше, чем тратите, это просто ужасно!')


