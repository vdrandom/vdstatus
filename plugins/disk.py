import plugins.common
import psutil


class PluginThread(plugins.common.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)
        self.part = config.get(section, 'part')

    def main(self):
        du_stat = psutil.disk_usage(self.part)
        if du_stat.percent >= self.problem_value:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False
        du_free = str(round(du_stat.free / 2**30, 2))
        du = self.part + ': ' + du_free + 'G'
        self.status['full_text'] = du
