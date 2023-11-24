from datetime import datetime
import datetime as dt
import pytz


def current_datetime():
    return dt.datetime.now()


def current_datetime_with_timezone():
    return append_timezone(current_datetime())


def append_timezone(target, timezone: str = 'Asia/Bangkok'):
    return target.astimezone(pytz.timezone(timezone))
