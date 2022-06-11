import time

from fake import sensors, switchers

TEMP = 20

while True:
    temp_now = sensors.temperature.get_value()
    if temp_now < TEMP:
        switchers.temperature.turn_on()
        print(temp_now)
    elif temp_now > TEMP:
        switchers.temperature.turn_off()
        print(temp_now)
    time.sleep(2)


