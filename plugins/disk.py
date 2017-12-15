import plugins
import psutil


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {'partition': '/', 'problem': 80}
        super(PluginThread, self).__init__(config, defaults)

    def main(self):
        du_stat = psutil.disk_usage(self.conf['partition'])
        if du_stat.percent >= self.conf['problem']:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False
        du_free = str(round(du_stat.free / 2**30, 2))
        disk_usage = self.conf['partition'] + ': ' + du_free + 'G'
        self.status['full_text'] = disk_usage
