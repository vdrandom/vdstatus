import datetime
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {'format': '%c', 'tz': None}
        super(PluginThread, self).__init__(config, defaults)
        self.timezone = None
        if self.conf['tz']:
            import pytz
            self.timezone = pytz.timezone(self.conf['tz'])

    def main(self):
        now = datetime.datetime.now(tz=self.timezone)
        self.status['full_text'] = now.strftime(self.conf['format'])
