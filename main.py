import time
from fake import sensors, switchers

BIO_CYCLE = [
    {'period': 36000, 'light': 1000, 'temperature': 23, 'moisture': 80, 'humidity': 34},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
    {'period': 36000, 'light': 0, 'temperature': 18, 'moisture': 70, 'humidity': 45},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
]

class DeviceOperator():
    def __init__(self, sensor, switcher, parametr, value=0):
        self.value = value
        self.sensor = sensor
        self.switcher = switcher
        self.parametr = parametr

    def set_value(self, value):
        self.value = value

    def check_and_control(self):
            parametr_now = self.sensor.get_value()
            if parametr_now < self.value:
                self.switcher.turn_on()
                print(self.parametr,parametr_now)
            elif parametr_now > self.value:
                self.switcher.turn_off()
                print(self.parametr, parametr_now)





temperature_d_o = DeviceOperator(sensors.temperature, switchers.temperature, "temperature")
moisture_d_o = DeviceOperator(sensors.moisture, switchers.moisture, "moisture")
humidity_d_o = DeviceOperator(sensors.humidity, switchers.humidity, "humidity")
light_d_o = DeviceOperator(sensors.light, switchers.light, "light")

device_operators = [temperature_d_o, moisture_d_o, humidity_d_o, light_d_o]

switchers.temperature.turn_on()
switchers.temperature.turn_off()

while True:
    def get_need_circle(data):
        periods = [i['period'] for i in data]
        all_time = time.time()
        current_time = all_time % sum(periods)
        for i, p in enumerate(periods):
            if p > current_time:
                break
            current_time -= p
        return data[i]

    circle_from_period = get_need_circle(BIO_CYCLE)
    for d_o in device_operators:
        d_o.set_value(circle_from_period[d_o.parametr])
        d_o.check_and_control()
        time.sleep(0.5)