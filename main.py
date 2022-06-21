import time
from fake import sensors, switchers
#print(sensors.temperature.get_value())
#switchers.temperature.turn_on()
#print(sensors.temperature.get_value())
while True:
    switchers.temperature.turn_off()
    if sensors.temperature.get_value() < 16:
        switchers.temperature.turn_on()
    time.sleep(1)

    print(sensors.temperature.get_value())