import logging

file_formatter = logging.Formatter("%(asctime)s:%(name)s:%(folder_name)s:%(loglevel)s:%(message)")

file = logging.FileHandler('test.log')
file.setFormatter(file_formatter)

class Logger:

    def __init__(self, folder, name = __name__, loglevel=logging.INFO, loggingtype=1):
        self.name = name
        self.folder_name = folder
        self.log_level = loglevel
        self.logging_type = loggingtype

        this_log = logging.getLogger(name)
        this_log.addHandler(file)

    @property
    def __name__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.folder_name, self.log_level,self.logging_type, self.message, self.logging_type )


emp_1 = Logger('John','testfile','Debug','Pizza delivered','1')
emp_2 = Logger('Corey','testfile','Warning','Cheese','1')
