from os.path import getsize
from time import sleep

from watchdog.events import RegexMatchingEventHandler

class FileEventHandler(RegexMatchingEventHandler):
    FILE_EXTS = [r".*\d{4,4}\-\d{2,2}\-\d{2,2}\-[A-Za-z]*\.pdf$"]

    def __init__(self):
        super().__init__(self.FILE_EXTS)

    def on_created(self, event):
        file_Size = -1
        
        while file_Size != getsize(event.src_path):
            file_Size = getsize(event.src_path)
            sleep(1)

        self.process(event)

    def process(self, event):
        print(event.src_path)
