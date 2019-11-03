import time

from watchdog.observers import Observer
from .events.FileEventHandler import FileEventHandler

class FolderWatcher:

    def __init__(self, path):
        self.__path = path
        self.__event_handler = FileEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()
    
    def __schedule(self):
        self.__event_observer.schedule(self.__event_handler, self.__path, recursive=False)