import random
import time


class Switcher:

    def turn_on(self, state):
        self.state = state
        return self.state

    def turn_off(self, state):
        self.state = state
        return self.state


class Sensor:
    def get_value(self):
        return self.current_value()


# -------------------------------

class DeviceOperator(Sensor, Switcher):

    """Получает значение для контроля параметра"""
    def set_expected_level(self, value):
        self.value = value
        print(self.value)

    """Имитирует отклонение от установленного заначения, возвращает текущее значение для вывода"""
    def current_value(self):
        self.current_val = random.randint(self.value - 2, self.value + 2)
        return self.current_val

    """Проверяет текущее значение на отклонение от заданного"""
    def check_and_control(self):
        if self.current_val != self.value:
            return self.turn_on("on")
        else:
            return self.turn_off("off")


class Check(DeviceOperator):
    def __init__(self, value):
        self.value = value

    """Выводит данные"""
    def check(self):
        while True:
            self.set_expected_level(self.value)
            print(self.current_value())
            print(self.check_and_control())
            time.sleep(3)


temperature = Check(int(input("Введите значение температуры (°): ")))
# soil_moisture = Check(int(input("Введите значение влажности почвы (%): ")))
# air_humidity = Check(int(input("Введите значение влажности воздуха (%): ")))

temperature.check()
# soil_moisture.check()
# air_humidity.check()
