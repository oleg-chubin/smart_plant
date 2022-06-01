import time

from fake import sensors, switchers

# print(sensors.temperature.get_value())
# switchers.temperature.turn_on()
# print(sensors.temperature.get_value())


while True:
    if sensors.temperature.get_value() < 23:
        switchers.temperature.turn_on()
    else:
        switchers.temperature.turn_off()
    time.sleep(5)