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
        time.sleep(2)
        print(self.sensor)

temperature = DeviceOperator(switchers.temperature, sensors.temperature.get_value())
temperature.set_expected_level(TEMP_CONST)
#moisture = DeviceOperator(switchers.moisture, sensors.moisture.get_value(), MOIS_CONST)
#humidity = DeviceOperator(switchers.humidity, sensors.humidity.get_value(), HUM_CONST)
while True:
    temperature.check_and_control()
#moisture.check_and_control()
#humidity.check_and_control()