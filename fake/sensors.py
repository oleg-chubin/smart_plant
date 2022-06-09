from Sensors_1 import BaseSensor

class FakeSensor(BaseSensor):
    name = None
    initial_value = 13

    def __init__(self, storage):
        self.storage = storage

    def get_value(self):
        return self.storage.get_current_value()



