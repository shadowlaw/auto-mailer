import logging

class Logger(logging):

    def __init__(self, name, folder, loglevel=INFO, loggingtype=1):
        self.filename = name
        self.folder_name = folder
        self.log_level = loglevel
        self.logging_type = loggingtype

    def logged_type(self):
        while logging_type == 1:
            logging.basicConfig(filename ='{}'.format(self.filename))
            if logging_type != 1:


