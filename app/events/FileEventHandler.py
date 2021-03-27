from os.path import getsize
from time import sleep
from abc import ABC, abstractmethod
from re import compile, I
from ..Logger import Logger
from app import APP_CONFIG

from watchdog.events import RegexMatchingEventHandler


class FileEventHandler(RegexMatchingEventHandler, ABC):

    def __init__(self, FILE_EXTS = [r".*"]):
        self.logger = Logger(APP_CONFIG['LOGGING_CONFIG']['LOG_LOCATION'], loglevel=APP_CONFIG['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'], name=__name__)

        if not self.__is_list(FILE_EXTS):
            raise TypeError("TypeError: {} is of type {}, not list".format(FILE_EXTS, type(FILE_EXTS)))
        super().__init__(FILE_EXTS)

    def on_created(self, event):
        self.logger.log.info("Detected file {}".format(event.src_path))
        self.logger.log.info("Processing file: {}".format(event.src_path))

        file_Size = -1
        uploaded = False

        try:
            while file_Size != getsize(event.src_path):
                file_Size = getsize(event.src_path)
                sleep(1)
            uploaded = True
        except FileNotFoundError as e:
            self.logger.log.error(e.strerror)

        if uploaded:
            self.process(event)
            self.logger.log.info("Processed file: {}".format(event.src_path))
        else:
            self.logger.log.info("Unable to Process file: {}".format(event.src_path))

    @property
    def regexes(self):
        return self._regexes
    
    @regexes.setter
    def regexes(self, FILE_EXTS):
        if not self.__is_list(FILE_EXTS):
            raise TypeError("TypeError: {} is of type {}, not list".format(FILE_EXTS, type(FILE_EXTS)))

        if len(FILE_EXTS) == 0:
            return
        
        self._regexes = [compile(r, I) for r in FILE_EXTS]

    def __is_list(self, obj):
        return type(obj) == list
        
    @abstractmethod
    def process(self, event):pass
