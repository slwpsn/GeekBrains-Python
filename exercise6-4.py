class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police == True:
            self.is_police = 'полицейская машина'
        elif is_police == False:
            self.is_police = 'не полицейская машина'

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула. Направление: {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        if self.speed < 60:
            print(f'Скорость автомобиля {self.speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч. Норма превышена!')

class WorkCar(Car):

    def show_speed(self):
        if self.speed < 40:
            print(f'Скорость автомобиля {self.speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.speed} км/ч. Норма превышена!')

a = WorkCar(120, 'жёлтый', 'форд', True)
a.go()
print('Это', a.is_police)
print('Внешние признаки:', a.color, a.name)
a.turn('Ессентуки')
a.show_speed()
a.stop()
