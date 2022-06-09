import time

from fake import sensors, switchers

while True:

    if sensors.temperature.initial_value != sensors.temperature.get_value():
        switchers.temperature.turn_on()
    else:
        switchers.temperature.turn_off()
    time.sleep(1)
