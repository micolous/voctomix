from .rpi_gpio import RpiGpio
from .stdout import Stdout


PLUGINS = {
    'rpi_gpio': RpiGpio,
    'stdout': Stdout,
}
