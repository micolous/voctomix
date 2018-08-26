# Plugin to provide a tally light interface via stdout
__all__ = ['Stdout']

class Stdout:
    def __init__(self, config):
        # We don't need an explicit event loop pump
        self.pump = lambda: None

    def tally_on(self):
        print('Tally light on')

    def tally_off(self):
        print('Tally light off')
