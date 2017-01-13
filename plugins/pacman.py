import plugins
import subprocess


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, section, config):
        super(PluginThread, self).__init__(section, config)
        self.freq = config.getint(section, 'freq', fallback=15)
        self.format_status(0)

    def format_status(self, count):
        self.status['full_text'] = 'UPD: ' + str(count)
        if count > 0:
            self.hide = False
            self.status['urgent'] = True
        else:
            self.hide = True
            self.status['urgent'] = False

    def main(self):
        # TODO: this is an ugly hack, fix it with subprocess.Popen asap
        updates = subprocess.getoutput('/usr/bin/pacman -Qu').count(" -> ")
        self.format_status(updates)
