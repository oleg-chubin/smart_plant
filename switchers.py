# from switchers import BaseSwitcher
class Switcher:

    def turn_on(self, state):
        self.state = state
        return self.state

    def turn_off(self, state):
        self.state = state
        return self.state

