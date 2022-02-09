from datetime import datetime, timedelta


def get_previous_date():
    return (datetime.today() - timedelta(days=1)).date()
