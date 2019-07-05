import os
import plugins


LOAD_DEFAULTS = {'title': 'LA', 'freq': 20, 'problem': 1}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, LOAD_DEFAULTS)

    def main(self):
        loads = os.getloadavg()
        if loads[0] >= self.conf['problem']:
            self.hide = False
            urgent = True
        else:
            self.hide = True
            urgent = False
        status = '{:.2f} {:.2f} {:.2f}'.format(*loads)
        self.format_status(status, urgent=urgent)
