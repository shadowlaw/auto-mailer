from os import getcwd, path
import logging

from app.utils import file_manager


def __getUserConfig():
    try:
        return __read_config_file(path.join(getcwd(), "app/config/user_conf.yaml"))
    except FileNotFoundError as e:
        file_manager.copy("app/data/defaults/user_conf.yaml", "app/config/user_conf.yaml")
        return __read_config_file(path.join(getcwd(), "app/config/user_conf.yaml"))


def __getSystemConfig():
    try:
        sys_config = __read_config_file(path.join(getcwd(), "app/config/system_conf.yaml"))
    except FileNotFoundError as e:
        file_manager.copy("app/data/defaults/system_conf.yaml", "app/config/system_conf.yaml")
        sys_config = __read_config_file(path.join(getcwd(), "app/config/system_conf.yaml"))

    __prepareLogging(sys_config)
    return sys_config


def __prepareLogging(sys_conf):
    sys_conf['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'] = getattr(logging, sys_conf['LOGGING_CONFIG'][
        'DEFAULT_LOG_LEVEL'].upper(), 20)

    file_manager.create_file(sys_conf['LOGGING_CONFIG']['LOG_LOCATION'])


def __read_config_file(config_path):
    return file_manager.read_yaml_file(path.normpath(config_path))


def getAppConfig():
    app_config = __getUserConfig()
    app_config.update(__getSystemConfig())
    return app_config
