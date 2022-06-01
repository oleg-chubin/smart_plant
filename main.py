import time
from fake import sensors, switchers

class DeviceOperator:
    def __init__(self, value, switcher, sensor):
        self.value = value
        self.switcher = switcher
        self.sensor = sensor
        # print(value, switcher, sensor)
    def set_expected_level(self, set_value):
        self.set_value = set_value

    def check_and_control(self):
        print(self.sensor.get_value())
        print(self.get_expected_level())
        if self.sensor.get_value() < self.get_expected_level():
            self.switcher.turn_on()
        else:
            self.switcher.turn_off()

    def get_expected_level(self):
        return self.value

temperature_device_operator = DeviceOperator(23, switchers.temperature, sensors.temperature)
moisture_device_operator = DeviceOperator(23, switchers.temperature, sensors.temperature)
humidity_device_operator = DeviceOperator(23, switchers.temperature, sensors.temperature)

n = 2
while n:
    temperature_device_operator.check_and_control()
    moisture_device_operator.check_and_control()
    humidity_device_operator.check_and_control()

    n -= 1


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