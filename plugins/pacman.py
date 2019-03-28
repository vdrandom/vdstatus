import plugins
import subprocess


PACMAN_DEFAULTS = {
    'cmd': ('/usr/bin/pacman', '-Qu'),
    'title': 'UPD', 'freq': 15, 'problem': 10
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, PACMAN_DEFAULTS)
        self.format_status(0)

    def format_status(self, count):
        self.hide = count == 0
        self.status['urgent'] = count >= self.conf['problem']
        self.status['full_text'] = self.conf['title'] + ': ' + str(count)

    def main(self):
        pacman_qu = subprocess.Popen(
            self.conf['cmd'], stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
            encoding='UTF-8'
        )
        out = pacman_qu.communicate()[0].strip().splitlines()
        packages = [pkg for pkg in out if not '[ignored]' in pkg]
        self.format_status(len(packages))
