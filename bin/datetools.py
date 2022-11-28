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


def date_function(args, date: Optional[str] = None):
    dateformat = '%Y-%m-%d'
    if args['method'] == 'default':
        current_date = datetime.now()
        year = current_date.year
        month = current_date.month
        day = current_date.day

        start_date = datetime(year=year, month=month, day=day - 1).strftime(dateformat)
        end_date = datetime(year=year, month=month, day=day).strftime(dateformat)
    if args['method'] == 'date':
        pattern = convert_date(date)
        date = datetime.strptime(date, pattern)
        start_date = date.strftime(dateformat)
        end_date = (date + timedelta(days=1)).strftime(dateformat)

    return start_date, end_date
