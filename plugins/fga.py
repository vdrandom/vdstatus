# TODO: tidy up the fucking code
import plugins
import requests


URI = 'http://fucking-great-advice.ru/api/random'
class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {'freq': 120}
        super(PluginThread, self).__init__(config, defaults)


    def main(self):
        try:
            req = requests.get(URI, timeout=2)
            advice = req.json()['text'] if req.status_code == 200 else 'N/A'
        except requests.exceptions.Timeout:
            advice = 'N/A (timeout)'
        except requests.exceptions.ConnectionError:
            advice = 'N/A (offline)'
        self.status['full_text'] = advice
