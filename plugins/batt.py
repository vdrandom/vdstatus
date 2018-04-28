import plugins


BATTERY_DIR = '/sys/class/power_supply/BAT0/'


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {
            'problem': 15,
            'symbol_charging': '\u2191',
            'symbol_discharging': '\u2193'
        }
        super(PluginThread, self).__init__(config, defaults)

    def main(self):
        with \
                open(BATTERY_DIR + 'capacity', 'r') as batt_capacity, \
                open(BATTERY_DIR + 'status', 'r') as batt_status:
            status = batt_status.read().strip()
            capacity = batt_capacity.read().strip()
        if status != 'Discharging':
            symbol = self.conf['symbol_charging']
            self.status['urgent'] = False
        else:
            symbol = self.conf['symbol_discharging']
            self.status['urgent'] = float(capacity) <= self.conf['problem']

        self.status['full_text'] = 'BAT: ' + capacity + '% ' + symbol
