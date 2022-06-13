import time
from fake import sensors, switchers

class DeviceOperator():
    def __init__(self, value, sensor, switcher, parametr):
        self.value = value
        self.sensor = sensor
        self.switcher = switcher
        self.parametr = parametr

    def check_and_control(self):
        while True:
            parametr_now = self.sensor.get_value()
            if parametr_now < self.value:
                self.switcher.turn_on()
                print(self.parametr,parametr_now)
            elif parametr_now > self.value:
                self.switcher.turn_off()
                print(self.parametr, parametr_now)
            time.sleep(1)

temperature_d_o = DeviceOperator(17, sensors.temperature, switchers.temperature, "temperature")
temperature_d_o.check_and_control()

moisture_d_o = DeviceOperator(55, sensors.moisture, switchers.moisture, "moisture")
moisture_d_o.check_and_control()

humidity_d_o = DeviceOperator(55, sensors.humidity, switchers.humidity, "humidity")
humidity_d_o.check_and_control()