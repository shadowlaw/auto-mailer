import smtplib

from os.path import basename
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.notifier.message.Message import Message


class Emailer:

    def __init__(self, smtp_config=dict(), user_details=dict(), msg=dict()):
        if bool(smtp_config):
            self.__smtpObj = smtp_config
        if bool(user_details):
            self.__user_details = user_details
        if bool(msg):

            msg['body'] = Message(msg['body'], msg)
            self.set_message(msg)

    def set_user_details(self, user_details):
        self.__user_details = user_details

    def get_user_details(self):
        return self.__user_details

    def test_connection(self):
        return self.__smtpObj.ehlo()

    def set_message(self, msg):
        if not bool(self.get_user_details()) or not bool(msg):
            return
        
        self.__sender = msg['from']
        if(type(msg['to']) is list):
            msg['to'] = ', '.join(msg['to'])
        self.__reciever = msg['to']
        self.__message = MIMEMultipart()
        self.__message["From"] = self.__sender
        self.__message["To"] = self.__reciever
        self.__message["Subject"] = msg['subject']
        self.__message.attach(MIMEText(msg['body'].message, "plain"))

        try:
            with open(msg['attachment'], "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
        except FileNotFoundError as e:
            print("File does not exist: {}".format(e))
            raise e
        except IOError as e:
            print("I/O Error {}".format(e))
            raise e
        except KeyError as e:
            print("Error finding key {}".format(e))
            return
        except Exception as e:
            print("General error {}".format(e))
            raise e

        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {basename(msg['attachment'])}",
        )

        # Add attachment to message and convert message to string
        self.__message.attach(part)
    
    def get_message(self):
        return self.__message

    def send_mail(self):
        timeout = 60
        try:
            if self.__smtpObj['SMTP_SSL']:
                server = smtplib.SMTP_SSL(self.__smtpObj["SMTP_SERVER"], self.__smtpObj["SMTP_PORT"], timeout=timeout)
            else:
                server = smtplib.SMTP(self.__smtpObj["SMTP_SERVER"], self.__smtpObj["SMTP_PORT"], timeout=timeout)
        except KeyError:
            server = smtplib.SMTP(self.__smtpObj["SMTP_SERVER"], self.__smtpObj["SMTP_PORT"])
        server.login(self.__user_details["EMAIL_ADDRESS"], self.__user_details["PASSWORD"])
        server.sendmail(self.__sender, self.__reciever, self.__message.as_string())
        server.close()
