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
        self.status = dict()
        self.freq = 5
        self.format_status('n/a')

    def format_status(self, state):
        self.status['full_text'] = self.title + ': ' + state

    def run(self):
        while True:
            random.shuffle(self.hosts)
            try:
                for host in self.hosts:
                    fping = 'fping -q -c1 -t100 ' + host + ' &>/dev/null'
                    response = os.system(fping)
                    if response == 0:
                        self.format_status('on')
                        break
                    self.format_status('off')

            except (KeyboardInterrupt, SystemExit):
                break
            time.sleep(self.freq)
