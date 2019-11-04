from .FileEventHandler import FileEventHandler
from ..Emailer import Emailer
from app.app import APP_CONFIG
from json import load

class DefaultFileEventHandler(FileEventHandler):

    def __init__(self, FILE_EXTS=None):
        if FILE_EXTS is not None:
            self.regex = FILE_EXTS
        super().__init__()

    def process(self, event):

        msg_data = dict()

        try:
            with open(APP_CONFIG["EMAIL_CONFIG"]["MAIL_DATA_PATH"],'r') as msg_fp:
                msg_data = load(msg_fp)
        except KeyError as e:
            print("Unable to locate key: {}".format(e))
            # send email with error message?
            return
        except FileNotFoundError as e:
            print("Unable to file file: {}".format(e))
            return
        except IOError as e:
            print("Unable to read file as location: {}".format(e))
            return

        msg_data["attachment"] = APP_CONFIG["EMAIL_CONFIG"]["MAIL_DATA_PATH"]
        try:
            emailer = Emailer(APP_CONFIG["SMTP_CONFIG"], APP_CONFIG["EMAIL_CONFIG"], msg_data)
            emailer.send_mail()
        except KeyError as e:
            print("Unable to locate key: {}".format(e))
        except Exception as e:
            print("Emailer error: {}".format(e))
        
