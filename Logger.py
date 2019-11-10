import logging

class Logger:

    def __init__(self, folder, name = __name__, loglevel=logging.INFO, loggingtype=1, format = "%(asctime)s:%(name)s:%(folder_name)s:%(loglevel)s:%(message)"):
        self.logging_type = loggingtype
        self.log_location = folder
        self.logging_type = loggingType

        self.logger = logging.getLogger(name)
        self.logger.setLevel(loglevel)

    @property
    def formatter(self):
        return self.formatter
    
    @formatter.setter
    def formatter(self, format):
        self.formatter = logging.Formatter(self.format)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.folder_name, self.log_level,self.logging_type, self.logging_type )


