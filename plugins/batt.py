import plugins


BATT_DEFAULTS = {
    'title': 'BAT',
    'problem': 15,
    'symbol_charging': '\u2191',
    'symbol_discharging': '\u2193'
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, BATT_DEFAULTS)

    def main(self):
        with \
                open('/sys/class/power_supply/BAT0/capacity', 'r') as bcap, \
                open('/sys/class/power_supply/BAT0/status', 'r') as bstat:
            capacity = bcap.readline().strip()
            status_value = bstat.readline().strip()

        if status_value != 'Discharging':
            symbol = self.conf['symbol_charging']
            urgent = False
        else:
            symbol = self.conf['symbol_discharging']
            urgent = float(capacity) <= self.conf['problem']

        status = '{}% {}'.format(capacity, symbol)
        self.format_status(status, urgent)
