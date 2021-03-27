import time

from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver
from .events.EmailProcessor import EmailProcessor
from app.Logger import Logger
from app import APP_CONFIG
from os.path import isfile, exists
from sys import exit


class FolderWatcher:

    def __init__(self, event_groups):
        self.logger = Logger(APP_CONFIG['LOGGING_CONFIG']['LOG_LOCATION'], loglevel=APP_CONFIG['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'], name=__name__)
        self.logger.log.info("Watcher initializing")
        self.__event_handler_groups = self.__create_event_handlers(event_groups)
        try:
            self.__event_observer = self.__get_observer(APP_CONFIG['WATCHER_CONFIG']['DEFAULT_OBSERVER_TYPE'])
        except KeyError as e:
            self.logger.log.debug("Optional value {} not set.".format(str(e)))
            self.logger.log.debug('Defaulting to native observer')
            self.__event_observer = Observer()

        self.logger.log.info("Watcher initialized")

    def run(self):
        self.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.logger.log.info("Watcher Starting")
        self.__schedule()
        self.__event_observer.start()
        self.logger.log.info("Watcher Started")

    def stop(self):
        self.logger.log.info("Watcher Stopping")
        self.__event_observer.stop()
        self.__event_observer.join()
        self.logger.log.info("Watcher Stopped")
    
    def __schedule(self):

        if len(self.__event_handler_groups) < 1:
            self.logger.log.critical("Unable to schedule observer. No valid event groups have been set.")
            exit()

        for event_handler_group in self.__event_handler_groups:
            self.__event_observer.schedule(event_handler_group['event_handler'], event_handler_group['watch_path'], recursive=False)

    def __create_event_handlers(self, event_groups):
        event_handlers = []

        if type(event_groups) is not list:
            self.logger.log.critical("Unable to schedule observer. At least 1 event group should be set")
            exit()

        for event_group in event_groups:

            if not self.__is_event_group_valid(event_group):
                continue
            if not isfile(event_group['MAIL_DATA_PATH']):
                self.logger.log.debug("Unable to create event handler. Could not find email template path: {}".format(
                    event_group['MAIL_DATA_PATH']))
                continue
            if not exists(event_group['WATCH_PATH']):
                self.logger.log.debug(
                    "Unable to create event handler. Could not find watch path: {}".format(event_group['WATCH_PATH']))
                continue

            event_handlers.append(
                {
                    "event_handler": EmailProcessor(event_group['MAIL_DATA_PATH'], event_group['WATCH_EXTS']),
                    "watch_path": event_group['WATCH_PATH']
                }
            )

        return event_handlers

    def __is_event_group_valid(self, event_group):
        try:
            return type(event_group['WATCH_EXTS']) is list and type(event_group['WATCH_PATH']) is str and \
                   type(event_group['MAIL_DATA_PATH']) is str
        except TypeError:
            self.logger.log.debug("Event group cannot be empty")
            return False
        except KeyError as e:
            self.logger.log.debug("Unable to find field {}".format(e.args[0]))
            return False

    def __get_observer(self, option):
        if option is not None and option.lower() == 'polling':
            return PollingObserver(timeout=3)
        elif option is not None and option.lower() == 'native':
            return Observer()
        else:
            self.logger.log.debug('Unknown observer option {} specified'.format(option))

        return Observer()
