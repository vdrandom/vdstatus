import time


def run(conf):
    fmt = conf['date']['format']
    return time.strftime(fmt)
