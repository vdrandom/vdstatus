import plugins.common


BATTERY_DIR = '/sys/class/power_supply/BAT0/'


class PluginThread(plugins.common.PluginThreadCommon):
    def __init__(self, section, config, thread_id):
        super(PluginThread, self).__init__(section, config)

    def main(self):
        with open(BATTERY_DIR + 'capacity', 'r') as capacity, \
                open(BATTERY_DIR + 'status', 'r') as status:
            batt_stat = status.read().strip()
            batt_capacity = capacity.read().strip()
        if batt_stat != 'Discharging':
            batt_stat = '\u2191'
            if float(batt_capacity) < 15:
                self.status['urgent'] = True
            else:
                self.status['urgent'] = False
        else:
            batt_stat = '\u2193'
            self.status['urgent'] = False

        batt = 'BAT: ' + batt_capacity + '% ' + batt_stat

        self.status['full_text'] = batt
