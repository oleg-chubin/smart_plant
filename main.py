import time

from fake import sensors, switchers

class DeviceOperator:
    # def __init__(self):
    #     pass
    def set_expected_level(self, set_value):
        return self.set_value
    def check_and_control(self, check_value):
        if self.check_value.get_value() < self.check_value.set_expected_level():
            switchers.temperature.turn_on()
        else:
            switchers.temperature.turn_off()

    def get_expected_level(self, get_value):
        return self.get_value

value_moisture = DeviceOperator()
value_humidity = DeviceOperator()
high_value_moisture = value_moisture.get_expected_level(int(input('Введите максимальное значение влажности земли')))
high_value_humidity = value_humidity.get_expected_level(int(input('Введите максимальное значение влажности воздуха')))

while True:
    sensors.temperature.check_and_control()

    # if sensors.temperature.get_value() < 23:
    #     switchers.temperature.turn_on()
    # else:
    #     switchers.temperature.turn_off()
    # time.sleep(5)
    # if sensors.moisture.get_value() < high_value_moisture:
    #     switchers.moisture.turn_on()
    # else:
    #     switchers.moisture.turn_off()
    # time.sleep(5)
    # if sensors.humidity.get_value() < high_value_humidity:
    #     switchers.humidity.turn_on()
    # else:
    #     switchers.humidity.turn_off()
    # time.sleep(5)