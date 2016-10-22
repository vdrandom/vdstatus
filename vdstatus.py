import json
import os
import configparser
import importlib
import plugins
import time


DEFAULT_CONFIG = os.path.join(os.environ['HOME'], '.config/vdstatus/conf.ini')


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


def format_i3wm(inputs):
    return json.dumps(inputs) + ','


def format_term(inputs):
    return_info = list()
    for item in inputs:
        return_info.append(item['full_text'])
    return ' \033[1m|\033[0m '.join(return_info)


def run_plugins(config_file=DEFAULT_CONFIG):
    configuration = configparser.ConfigParser()
    configuration.read(config_file)
    output_format = configuration.get('main', 'format', fallback='term')

    if output_format == 'i3':
        print('{"version":1}\n[')
        format_outputs = format_i3wm
    # default to terminal output
    else:
        format_outputs = format_term

    plugins_l = load_plugins(configuration)
    for plugin in plugins_l:
        plugin.start()

    while True:
        outputs = list()
        for plugin in plugins_l:
            outputs.append(plugin.status)
        print(format_outputs(outputs))
        time.sleep(1)
