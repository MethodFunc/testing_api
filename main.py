import warnings

from sqlalchemy.exc import ProgrammingError

from bin.datetools import date_function
from bin.extract_api import forecast_api
from setting import settings, load_logger

warnings.filterwarnings('ignore')
GEN_NAME = [f'DB{i:02d}' for i in range(1, 16)]


def main():
    if args['method'] == 'default':
        start_date, end_date = date_function(args)

    elif args['method'] == 'date':
        date = str(args['date'])
        start_date, end_date = date_function(args, date)

    else:
        raise logger.warning('It\'s only support [default, date], check your method')

    if args['generator'] == 'all':
        for gen in GEN_NAME:
            logger.info(forecast_api(gen, start_date, end_date, logger))

    else:
        try:
            logger.info(forecast_api(args['generator'], start_date, end_date, logger))
        except ProgrammingError:
            raise logger.warning('잘못 된 데이터를 입력했을 수도 있습니다.\n이 문구가 보이면 관리자에게 연락해주세요.')


if __name__ == '__main__':
    args = settings()
    logger = load_logger()

    main()
