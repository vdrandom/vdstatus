import psutil
import plugins


MEM_DEFAULTS = {'title': 'RAM', 'problem': 85}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, MEM_DEFAULTS)

    def main(self):
        mem_stat = psutil.virtual_memory()
        if mem_stat.percent > self.conf['problem']:
            self.hide = False
            urgent = True
        else:
            self.hide = True
            urgent = False

        status = '{:.2f}G'.format(mem_stat.available / 2**30)
        self.format_status(status, urgent)
