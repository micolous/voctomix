from .rpi_gpio import RpiGpio
from .stdout import Stdout
from .tk import Tk
from .tomu_simple_led import TomuSimpleLed


PLUGINS = {
    'rpi_gpio': RpiGpio,
    'stdout': Stdout,
    'tk': Tk,
    'tomu_simple_led': TomuSimpleLed,
}
