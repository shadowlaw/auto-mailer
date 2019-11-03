from .FileEventHandler import FileEventHandler
from ..Emailer import Emailer
from app.app import APP_CONFIG

class DefaultFileEventHandler(FileEventHandler):

    def __init__(self, FILE_EXTS=None):
        if FILE_EXTS is not None:
            self.regex = FILE_EXTS
        super().__init__()

    def process(self):
        pass
