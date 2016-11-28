import os
import random
import plugins


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)
        self.hosts = config.get(section, 'hosts').split(',')
        self.title = config.get(section, 'title')
        self.timeout = config.get(section, 'timeout', fallback='150')
        self.format_status('n/a')

    def format_status(self, state):
        self.status['full_text'] = self.title + ': ' + state
        if state == 'on':
            self.status['urgent'] = False
            self.hide = True
        else:
            self.status['urgent'] = True

    def main(self):
        random.shuffle(self.hosts)
        for host in self.hosts:
            fping = 'fping -qc1t' + self.timeout + ' ' + host + ' &>/dev/null'
            response = os.system(fping)
            if response == 0:
                self.format_status('on')
                break
            self.format_status('off')
