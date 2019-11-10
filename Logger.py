import logging

class Logger:

    def __init__(self, folder, name = __name__, loglevel=logging.INFO, loggingtype=1, format = "%(asctime)s:%(name)s:%(folder_name)s:%(loglevel)s:%(message)"):
        self.logging_type = loggingtype

        this_log = logging.getLogger(name)
        this_log.addHandler(file)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.folder_name, self.log_level,self.logging_type, self.logging_type )


emp_1 = Logger('John','testfile','Debug','Pizza delivered','1')
emp_2 = Logger('Corey','testfile','Warning','Cheese','1')
