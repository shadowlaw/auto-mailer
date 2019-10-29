import unittest
from app.Emailer import Emailer
from config.config import SMTP_CONFIG, EMAIL_CONFIG
from os import getcwd
from os import path


class EmailerTest(unittest.TestCase):

    msg = dict()
    emailer = Emailer()

    @classmethod
    def setUpClass(cls, self):
        self.msg['to'] = ''
        self.msg['from'] = ''
        self.msg['subject'] = 'Test mail'
        self.msg['body'] = 'This is a test email'
        self.emailer = Emailer(SMTP_CONFIG, EMAIL_CONFIG, self.msg)

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