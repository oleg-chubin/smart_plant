from functools import cached_property


class Storages:
    @cached_property
    def light(self):
        from fake.storage import StepStorage
        return StepStorage(1000, 0)

    @cached_property
    def humidity(self):
        from fake.storage import LinearStorage
        return LinearStorage(50, 1, 0.1)

    @cached_property
    def moisture(self):
        from fake.storage import LinearStorage
        return LinearStorage(50, 2, 0.01)

    @cached_property
    def temperature(self):
        from fake.storage import LinearStorage
        return LinearStorage(14, 0.2, 0.1)


storages = Storages()


class Sensors:
    @cached_property
    def light(self):
        from fake.sensors import FakeSensor
        return FakeSensor(storages.light)

    @cached_property
    def humidity(self):
        from fake.sensors import FakeSensor
        return FakeSensor(storages.humidity)

    @cached_property
    def moisture(self):
        from fake.sensors import FakeSensor
        return FakeSensor(storages.moisture)

    @cached_property
    def temperature(self):
        from fake.sensors import FakeSensor
        return FakeSensor(storages.temperature)


class Switchers:
    @cached_property
    def light(self):
        from fake.switchers import FakeSwitcher
        return FakeSwitcher(storages.light)

    @cached_property
    def humidity(self):
        from fake.switchers import FakeSwitcher
        return FakeSwitcher(storages.humidity)

    @cached_property
    def moisture(self):
        from fake.switchers import FakeSwitcher
        return FakeSwitcher(storages.moisture)

    @cached_property
    def temperature(self):
        from fake.switchers import FakeSwitcher
        return FakeSwitcher(storages.temperature)


sensors = Sensors()
switchers = Switchers()
