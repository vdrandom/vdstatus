import json
import os
import configparser
import importlib
import plugins


DEFAULT_CONFIG = os.path.join(os.environ['HOME'], 'IdeaProjects/vdstatus/conf.ini')

configuration = configparser.ConfigParser()
configuration.read(DEFAULT_CONFIG)


def run_plugins():
    outputs = list()
    for section in configuration.sections():
        if section == 'main':
            continue
        plugin_name = '.' + configuration.get(section, 'plugin')
        plugin_module = importlib.import_module(plugin_name, 'plugins')
        outputs.append(plugin_module.execute(configuration, section))
    return outputs
