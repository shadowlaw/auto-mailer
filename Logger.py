import logging

class Logger:

    def __init__(self, name, folder, message_logged, loglevel=INFO, loggingtype=1):
        self.name = name
        self.folder_name = folder
        self.log_level = loglevel
        self.logging_type = loggingtype
        self.message = message_logged

        logging.getLogger(format = "%(asctime)s:%(name)s:%(folder_name)s:%(loglevel)s:%(message)s")

    def __name__(self):
        return logging.basicConfig(format="%(name)")

