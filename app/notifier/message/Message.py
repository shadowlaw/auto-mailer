import re
from datetime import datetime

from app import APP_CONFIG
from app.Logger import Logger
from app.notifier.message.placeholders import MESSAGE_PLACEHOLDERS


class Message:

    def __init__(self, message_string):
        self.logger = Logger(APP_CONFIG['LOGGING_CONFIG']['LOG_LOCATION'],
                             loglevel=APP_CONFIG['LOGGING_CONFIG']['DEFAULT_LOG_LEVEL'], name=__name__)
        self.__raw_message = message_string
        self.__enriched_message = self.enrich_message()  # add enrichment method call

    def enrich_message(self):
        return self.__replace_placeholder()

    def __get_placeholder(self):
        placeholder_match = re.compile(r"_{2}[a-zA-Z-]+_{2}").search(self.__raw_message)
        if placeholder_match:
            if placeholder_match.group(0) in MESSAGE_PLACEHOLDERS.keys():
                return placeholder_match.group(0)
            self.logger.log.debug("Invalid placeholder value {}".format(placeholder_match.group(0)))
        else:
            self.logger.log.debug("No placeholder found in raw message")
        return None

    def __replace_placeholder(self):
        placeholder = self.__get_placeholder()
        if placeholder:
            return self.__raw_message.replace(placeholder, MESSAGE_PLACEHOLDERS[placeholder]())
        return self.__raw_message

    @property
    def message(self):
        return self.__enriched_message
