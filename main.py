import time
from fake import sensors, switchers

TEMP_CONST = 16
MOIS_CONST = 56
HUM_CONST = 60

class DeviceOperator():
    def __init__(self, switcher, sensor):
        self.switcher = switcher
        self.sensor = sensor
    def set_expected_level(self, value):
        self.value = value
    def check_and_control(self):
        self.switcher.turn_off()
        if self.sensor < self.value:
            self.switcher.turn_on()
        print(self.sensor)

indicators =[]
temperature = DeviceOperator(switchers.temperature, sensors.temperature.get_value())
temperature.set_expected_level(TEMP_CONST)
indicators.append(temperature)
moisture = DeviceOperator(switchers.moisture, sensors.moisture.get_value())
moisture.set_expected_level(MOIS_CONST)
indicators.append(moisture)
humidity = DeviceOperator(switchers.humidity, sensors.humidity.get_value())
humidity.set_expected_level(HUM_CONST)
indicators.append(humidity)

while True:
    for indicator in indicators:
        indicator.check_and_control()
    time.sleep(2)
