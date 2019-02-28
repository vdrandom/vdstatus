import plugins
import subprocess


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        defaults = {
            'freq': 15,
            'problem': 10
        }
        super(PluginThread, self).__init__(config, defaults)
        self.format_status(0)

    def format_status(self, count):
        self.hide = count == 0
        self.status['urgent'] = count >= self.conf['problem']
        self.status['full_text'] = 'UPD: ' + str(count)

    def main(self):
        pacman_qu = subprocess.Popen(
            ('/usr/bin/pacman', '-Qu'), stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
            encoding='UTF-8'
        )
        out = pacman_qu.communicate()[0].strip().splitlines()
        packages = [pkg for pkg in out if not '[ignored]' in pkg]
        self.format_status(len(packages))
