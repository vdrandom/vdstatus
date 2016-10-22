import os
import time
import threading


class PluginThread(threading.Thread):
    def __init__(self, section, config, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.date_format = config.get(section, 'format', fallback='%c')
        self.status = dict()
        if config.has_option(section, 'color'):
            self.status['color'] = config.get(section, 'color')
        self.freq = config.getint(section, 'freq', fallback=10)

    def main(self):
        loads = os.getloadavg()
        loads = [str(i) for i in loads]
        self.status['full_text'] = 'LA: ' + ' '.join(loads)

    def run(self):
        while True:
            self.main()
            time.sleep(self.freq)
