import time


def run(conf):
    fmt = conf['format']
    return time.strftime(fmt)
