from os.path import getsize
from time import sleep
from abc import ABC, abstractclassmethod
from re import compile, I

from watchdog.events import RegexMatchingEventHandler

class FileEventHandler(RegexMatchingEventHandler, ABC):

    def __init__(self, FILE_EXTS = [r".*"]):
        if not self.__is_list(FILE_EXTS):
            raise TypeError("TypeError: {} is of type {}, not list".format(FILE_EXTS, type(FILE_EXTS)))
        super().__init__(FILE_EXTS)

    def on_created(self, event):
        print("Detected file {}".format(event.src_path))
        file_Size = -1
        
        while file_Size != getsize(event.src_path):
            file_Size = getsize(event.src_path)
            sleep(1)
        print("Processing file: {}".format(event.src_path))
        self.process(event)
        print("Processed file: {}".format(event.src_path))

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
        
    @abstractclassmethod
    def process(self, event):pass
