import time

from watchdog.observers import Observer
from .events.DefaultFileEventHandler import DefaultFileEventHandler
from app.app import APP_CONFIG
from app.Logger import Logger
from config.config import LOGGING_CONFIG

class FolderWatcher:

    def __init__(self, path):
        self.logger = Logger(LOGGING_CONFIG['LOG_LOCATION'])
        self.logger.log.info("Watcher initialized")
        self.__path = path
        self.__event_handler = DefaultFileEventHandler(APP_CONFIG["WATCHER_CONFIG"]["WATCH_EXTS"])
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
        self.__event_observer.schedule(self.__event_handler, self.__path, recursive=False)