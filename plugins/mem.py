import psutil
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {'problem': 85}
        super(PluginThread, self).__init__(config, defaults)

    def main(self):
        mem_stat = psutil.virtual_memory()
        if mem_stat.percent > self.conf['problem']:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False
        mem_available = round(mem_stat.available / 2**30, 2)
        self.status['full_text'] = 'RAM: {:.2f}G'.format(mem_available)
