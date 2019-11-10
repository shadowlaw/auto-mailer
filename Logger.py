import logging

class Logger:

    def __init__(self, folder, name = __name__, loglevel=logging.INFO, loggingtype=1, format = "%(asctime)s:%(name)s:%(folder_name)s:%(loglevel)s:%(message)"):
        self.logging_type = loggingtype
        self.log_location = folder
        self.logging_type = loggingType

        self.logger = logging.getLogger(name)
        self.logger.setLevel(loglevel)

    def set_handler(self, loggingtype):
        if loggingtype == 0:
            self.set_file_hendler()
        elif loggingtype ==  1:
            self.set_steam_handler()
        elif loggingtype == 2:
            self.set_steam_handler()
            self.set_file_hendler()

    @property
    def formatter(self):
        return self.formatter
    
    @formatter.setter
    def formatter(self, format):
        self.formatter = logging.Formatter(self.format)

    def set_steam_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self.logger.addHandler(stream_handler)

    def set_file_hendler(self):
        file_handler = logging.FileHandler(self.log_location)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.folder_name, self.log_level,self.logging_type, self.logging_type )


