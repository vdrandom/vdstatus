import json
import os
import configparser
import importlib
import plugins
import time


DEFAULT_CONFIG = os.path.join(os.environ['HOME'], 'IdeaProjects/vdstatus/conf.ini')

configuration = configparser.ConfigParser()
configuration.read(DEFAULT_CONFIG)


def load_plugins(config):
    plugins_loaded = list()
    config.remove_section('main')
    for section in config.sections():
        plugin_name = config.get(section, 'plugin')
        plugin_id = len(plugins_loaded)
        module = importlib.import_module('.' + plugin_name, 'plugins')
        thread_object = module.PluginThread(section, config, plugin_id)
        plugins_loaded.append(thread_object)
    return plugins_loaded


def run_plugins():
    plugins_l = load_plugins(configuration)
    for plugin in plugins_l:
        plugin.start()

    while True:
        outputs = list()
        for plugin in plugins_l:
            outputs.append(plugin.status)
        print(json.dumps(outputs) + ',')
        time.sleep(1)
