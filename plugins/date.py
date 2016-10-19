import time


def execute(config, section):
    fmt = config.get(section, 'format')
    result = dict()
    if config.has_option(section, 'color'):
        result['color'] = config.get(section, 'color')
    result['full_text'] = time.strftime(fmt)
    return result
