import datetime
import plugins


DATE_DEFAULTS = {'format': '%c'}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, DATE_DEFAULTS)
        self.timezone = None
        if 'tz' in self.conf:
            import pytz
            self.timezone = pytz.timezone(self.conf['tz'])

    def main(self):
        now = datetime.datetime.now(tz=self.timezone)
        self.status['full_text'] = now.strftime(self.conf['format'])
