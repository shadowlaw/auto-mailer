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

    @abstractclassmethod
    def process(self, event):pass
