import warnings

from bin.datetools import date_function
from bin.forecast import ForecastDate, ForecastRange
from setting import settings, load_logger

warnings.filterwarnings('ignore')
GEN_NAME = [f'DB{i:02d}' for i in range(1, 16)]


def main():
    args = settings()
    logger = load_logger()
    logger.info('Process Start')

    if args['method'] == 'date':
        date = str(args['date'])
        start_date, end_date = date_function(date)
        forecast = ForecastDate()
        forecast.forecast(logger=logger, args=args, start_date=start_date, end_date=end_date)

    if args['method'] == 'range':
        start_date = str(args['start_date'])
        end_date = str(args['end_date'])
        date_list = date_function(start_date, end_date)
        forecast = ForecastRange()
        forecast.forecast(logger=logger, args=args, start_date=date_list, end_date=None)

    logger.info('Process Done')


if __name__ == '__main__':
    main()
