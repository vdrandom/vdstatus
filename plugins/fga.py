import plugins
import requests
import time


URI = 'http://fucking-great-advice.ru/api/random'
class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {'freq': 120, 'retry': 3}
        super(PluginThread, self).__init__(config, defaults)
        self.retry = False


    def main(self):
        try:
            req = requests.get(URI, timeout=2)
            advice = req.json()['text'] if req.status_code == 200 else 'N/A'
            self.retry = False
        except requests.exceptions.Timeout:
            advice = 'N/A (timeout)'
            self.retry = True
        except requests.exceptions.ConnectionError:
            advice = 'N/A (offline)'
            self.retry = True
        self.status['full_text'] = advice


    def run(self):
        while True:
            self.main()
            if self.retry:
                sleep_time = self.conf['retry']
            else:
                sleep_time = self.conf['freq']
            time.sleep(sleep_time)
