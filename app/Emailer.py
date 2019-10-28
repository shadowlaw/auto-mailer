import smtplib


class Emailer:
    __smtpObj = smtplib.SMTP()
    __user_details = dict()
    __msg = dict()

    def __init__(self, smtp_config, user_details, msg):
        self.__smtpObj = smtplib.SMTP(smtp_config['SMTP_SERVER'], smtp_config['SMTP_PORT'])
        self.__user_details = user_details

    def set_user_details(self, user_details):
        self.__user_details = user_details

    def set_msg(self, msg):
        self.__msg = msg

    def get_user_details(self):
        return self.__user_details

    def test_connection(self):
        return self.__smtpObj.ehlo()
