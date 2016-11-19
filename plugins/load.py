import os
import plugins.common


class PluginThread(plugins.common.PluginThreadCommon):
    def __init__(self, section, config, thread_id):
        super(PluginThread, self).__init__(section, config)
        self.hide_ok = config.getboolean(section, 'hide_ok', fallback=False)

    def main(self):
        loads = os.getloadavg()
        if loads[0] >= self.problem_value:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = self.hide_ok
            self.status['urgent'] = False
        loads = [str(i) for i in loads]
        self.status['full_text'] = 'LA: ' + ' '.join(loads)
