from app import APP_CONFIG
from app.FolderWatcher import FolderWatcher


def run():
    watcher = FolderWatcher(APP_CONFIG['WATCHER_CONFIG']['EVENT_GROUPS'])
    watcher.run()
