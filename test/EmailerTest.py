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
        

    def setUp(self):
        self.emailer = Emailer(SMTP_CONFIG, EMAIL_CONFIG, dict())

    def tearDown(self):
        try:
            del self.msg["attachment"]
        except KeyError:
            pass

    def test_set_message_given_plaintext_message_and_pdf_attachment(self):
        msg = self.msg
        emailer = self.emailer
        msg["attachment"] = path.join(getcwd(), "test", "test_assets", "test.pdf")
        emailer.set_message(msg)
    
    def test_set_message_given_plaintext_message_and_incorrect_pdf_attachment_path(self):
        msg = self.msg
        emailer = self.emailer
        msg["attachment"] = path.join(getcwd(), "test_assets", "test.pdf")
        
        self.assertRaises(FileNotFoundError, emailer.set_message, msg)

    def test_send_message_given_valid_mail_details(self):
        msg = self.msg
        emailer = self.emailer
        msg['to'] = "shadowdev03@gmail.com"
        msg['from'] = "shadowdev03@gmail.com"
        msg["body"] = "This is a test email"
        msg["attachment"] = path.join(getcwd(), "test", "test_assets", "test.pdf")
        emailer.set_message(msg)
        emailer.send_mail()


if __name__ == '__main__':
    unittest.main()
