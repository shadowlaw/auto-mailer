from os.path import getsize
from time import sleep
from abc import ABC, abstractclassmethod

from watchdog.events import RegexMatchingEventHandler

class FileEventHandler(RegexMatchingEventHandler, ABC):

    def __init__(self, FILE_EXTS = [r".*"]):
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
    def regex(self):
        return self.FILE_EXTS

    @regex.setter
    def regex(self, FILE_EXTS):
        if type(FILE_EXTS) != list:
            raise TypeError("TypeError: {} is of type {}, not list".format(FILE_EXTS, type(FILE_EXTS)))

        if len(FILE_EXTS) == 0:
            return
        
        self.FILE_EXTS = FILE_EXTS

    @abstractclassmethod
    def process(self, event):pass
