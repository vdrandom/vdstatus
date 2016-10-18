import sys
import os
import configparser
import importlib
import plugins


DEFAULT_CONFIG = os.path.join(os.environ['HOME'], 'IdeaProjects/vdstatus/conf.ini')

configuration = configparser.ConfigParser()
configuration.read(DEFAULT_CONFIG)

importlib.import_module('.date', 'plugins')
print(plugins.date.run(configuration))
