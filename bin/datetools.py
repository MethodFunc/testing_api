import re
from datetime import datetime, timedelta
from typing import Optional


def convert_date(date):
    pattern = r'[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·\s]'

    date_pattern = {
        8: '%Y%m%d',
        10: '%Y%m%d%H',
        12: '%Y%m%d%H%M',
        14: '%Y%m%d%H%M%S',
    }

    date = re.sub(pattern, '', date)

    return date_pattern[len(date)]


def date_function(date: Optional[str] = None, end_date: Optional[str] = None):
    dateformat = '%Y-%m-%d'
    if end_date is not None:
        start_pattern = convert_date(date)
        end_pattern = convert_date(end_date)

        start_date = datetime.strptime(date, start_pattern) - timedelta(days=1)
        end_date = datetime.strptime(end_date, end_pattern)

        date_range = (end_date - start_date).days

        return [(start_date + timedelta(days=i)).strftime(dateformat) for i in range(date_range)]

    pattern = convert_date(date)
    date = datetime.strptime(date, pattern)
    start_date = (date - timedelta(days=1)).strftime(dateformat)
    end_date = date.strftime(dateformat)

    return start_date, end_date
