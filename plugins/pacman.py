import plugins
import subprocess


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {
            'freq': 15,
            'problem': 10
        }
        super(PluginThread, self).__init__(config, defaults)
        self.format_status(list())

    def format_status(self, updates):
        count = int()
        for update in updates:
            if not '[ignored]' in update:
                count += 1
        self.hide = count == 0
        self.status['urgent'] = count >= self.conf['problem']
        self.status['full_text'] = 'UPD: ' + str(count)

    def main(self):
        pacman_qu = subprocess.Popen(
            ('/usr/bin/pacman', '-Qu'), stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )
        out = str(pacman_qu.communicate()[0])
        self.format_status(out.splitlines())
