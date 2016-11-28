import threading
import time


class PluginThreadCommon:
    def __init__(self, section, config):
        self.status = dict()
        self.hide = False
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.freq = config.getint(section, 'freq', fallback=1)
        self.problem_value = config.getint(section, 'problem', fallback=70)
        if config.has_option(section, 'color'):
            self.status['color'] = config.get(section, 'color')

    def start(self):
        self.thread.start()

    def main(self):
        self.status['full_text'] = 'placeholder'

    def run(self):
        while True:
            self.main()
            time.sleep(self.freq)
