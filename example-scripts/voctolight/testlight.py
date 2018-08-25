#!/usr/bin/env python3
# Test driver for Voctolight plugins.
from lib.config import Config
from lib.plugins.all_plugins import PLUGINS

def main():
    plugin_cls = PLUGINS.get(Config.get('light', 'plugin'), None)
    if plugin_cls is None:
        print('No plugin selected, control will not work!')
        
    plugin = plugin_cls(Config)
    
    try:
        while True:
            print('Tally light on. Press ENTER to turn off, ^C to stop.')
            plugin.tally_on()
            input()
            print('Tally light off. Press ENTER to turn on, ^C to stop.')
            plugin.tally_off()
            input()
    except KeyboardInterrupt:
        pass

if __name__ in '__main__':
    main()
