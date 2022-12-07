from .extract_api import forecast_api
from typing import Optional, List
from sqlalchemy.exc import ProgrammingError

ERROR_MESSAGE = '잘못 된 데이터를 입력했을 수도 있습니다.\n이 문구가 보이면 관리자에게 연락해주세요.'


class ForecastBase:
    @staticmethod
    def run_api(logger, generator, start_date: str, end_date: str):
        result = forecast_api(generator, start_date, end_date, logger)
        if result is None:
            ...
        else:
            logger.info(f'{generator} - {end_date} Forecast\n{result}')

    def forecast(self, logger, args, start_date, end_date):
        ...


class ForecastDate(ForecastBase):
    def forecast(self, logger, args: dict, start_date: str, end_date: str):
        if args['generator'] == 'all':
            generator_list = [f'DB{i:02d}' for i in range(1, 16)]
            for gen in generator_list:
                try:
                    self.run_api(logger, gen, start_date, end_date)
                except ProgrammingError:
                    raise logger.warning(ERROR_MESSAGE)
        else:
            try:
                self.run_api(logger, args['generator'], start_date, end_date)
            except ProgrammingError:
                raise logger.warning(ERROR_MESSAGE)


class ForecastRange(ForecastBase):
    def forecast(self, logger, args: dict, start_date: List, end_date: Optional[str] = None):
        generator_list = [f'DB{i:02d}' for i in range(1, 16)]
        for i in range(len(start_date) - 1):
            start = start_date[i]
            end = start_date[i + 1]
            if args['generator'] == 'all':
                for gen in generator_list:
                    try:
                        self.run_api(logger, gen, start, end)
                    except ProgrammingError:
                        raise logger.warning(ERROR_MESSAGE)
            else:
                try:
                    self.run_api(logger, args['generator'], start, end)
                except ProgrammingError:
                    raise logger.warning(ERROR_MESSAGE)
