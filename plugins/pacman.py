import plugins
import subprocess


PACMAN_DEFAULTS = {
    'cmd': ('/usr/bin/pacman', '-Qu'),
    'title': 'UPD', 'freq': 15, 'problem': 10
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, PACMAN_DEFAULTS)

    def main(self):
        pacman_qu = subprocess.Popen(
            self.conf['cmd'], stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL,
            encoding='UTF-8'
        )
        out = pacman_qu.communicate()[0].strip().splitlines()
        packages = len([pkg for pkg in out if not '[ignored]' in pkg])
        if packages:
            self.hide = False
        else:
            self.hide = True

        urgent = packages >= self.conf['problem']
        self.format_status(packages, urgent)
