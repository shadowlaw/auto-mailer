import sys
from os import getcwd
from os import path
sys.path.append(getcwd())
import unittest
from app.Emailer import Emailer
from config.config import SMTP_CONFIG, EMAIL_CONFIG



class EmailerTest(unittest.TestCase):

    msg = dict()
    emailer = Emailer()

    @classmethod
    def setUpClass(cls):
        cls.msg['to'] = ''
        cls.msg['from'] = ''
        cls.msg['subject'] = 'Test mail'
        cls.msg['body'] = 'This is a test email'
        cls.emailer = Emailer(SMTP_CONFIG, EMAIL_CONFIG, cls.msg)

    def test_set_message_given_plaintext_message_and_pdf_attachment(self):
        self.msg["attachment"] = path.join(getcwd(),"test_assets", "test.pdf")
        self.emailer.set_message(self.msg)
        emailer_message = self.emailer.get_message()
        print(emailer_message)
        # TODO: Plain text email (failure)
        # TODO: email with attachment (failure)
        pass


if __name__ == '__main__':
    unittest.main()