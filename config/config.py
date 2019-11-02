from os import path, getcwd

# FILE CONFIG
BASE_PATH = getcwd()
WATCH_PATH = path.join(BASE_PATH, 'dev')

# LOGGING CONFIG
LOG_LOCATION = path.join(BASE_PATH, 'dev', 'logs')
DEFAULT_LOG_LEVEL = 'INFO'

# SMTP SERVER CONFIG
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465  # SSL Port

# EMAIL CONFIG
EMAIL_ADDRESS = ''
PASSWORD = ''

# Adding properties to config dictionary
APP_CONFIG = dict()
WATCHER_CONFIG = dict()
LOGGING_CONFIG = dict()
SMTP_CONFIG = dict()
EMAIL_CONFIG = dict()

APP_CONFIG['WATCHER_CONFIG'] = WATCHER_CONFIG
APP_CONFIG['LOGGING_CONFIG'] = LOGGING_CONFIG
APP_CONFIG['SMTP_CONFIG'] = SMTP_CONFIG
APP_CONFIG['EMAIL_CONFIG'] = EMAIL_CONFIG

WATCHER_CONFIG['WATCH_PATH'] = WATCH_PATH

LOGGING_CONFIG['LOG_LOCATION'] = LOG_LOCATION
LOGGING_CONFIG['DEFAULT_LOG_LEVEL'] = DEFAULT_LOG_LEVEL

SMTP_CONFIG['SMTP_SERVER'] = SMTP_SERVER
SMTP_CONFIG['SMTP_PORT'] = SMTP_PORT

EMAIL_CONFIG['EMAIL_ADDRESS'] = EMAIL_ADDRESS
EMAIL_CONFIG['PASSWORD'] = PASSWORD
