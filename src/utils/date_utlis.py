from datetime import datetime, timedelta, date
from typing import Generator


def get_previous_date() -> date:
    return (datetime.today() - timedelta(days=1)).date()


def get_current_date() -> date:
    return datetime.today().date()


def get_dates(start_date=date(2003, 1, 1), end_date=date.today()) -> Generator[date, None, None]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
