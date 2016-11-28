import time
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)
        self.date_format = config.get(section, 'format', fallback='%c')

    def main(self):
        self.status['full_text'] = time.strftime(self.date_format)
