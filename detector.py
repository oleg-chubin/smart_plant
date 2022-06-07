import random
class Detector:
    def value_from_detector(self):
        """Подает для контроля текущее значение параметра с датчика"""
        self.current_val = random.randint(self.value_for_control - 2, self.value_for_control + 2)