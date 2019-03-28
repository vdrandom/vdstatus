import os
import random
import plugins


PING_DEFAULTS = {
    'hosts': list(), 'title': 'PING', 'timeout': 150
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, PING_DEFAULTS)
        self.format_status('n/a')

    def format_status(self, state):
        self.status['full_text'] = self.conf['title'] + ': ' + state
        if state == 'up':
            self.status['urgent'] = False
            self.hide = True
        else:
            self.status['urgent'] = True

    def main(self):
        random.shuffle(self.conf['hosts'])
        for host in self.conf['hosts']:
            fping = 'fping -qc1t' + str(self.conf['timeout'])\
                                        + ' ' + host + ' &>/dev/null'
            response = os.system(fping)
            if response == 0:
                self.format_status('on')
                break
            self.format_status('down')
