from datetime import datetime


def get_current_date():
    return datetime.today().strftime('%B %d, %Y')


MESSAGE_PLACEHOLDERS = {
    "__current-date__": get_current_date
}
