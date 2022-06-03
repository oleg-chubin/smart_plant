import time
from fake import sensors, switchers


class DeviceOperator:
    def __init__(self, value, switcher, sensor):
        self.value = value
        self.switcher = switcher
        self.sensor = sensor

    def set_expected_level(self, set_value):
        self.value = set_value

    def check_and_control(self):
        print('текущее значение - ', self.sensor.get_value())
        print('значение, которое нужно достигнуть - ', self.get_expected_level())
        if self.sensor.get_value() < self.get_expected_level():
            self.switcher.turn_on()
        else:
            self.switcher.turn_off()

    def get_expected_level(self):
        return self.value

# temperature_device_operator = DeviceOperator(23, switchers.temperature, sensors.temperature)
# moisture_device_operator = DeviceOperator(80, switchers.moisture, sensors.moisture)
# humidity_device_operator = DeviceOperator(34, switchers.humidity, sensors.humidity)

BIO_CYCLE = [
    {'period': 36000, 'light': 1000, 'temperature': 23, 'moisture': 80, 'humidity': 34},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
    {'period': 36000, 'light': 0, 'temperature': 18, 'moisture': 70, 'humidity': 45},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
]
time_period = [36000, 7200, 36000, 7200]
now_time = time.time()
remains_time = now_time % sum(time_period)
for i, t in enumerate(time_period):
    if t > remains_time:
        break
    remains_time -= t

temperature_device_operator = DeviceOperator(BIO_CYCLE[i]['temperature'], switchers.temperature, sensors.temperature)
moisture_device_operator = DeviceOperator(BIO_CYCLE[i]['moisture'], switchers.moisture, sensors.moisture)
humidity_device_operator = DeviceOperator(BIO_CYCLE[i]['humidity'], switchers.humidity, sensors.humidity)
light_device_operator = DeviceOperator(BIO_CYCLE[i]['light'], switchers.light, sensors.light)

n = 5
while n:
    temperature_device_operator.check_and_control()
    moisture_device_operator.check_and_control()
    humidity_device_operator.check_and_control()
    light_device_operator.check_and_control()
    time.sleep(10)

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
