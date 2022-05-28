from switchers import BaseSwitcher


class FakeSwitcher(BaseSwitcher):
    def __init__(self, storage):
        self.storage = storage

    def turn_on(self):
        self.storage.turn_on()
    
    def turn_off(self):
        self.storage.turn_off()
