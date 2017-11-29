import datetime
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)
        self.date_format = config.get(section, 'format', fallback='%c')
        tz = config.get(section, 'TZ', fallback=None)
        if tz:
            import pytz
            self.tz = pytz.timezone(tz)
        else:
            self.tz = None

    def main(self):
        now = datetime.datetime.now(tz=self.tz)
        self.status['full_text'] = now.strftime(self.date_format)
