import plugins


BATTERY_DIR = '/sys/class/power_supply/BAT0/'
BATT_DEFAULTS = {
    'problem': 15,
    'symbol_charging': '\u2191',
    'symbol_discharging': '\u2193'
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, BATT_DEFAULTS)

    def main(self):
        with \
                open(BATTERY_DIR + 'capacity', 'r') as batt_capacity, \
                open(BATTERY_DIR + 'status', 'r') as batt_status:
            capacity = batt_capacity.readline().strip()
            status_value = batt_status.readline().strip()

        if status_value != 'Discharging':
            symbol = self.conf['symbol_charging']
            urgent = False
        else:
            symbol = self.conf['symbol_discharging']
            urgent = float(capacity) <= self.conf['problem']

        self.format_status(capacity + '% ' + symbol, urgent=urgent)
