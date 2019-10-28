import plugins
import subprocess


PACMAN_DEFAULTS = {
    'cmd': ('/usr/bin/echo', 'I am cmd'),
    'title': 'CMD', 'freq': 15
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
        out = pacman_qu.communicate()[0].strip().splitlines()[0]

        self.format_status(out)
