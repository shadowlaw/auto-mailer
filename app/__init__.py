from os import path, getcwd, mkdir
from .utils import yml
import logging

user_conf = yml.read_yaml_file(
        path.normpath(
            path.join(getcwd(), "app/config/user_conf.yaml")
        )
    )

sys_conf = yml.read_yaml_file(
        path.normpath(
            path.join(getcwd(), "app/config/system_conf.yaml")
        )
    )

sys_conf['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'] = getattr(logging, sys_conf['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'].upper(), 20)

if not path.exists(sys_conf['LOGGING_CONFIG']['LOG_LOCATION']):
    mkdir(path.dirname(sys_conf['LOGGING_CONFIG']['LOG_LOCATION']))
    with open(sys_conf['LOGGING_CONFIG']['LOG_LOCATION'], 'w'):
        pass


# Adding properties to config dictionary
APP_CONFIG = user_conf
APP_CONFIG.update(sys_conf)
