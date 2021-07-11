import re

from app import APP_CONFIG
from app.Logger import Logger
from app.notifier.message.placeholders import MESSAGE_PLACEHOLDERS


class Message:

    def __init__(self, message_string, msg_data):
        self.logger = Logger(APP_CONFIG['LOGGING_CONFIG']['LOG_LOCATION'],
                             loglevel=APP_CONFIG['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'], name=__name__)
        self.__msg_data = msg_data
        self.__raw_message = message_string
        self.__enriched_message = self.enrich_message()  # add enrichment method call

    def enrich_message(self):
        return self.__replace_placeholder()

    def __get_placeholder(self, message_string):
        placeholder_match = re.compile(r"_{2}[a-zA-Z-]+_{2}").search(message_string)
        if placeholder_match:
            if placeholder_match.group(0) in self.__msg_data.keys():
                return placeholder_match.group(0)
            self.logger.log.debug("Invalid placeholder value {}".format(placeholder_match.group(0)))
        return None

    def __replace_placeholder(self):
        replaced_message = self.__raw_message
        placeholder = self.__get_placeholder(replaced_message)

        if not placeholder:
            self.logger.log.debug("No placeholder found in raw message")

        while placeholder:
            if callable(self.__msg_data[placeholder]):
                replaced_message = replaced_message.replace(placeholder, self.__msg_data[placeholder]())
            else:
                replaced_message = replaced_message.replace(placeholder, self.__msg_data[placeholder])

            placeholder = self.__get_placeholder(replaced_message)

        return replaced_message

    @property
    def message(self):
        return self.__enriched_message
