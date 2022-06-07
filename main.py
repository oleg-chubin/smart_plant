import time

from detector import Detector
from sensors import Sensor
from switchers import Switcher


class DeviceOperator(Sensor, Switcher, Detector):

    def set_expected_level(self, value_for_control):
        """Получает значение для контроля параметра"""
        self.value_for_control = value_for_control
        print(self.value_for_control)

    def current_value(self):
        """Выводит текущее значение параметра"""
        return self.current_val

    def check_and_control(self):
        """Проверяет текущее значение на отклонение от заданного"""
        self.value_from_detector()
        if self.current_val != self.value_for_control:
            return self.turn_on("on")
        else:
            return self.turn_off("off")


BIO_CYCLE = [
    {'period': 5, 'light': 1000, 'temperature': 23, 'moisture': 80, 'humidity': 34},
    {'period': 4, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
    {'period': 4, 'light': 0, 'temperature': 18, 'moisture': 70, 'humidity': 45},
    {'period': 4, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
]

temperature = DeviceOperator()
soil_moisture = DeviceOperator()
air_humidity = DeviceOperator()
light = DeviceOperator()

for i in BIO_CYCLE:
    temperature.set_expected_level(i.get('temperature'))
    soil_moisture.set_expected_level(i.get('moisture'))
    air_humidity.set_expected_level(i.get('humidity'))
    light.set_expected_level(i.get('light'))
    print("----------------------")
    cycle_change_time = time.time() // 1 + i.get('period')
    current_time = None

    while cycle_change_time != current_time:
        print(f' Состояние: {temperature.check_and_control()}. Температура: {temperature.get_value()}(°C)')
        print(f' Состояние: {soil_moisture.check_and_control()}. Влажность почвы: {soil_moisture.get_value()}(%)')
        print(f' Состояние: {air_humidity.check_and_control()}. Влажность воздуха: {air_humidity.get_value()}(%)')
        print(f' Состояние: {light.check_and_control()}. Освещенность: {light.get_value()}(lm)')
        current_time = time.time() // 1
        time.sleep(1)
