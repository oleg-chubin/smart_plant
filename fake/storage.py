import time
from abc import abstractmethod, ABCMeta


class StorageMeta(ABCMeta):
    STORAGES = {}

    def __new__(mcs, class_name, parents, attributes):
        storage_type = None
        if 'storage_type' in attributes:
            storage_type = attributes.pop('storage_type')
        if storage_type in mcs.STORAGES:
            raise AttributeError(f'Storage {storage_type} is already registered')
        # Here we could add some helper methods or attributes to c
        cls = super().__new__(mcs, class_name, parents, attributes)
        if storage_type:
            mcs.STORAGES[storage_type] = cls
        return cls


class BaseStorage(list, metaclass=StorageMeta):
    @classmethod
    def create(cls, storage_type, **kwargs):
        if storage_type not in cls.STORAGES:
            raise ValueError(f'Storage {storage_type} is not registered')
        return cls.STORAGES[storage_type](**kwargs)

    @abstractmethod
    def get_decreasing_value(self, previous_state, current_time):
        raise NotImplementedError

    @abstractmethod
    def get_increasing_value(self, previous_state, current_time):
        raise NotImplementedError
        
    def get_previous_state(self):
        if not self:
            return {
                'value': self.initial_value,
                'time': time.time(),
                'command': 'off'
            }
        return self[-1]

    def get_current_value(self):
        return self.get_value(time.time())

    def get_value(self, current_time):
        previous_state = self.get_previous_state()
        if previous_state['command'] == 'off':
            return self.get_decreasing_value(previous_state, current_time)
        return self.get_increasing_value(previous_state, current_time)

    def _set_state(self, state):
        current_time = time.time()
        recent_state = {
            'command': state,
            'time': current_time,
            'value': self.get_value(current_time)
        }
        self.append(recent_state)

    def turn_on(self):
        previous_state = self.get_previous_state()
        if previous_state['command'] == 'off':
            self._set_state('on')

    def turn_off(self):
        previous_state = self.get_previous_state()
        if previous_state['command'] == 'on':
            self._set_state('off')


class LinearStorage(BaseStorage):
    storage_type = 'linear'

    def __init__(self, initial_value, incr_rate, decr_rate):
        self.initial_value = initial_value
        self.incr_rate = incr_rate
        self.decr_rate = decr_rate

    def get_decreasing_value(self, previous_state, current_time):
        return previous_state['value'] - (current_time - previous_state['time']) * self.decr_rate

    def get_increasing_value(self, previous_state, current_time):
        return previous_state['value'] + (current_time - previous_state['time']) * self.incr_rate


class StepStorage(BaseStorage):
    storage_type = 'step'

    def __init__(self, on_value, off_value):
        self.initial_value = off_value
        self.on_value = on_value
        self.off_value = off_value

    def get_decreasing_value(self, previous_state, current_time):
        return self.off_value

    def get_increasing_value(self, previous_state, current_time):
        return self.on_value
