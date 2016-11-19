import psutil
import plugins.common


class PluginThread(plugins.common.PluginThreadCommon):
    def __init__(self, section, config, thread_id):
        super(PluginThread, self).__init__(section, config)

    def main(self):
        mem_stat = psutil.virtual_memory()
        mem_available = str(round(mem_stat.available / 2**30, 2))
        mem = 'RAM: ' + mem_available + 'G'
        self.status['full_text'] = mem
