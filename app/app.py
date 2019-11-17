from config.config import APP_CONFIG
from app.FolderWatcher import FolderWatcher

def run():
    watcher = FolderWatcher(APP_CONFIG['WATCHER_CONFIG']['WATCH_PATH'])
    watcher.run()
