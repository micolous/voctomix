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
        if not DO_GPIO:
            raise ValueError('RpiGpio will not work on this platform. Is RPi.GPIO installed?')

        # We don't need an explicit event loop pump
        self.pump = lambda _: pass

        all_gpios = [int(i) for i in config.get('rpi', 'gpios').split(',')]
        self.gpio_port = int(config.get('rpi', 'gpio_red'))

        GPIO.setup(all_gpios, GPIO.OUT)
        GPIO.output(all_gpios, GPIO.HIGH)

    def tally_on(self):
        GPIO.output(self.gpio_port, GPIO.LOW)

    def tally_off(self):
        GPIO.output(self.gpio_port, GPIO.HIGH)

    def __del__(self):
        GPIO.cleanup()
