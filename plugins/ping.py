import os
import random
import time
import threading


class ConnTest(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.hosts = list()
        self.status = 'n/a'
        self.freq = int()

    def configure(self, hosts, freq=5):
        self.hosts = hosts.split(',')
        self.freq = freq

    def run(self):
        global is_running
        is_running = True
        while True:
            random.shuffle(self.hosts)
            try:
                for host in self.hosts:
                    fping = 'fping -q -c1 -t100 ' + host + ' &>/dev/null'
                    response = os.system(fping)
                    if response == 0:
                        self.status = 'on'
                        break
                    self.status = 'off'

            except (KeyboardInterrupt, SystemExit):
                break
            time.sleep(self.freq)

is_running = False
ping_object = ConnTest(1, 'test_network')


def execute(config, section):
    result = dict()
    global ping_object
    if is_running is False:
        ping_object.configure(config.get(section, 'hosts'), 10)
        ping_object.start()
    result['full_text'] = config.get(section, 'title') + ' ' + ping_object.status
    return result
