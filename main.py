import time
from fake import sensors, switchers

BIO_CYCLE = [
    {'period': 36000, 'light': 1000, 'temperature': 23, 'moisture': 80, 'humidity': 34},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
    {'period': 36000, 'light': 0, 'temperature': 18, 'moisture': 70, 'humidity': 45},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
]

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

def circle(bio_cycle):
    bio_cycle_periods = [data['period'] for data in bio_cycle]
    nowadays = time.time()
    remain_time = nowadays % sum(bio_cycle_periods)
    for i, j in enumerate(bio_cycle_periods):
        if j > remain_time:
            break
        remain_time -= j
    #print(remain_time)
    return bio_cycle[i]

currient_period = circle(BIO_CYCLE)

indicators =[]
temperature = DeviceOperator(switchers.temperature, sensors.temperature.get_value())
temperature.set_expected_level(currient_period['temperature'])
indicators.append(temperature)
moisture = DeviceOperator(switchers.moisture, sensors.moisture.get_value())
moisture.set_expected_level(currient_period['moisture'])
indicators.append(moisture)
humidity = DeviceOperator(switchers.humidity, sensors.humidity.get_value())
humidity.set_expected_level(currient_period['humidity'])
indicators.append(humidity)
light = DeviceOperator(switchers.light, sensors.light.get_value())
light.set_expected_level(currient_period['light'])
indicators.append(light)
print(currient_period)

while True:
    for indicator in indicators:
        indicator.check_and_control()
    time.sleep(2)