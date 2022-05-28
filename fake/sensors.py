from sensors import BaseSensor


class FakeSensor(BaseSensor):
    name = None
    initial_value = None
    
    def __init__(self, storage):
        self.storage = storage

    def get_value(self):
        return self.storage.get_current_value()


            
            

