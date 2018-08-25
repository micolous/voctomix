from .rpi_gpio import RpiGpio
from .stdout import Stdout
from .tomu_simple_led import TomuSimpleLed


PLUGINS = {
    'rpi_gpio': RpiGpio,
    'stdout': Stdout,
    'tomu_simple_led': TomuSimpleLed
}
