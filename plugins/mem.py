import psutil
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)

    def main(self):
        mem_stat = psutil.virtual_memory()
        mem_available = str(round(mem_stat.available / 2**30, 2))
        mem = 'RAM: ' + mem_available + 'G'
        self.status['full_text'] = mem
