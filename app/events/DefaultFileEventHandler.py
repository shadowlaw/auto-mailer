from .FileEventHandler import FileEventHandler
from ..Emailer import Emailer
from app.app import APP_CONFIG
from json import load
from ..Logger import Logger
from config.config import LOGGING_CONFIG

class DefaultFileEventHandler(FileEventHandler):

    def __init__(self, FILE_EXTS=None):
        self.logger = Logger(LOGGING_CONFIG['LOG_LOCATION'])
        self.logger.log.info("DefaultFileHandler initializing")
        
        if FILE_EXTS is not None:
            super().__init__(FILE_EXTS)
        else:
            super().__init__()

        self.logger.log.info("DefaultFileHandler initialized")

    def process(self, event):

        msg_data = dict()

        try:
            with open(APP_CONFIG["EMAIL_CONFIG"]["MAIL_DATA_PATH"],'r') as msg_fp:
                msg_data = load(msg_fp)
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

        msg_data["attachment"] = event.src_path
        try:
            emailer = Emailer(APP_CONFIG["SMTP_CONFIG"], APP_CONFIG["EMAIL_CONFIG"], msg_data)
            emailer.send_mail()
            del emailer
            del msg_data
        except KeyError as e:
            self.logger.log.error("Unable to locate key: {}".format(e))
        except Exception as e:
            self.logger.log.error("Emailer error: {}".format(e))
        
