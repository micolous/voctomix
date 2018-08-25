# Plugin to provide a tally light interface for a Raspberry Pi's GPIO
DO_GPIO = True
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
except ImportError:
    DO_GPIO = False

__all__ = ['RpiGpio']

class RpiGpio:
    def __init__(self, config):
        all_gpios = [int(i) for i in config.get('light', 'gpios').split(',')]
        self.gpio_port = int(config.get('light', 'gpio_red'))

        if DO_GPIO:
            GPIO.setup(all_gpios, GPIO.OUT)
            GPIO.output(all_gpios, GPIO.HIGH)
        else:
            print('RpiGpio will not work on this platform. Is RPi.GPIO installed?')

    def tally_on(self):
        if DO_GPIO:
            GPIO.output(self.gpio_port, GPIO.LOW)

    def tally_off(self):
        if DO_GPIO:
            GPIO.output(self.gpio_port, GPIO.HIGH)

    def __del__(self):
        if DO_GPIO:
            GPIO.cleanup()
