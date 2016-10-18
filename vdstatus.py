import os
import configparser
import importlib
import plugins


def get_plugins(config):
    result = list()
    for element in config['main']['plugins'].split(','):
        result.append(config[element])
    return result

DEFAULT_CONFIG = os.path.join(os.environ['HOME'], 'IdeaProjects/vdstatus/conf.ini')

configuration = configparser.ConfigParser()
configuration.read(DEFAULT_CONFIG)

plugin_list = get_plugins(configuration)

for plugin in plugin_list:
    plugin_name = '.' + plugin['plugin']
    plugin_module = importlib.import_module(plugin_name, 'plugins')
    print(plugin_module.run(plugin))
