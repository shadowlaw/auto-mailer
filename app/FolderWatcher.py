import time

from watchdog.observers import Observer
from .events.DefaultFileEventHandler import DefaultFileEventHandler
from app.app import APP_CONFIG

class FolderWatcher:

    def __init__(self, path):
        self.__path = path
        self.__event_handler = DefaultFileEventHandler(APP_CONFIG["WATCHER_CONFIG"]["WATCH_EXTS"])
        self.__event_observer = Observer()

    def run(self):
        self.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        print("Watcher Starting")
        self.__schedule()
        self.__event_observer.start()
        print("Watcher Started")

    def stop(self):
        print("\nWatcher Stopping")
        self.__event_observer.stop()
        self.__event_observer.join()
        print("Watcher Stopped")
    
    def __schedule(self):
        self.__event_observer.schedule(self.__event_handler, self.__path, recursive=False)