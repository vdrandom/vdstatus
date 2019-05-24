import plugins


FILECAT_DEFAULTS = {
    'filename': '/etc/hostname', 'title': 'CAT',
    'freq': 60, 'nofile': 'unavailable'
}


class PluginThread(plugins.PluginThreadCommon):
    def __init__(self, config):
        super(PluginThread, self).__init__(config, FILECAT_DEFAULTS)
        self.hide = False
        self.format_status(self.conf['title'], False)

    def format_status(self, contents, urgent):
        self.status['urgent'] = urgent
        self.status['full_text'] = self.conf['title'] + ': ' + contents

    def main(self):
        try:
            with open(self.conf['filename'], 'r') as datafile:
                contents = datafile.read().strip()
            urgent = False
        except FileNotFoundError:
            contents = self.conf['nofile']
            urgent = True
        self.format_status(contents, urgent)
