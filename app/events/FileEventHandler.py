from os.path import getsize
from time import sleep
from abc import ABC, abstractclassmethod

from watchdog.events import RegexMatchingEventHandler

class FileEventHandler(RegexMatchingEventHandler, ABC):
    FILE_EXTS = [r".*"]

    def __init__(self):
        super().__init__(self.FILE_EXTS)

    def on_created(self, event):
        file_Size = -1
        
        while file_Size != getsize(event.src_path):
            file_Size = getsize(event.src_path)
            sleep(1)

        self.process(event)

    @property
    def regex(self):
        return self.FILE_EXTS

    @regex.setter
    def regex(self, FILE_EXTS):
        if type(FILE_EXTS) != list:
            raise TypeError("TypeError: {} is not of tpye list".format(FILE_EXTS))

        if len(FILE_EXTS) == 0:
            return
        
        self.FILE_EXTS = FILE_EXTS

    @abstractclassmethod
    def process(self, event):pass
