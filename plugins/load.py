import os
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)

    def main(self):
        loads = os.getloadavg()
        if loads[0] >= self.problem_value:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False
        loads = [str(i) for i in loads]
        self.status['full_text'] = 'LA: ' + ' '.join(loads)
