# Tk tally light

__all__ = ['Tk']

DO_TK = True
try:
    import tkinter as tk
except ImportError:
    DO_TK = False
from sys import exit


class Tk:
    def __init__(self, config):
        if not DO_TK:
            raise ValueError('Tk support not available.')

        self.on_colour = config.get('tk', 'on_colour')
        self.off_colour = config.get('tk', 'off_colour')

        self.app = tk.Tk()
        self.app.protocol('WM_DELETE_WINDOW', self.quit_callback)
        self.app.title('Voctomix Tally Light')
        self.app.geometry('300x300')

    def pump(self):
        self.app.update()

    def tally_on(self):
        print('tally on')
        self.app.config(bg=self.on_colour)

    def tally_off(self):
        print('tally off')
        self.app.config(bg=self.off_colour)

    def quit_callback(self):
        exit(0)
