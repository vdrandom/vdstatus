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
        self.hide_ok = config.getboolean(section, 'hide_ok', fallback=False)
        self.hide = False
        self.should_stop = False
        self.problem_value = config.getint(section, 'problem', fallback=100)

    def main(self):
        loads = os.getloadavg()
        if loads[0] >= self.problem_value:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = self.hide_ok
            self.status['urgent'] = False
        loads = [str(i) for i in loads]
        self.status['full_text'] = 'LA: ' + ' '.join(loads)

    def stop(self):
        self.should_stop = True

    def run(self):
        while True:
            if self.should_stop is False:
                self.main()
                time.sleep(self.freq)
            else:
                break
