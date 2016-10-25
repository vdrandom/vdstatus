import psutil
import threading
import time


class PluginThread(threading.Thread):
    def __init__(self, section, config, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.status = dict()
        if config.has_option(section, 'color'):
            self.status['color'] = config.get(section, 'color')
        self.freq = config.getint(section, 'freq', fallback=1)
        self.hide = False

    def main(self):
        mem_stat = psutil.virtual_memory()
        mem_available = str(round(mem_stat.available / 2**30, 2))
        mem = 'RAM: ' + mem_available + 'G'
        self.status['full_text'] = mem

    def run(self):
        while True:
            self.main()
            time.sleep(self.freq)
