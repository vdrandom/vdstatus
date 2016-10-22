import threading
import time


BATTERY_DIR = '/sys/class/power_supply/BAT0/'


class PluginThread(threading.Thread):
    def __init__(self, section, config, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.status = dict()
        if config.has_option(section, 'color'):
            self.status['color'] = config.get(section, 'color')
        self.freq = config.get(section, 'freq', fallback=1)

    def main(self):
        with open(BATTERY_DIR + 'capacity', 'r') as capacity, \
                open(BATTERY_DIR + 'status', 'r') as status:
            batt_stat = status.read().strip()
            batt_capacity = capacity.read().strip()
        if batt_stat != 'Discharging':
            batt_stat = '\u2191'
        else:
            batt_stat = '\u2193'
        batt = 'BAT: ' + batt_capacity + '% ' + batt_stat

        self.status['full_text'] = batt

    def run(self):
        while True:
            self.main()
            time.sleep(self.freq)
