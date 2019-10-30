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

    def setUp(self):
        try:
            del self.msg["attachment"]
        except KeyError:
            pass

    def test_set_message_given_plaintext_message_and_pdf_attachment(self):
        msg = self.msg
        msg["attachment"] = path.join(getcwd(), "test", "test_assets", "test.pdf")
        self.emailer.set_message(msg)
    
    def test_set_message_given_plaintext_message_and_incorrect_pdf_attachment_path(self):
        msg = self.msg
        msg["attachment"] = path.join(getcwd(), "test_assets", "test.pdf")
        
        self.assertRaises(FileNotFoundError, self.emailer.set_message,msg)

    def test_send_message_given_valid_mail_details(self):
        msg = self.msg
        msg['to'] = ''
        msg['from'] = ''
        msg["attachment"] = path.join(getcwd(), "test", "test_assets", "test.pdf")
        self.emailer.set_message(msg)
        self.emailer.send_mail()
        


if __name__ == '__main__':
    unittest.main()