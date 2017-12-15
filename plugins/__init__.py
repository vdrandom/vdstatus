import threading
import time


def parse_config(config, defaults):
    result = dict()
    for key in defaults:
        result[key] = config[key] if key in config else defaults[key]
    return result


class PluginThreadCommon:
    def __init__(self, config, defaults=dict()):
        if 'freq' not in defaults:
            defaults['freq'] = 1
        if 'hide_ok' not in defaults:
            defaults['hide_ok'] = True
        self.conf = parse_config(config, defaults)
        self.status = dict()
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
