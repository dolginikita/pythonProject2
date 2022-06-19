import time
import random


class TrafficLight:
    __color = [('Красный', 7), ('Желтый', 2), ('Зеленый', random.randint(1, 10))]

    def runing(self):
        for c, t in self.__color:
            print(f'включен {c} свет, на {t} секунд')
            time.sleep(t)
            print('!!! Переключение светофора !!!')


traf_light = TrafficLight()
traf_light.runing()

