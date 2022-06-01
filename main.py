# from fake import sensors, switchers
import random
import time

TEMPERATURE = 25


def adjustment(current_temperature):
    while current_temperature != 25:
        if current_temperature < TEMPERATURE:
            current_temperature += 1
            print(current_temperature)
        else:
            current_temperature -= 1
            print(current_temperature)
        time.sleep(1)
    return current_temperature


while True:
    current_temperature = random.randint(22, 28)
    if not current_temperature == TEMPERATURE:
        current_temperature = adjustment(current_temperature)

    time.sleep(3)