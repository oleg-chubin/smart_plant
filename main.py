import random
import time

class Parameter_control():

    def __init__(self, TEMPERATURE):
        self.TEMPERATURE = TEMPERATURE
        # self.switch_status = switch_status


    def temperature(self):
        current_temperature = 0
        while True:
            while current_temperature != self.TEMPERATURE:
                print(current_temperature)
                if current_temperature < self.TEMPERATURE:
                    current_temperature += 1
                else:
                    current_temperature -= 1
                time.sleep(1)
            print(current_temperature)

            current_temperature = random.randint(2, 4)
            time.sleep(5)

test = Parameter_control(3)
test.temperature()






