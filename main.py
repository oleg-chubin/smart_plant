import time

from fake import sensors, switchers

BIO_CYCLE = [
    {'period': 36000, 'light': 1000, 'temperature': 23, 'moisture': 80, 'humidity': 34},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34},
    {'period': 36000, 'light': 0, 'temperature': 18, 'moisture': 70, 'humidity': 45},
    {'period': 7200, 'light': 500, 'temperature': 20, 'moisture': 85, 'humidity': 34}
]


class DeviceOperator:
    def __init__(self, sensor, switcher):
        self.sensor = sensor
        self.switcher = switcher

    def check_and_control(self, initial_value):
        self.initial_value = initial_value

        if self.initial_value > self.sensor.get_value():
            self.switcher.turn_on()
            return self.sensor.get_value()
        else:
            self.switcher.turn_off()
            return self.sensor.get_value()


base_parametrs = {"light": DeviceOperator(sensors.light, switchers.light),
                  "temperature": DeviceOperator(sensors.temperature, switchers.temperature),
                  "moisture": DeviceOperator(sensors.moisture, switchers.moisture),
                  "humidity": DeviceOperator(sensors.humidity, switchers.humidity)}

while True:
    def cycle(znach):
        cycle_change_time = time.time() + next(time_periods)
        while time.time() < cycle_change_time:
            for numb, parametr in enumerate(base_parametrs):
                base_parametrs.get(parametr).check_and_control(znach[numb])
            time.sleep(1)


    time_periods = iter([period.get("period") for period in BIO_CYCLE])

    list(map(cycle, [(cycle.get("light"),
                      cycle.get("temperature"),
                      cycle.get("moisture"),
                      cycle.get("humidity")) for cycle in BIO_CYCLE]))
