import plugins
import psutil


DISK_DEFAULTS = {'partition': '/', 'problem': 80, 'freq': 15}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, DISK_DEFAULTS)
        if 'title' not in self.conf:
            self.conf['title'] = self.conf['partition']

    def main(self):
        du_stat = psutil.disk_usage(self.conf['partition'])
        if du_stat.percent >= self.conf['problem']:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False

        status = '{:.2f}G'.format(du_stat.free / 2**30)
        self.format_status(status)
