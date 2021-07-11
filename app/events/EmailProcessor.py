from .FileEventHandler import FileEventHandler
from app.notifier.Emailer import Emailer
from app import APP_CONFIG
from ..Logger import Logger
from ..utils.file_manager import read_json_file
from os.path import basename
from app.notifier.message.placeholders import MESSAGE_PLACEHOLDERS


class EmailProcessor(FileEventHandler):

    def __init__(self, email_data_location, FILE_EXTS=None):
        self.logger = Logger(APP_CONFIG['LOGGING_CONFIG']['LOG_LOCATION'], loglevel=APP_CONFIG['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'], name=__name__)
        self.logger.log.info("DefaultFileHandler initializing")
        
        if FILE_EXTS is not None:
            super().__init__(FILE_EXTS)
        else:
            super().__init__()

        self.__msg_data = MESSAGE_PLACEHOLDERS

        self.email_data_location = email_data_location

        self.logger.log.info("DefaultFileHandler initialized")

    def process(self, event):
        try:
            self.__msg_data.update(read_json_file(self.email_data_location))
        except KeyError as e:
            self.logger.log.error("Unable to locate key: {}".format(e))
            # send email with error message?
            return
        except FileNotFoundError as e:
            self.logger.log.error("Unable to file file: {}".format(e))
            return
        except IOError as e:
            self.logger.log.error("Unable to read file as location: {}".format(e))
            return

        self.__msg_data["attachment"] = event.src_path
        self.__msg_data["__triggering-file-name__"] = basename(event.src_path)
        try:
            emailer = Emailer(APP_CONFIG["SMTP_CONFIG"], APP_CONFIG["EMAIL_CONFIG"], self.__msg_data)
            emailer.send_mail()
        except KeyError as e:
            self.logger.log.error("Unable to locate key: {}".format(e))
        except Exception as e:
            self.logger.log.error("Emailer error: {}".format(e))
