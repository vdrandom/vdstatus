import time
import threading


class PluginThread(threading.Thread):
    def __init__(self, section, config, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.date_format = config.get(section, 'format')
        self.status = dict()
        if config.has_option(section, 'color'):
            self.status['color'] = config.get(section, 'color')
        self.freq = 1

    def run(self):
        while True:
            self.status['full_text'] = time.strftime(self.date_format)
            time.sleep(self.freq)
