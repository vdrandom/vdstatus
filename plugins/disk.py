import psutil
import threading
import time


class PluginThread(threading.Thread):
    def __init__(self, section, config, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.status = dict()
        self.part = config.get(section, 'part')
        if config.has_option(section, 'color'):
            self.status['color'] = config.get(section, 'color')
        self.freq = config.getint(section, 'freq', fallback=30)

    def main(self):
        du_stat = psutil.disk_usage(self.part)
        # du_perc = str(du_stat.percent)
        du_free = str(round(du_stat.free / 2**30, 2))
        du = self.part + ': ' + du_free + 'G'
        self.status['full_text'] = du

    def run(self):
        while True:
            self.main()
            time.sleep(self.freq)
