import os
import subprocess
import random
import plugins


PING_DEFAULTS = {
    'hosts': tuple(), 'title': 'PING', 'timeout': 150
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, PING_DEFAULTS)
        self.ping_cmd = ('fping', '-c1', '-qt' + str(self.conf['timeout']))

    def main(self):
        host = random.choice(self.conf['hosts'])
        fping = subprocess.run(
            (*self.ping_cmd, host),
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        if fping.returncode == 0:
            self.format_status('up')
        else:
            self.format_status('down', urgent=True)
