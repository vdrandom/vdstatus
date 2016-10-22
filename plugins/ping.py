import os
import random
import time
import threading


class PluginThread(threading.Thread):
    def __init__(self, section, config, thread_id):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.hosts = config.get(section, 'hosts').split(',')
        self.title = config.get(section, 'title')
        if config.has_option(section, 'colors'):
            self.colors = config.get(section, 'colors').split(',')
        else:
            self.colors = None
        self.timeout = config.get(section, 'timeout', fallback='150')
        self.status = dict()
        self.freq = config.getint(section, 'freq', fallback=5)
        self.format_status('n/a')

    def format_status(self, state):
        self.status['full_text'] = self.title + ': ' + state
        if self.colors is not None:
            if state == 'on':
                self.status['color'] = self.colors[0]
            else:
                self.status['color'] = self.colors[1]

    def main(self):
        random.shuffle(self.hosts)
        for host in self.hosts:
            fping = 'fping -q -c1 -t' + self.timeout + ' ' + host + ' &>/dev/null'
            response = os.system(fping)
            if response == 0:
                self.format_status('on')
                break
            self.format_status('off')

    def run(self):
        while True:
            self.main()
            time.sleep(self.freq)
