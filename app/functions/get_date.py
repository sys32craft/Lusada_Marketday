from datetime import datetime


def get_date():

    current_date = datetime.now()

    phone_now = current_date

    return phone_now.date()