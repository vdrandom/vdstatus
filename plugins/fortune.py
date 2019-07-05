import plugins
import requests
import time


FORTUNE_DEFAULTS = {
    'uri': 'http://fucking-great-advice.ru/api/random',
    'freq': 120, 'retry': 3
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, FORTUNE_DEFAULTS)
        self.retry = False

    def main(self):
        try:
            req = requests.get(self.conf['uri'], timeout=2)
            fortune = req.json()['text'] if req.status_code == 200 else 'N/A'
            self.retry = False
        except requests.exceptions.Timeout:
            fortune = 'N/A (timeout)'
            self.retry = True
        except requests.exceptions.ConnectionError:
            fortune = 'N/A (offline)'
            self.retry = True
        self.format_status(fortune)

    def run(self):
        while True:
            self.main()
            if self.retry:
                sleep_time = self.conf['retry']
            else:
                sleep_time = self.conf['freq']
            time.sleep(sleep_time)
