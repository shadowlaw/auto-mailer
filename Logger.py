import logging

class Logger:

    def __init__(self, folder, name = __name__, loglevel=logging.INFO, loggingtype=1, format = "%(levelname)s:%(asctime)s:%(name)s:%(funcName)s:%(message)s"):
        self.logging_type = loggingtype
        self.log_location = folder
        self.logging_type = loggingtype
        self.format = format
        self.name = name
        self.loglevel = loglevel

        self.__log = logging.getLogger(name)
        self.__log.setLevel(loglevel)
        self.formatter = format
        self.set_handler(loggingtype)

    def set_handler(self, loggingtype):
        if loggingtype == 0:
            self.set_file_hendler()
        elif loggingtype ==  1:
            self.set_steam_handler()
        elif loggingtype == 2:
            self.set_steam_handler()
            self.set_file_hendler()

    @property
    def log(self):
        return self.__log
        
    @property
    def formatter(self):
        return self.formatter_obj
    
    @formatter.setter
    def formatter(self, format):
        self.formatter_obj = logging.Formatter(self.format)

    def set_steam_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self.__log.addHandler(stream_handler)

    def set_file_hendler(self):
        file_handler = logging.FileHandler(self.log_location)
        file_handler.setFormatter(self.formatter)
        self.__log.addHandler(file_handler)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.log_location, self.loglevel,self.logging_type, self.logging_type )


