import threading
import time


PLUGIN_DEFAULTS = {'freq': 1, 'hide_ok': True}


class PluginThreadCommon:
    def __init__(self, config, defaults=None):
        self.status = dict()
        self.conf = dict()
        self.conf.update(PLUGIN_DEFAULTS)
        if defaults:
            self.conf.update(defaults)
        self.conf.update(config)
        self.hide = False
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True

    def start(self):
        self.thread.start()

    def main(self):
        self.status['full_text'] = 'placeholder'

    def run(self):
        while True:
            self.main()
            time.sleep(self.conf['freq'])
