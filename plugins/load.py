import os
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {'freq': 20, 'problem': 1}
        super(PluginThread, self).__init__(config, defaults)

    def main(self):
        loads = os.getloadavg()
        if loads[0] >= self.conf['problem']:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False
        self.status['full_text'] = 'LA: {:.2f} {:.2f} {:.2f}'.format(*loads)
