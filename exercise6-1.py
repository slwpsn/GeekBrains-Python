import time

class TrafficLight:

    def __init__(self):
        for count in range(3):
            if count == 0:
                self.__color = 'красный'
            elif count == 1:
                self.__color = 'жёлтый'
            else:
                self.__color = 'зелёный'
            self.running(self, count)

    def running(self, color, count):
        if count == 0:
            print(f'Сейчас цвет светофора {self.__color}. Ждите 7 секунд и переходите дорогу')
            time.sleep(7)
            pass
        if count == 1:
            print(f'Теперь {self.__color}. Подождите немного — он горит совсем недолго')
            time.sleep(2)
            pass
        if count == 2:
            print(f'Загорелся {self.__color}. Можно идти!')
            time.sleep(5)
            pass

a = TrafficLight()
a
