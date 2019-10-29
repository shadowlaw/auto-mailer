import smtplib
import email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Emailer:
    __smtpObj = smtplib.SMTP()
    __user_details = dict()
    __message = MIMEMultipart()

    def __init__(self, smtp_config=dict(), user_details=dict(), msg=dict()):
        self.__smtpObj = smtplib.SMTP(smtp_config['SMTP_SERVER'], smtp_config['SMTP_PORT'])
        self.__user_details = user_details
        self.set_message(msg)

    def set_user_details(self, user_details):
        self.__user_details = user_details

    def get_user_details(self):
        return self.__user_details

    def test_connection(self):
        return self.__smtpObj.ehlo()

    def set_message(self, msg):
        self.__message["From"] = msg['from']
        self.__message["To"] = msg['to']
        self.__message["Subject"] = msg['subject']
        self.__message.attach(MIMEText(msg['body'], "plain"))

        try:
            with open(msg['attachment'], "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
        except FileNotFoundError:
            print("File does not exist")
        except IOError:
            print("I/O Error")
        except KeyError:
            pass
        except Exception as e:
            print(e)

        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {msg['attachment']}",
        )

        # Add attachment to message and convert message to string
        self.__message.attach(part)
    
    def get_message(self):
        return self.__message
