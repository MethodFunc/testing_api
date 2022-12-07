import requests
from sqlalchemy.exc import OperationalError

from bin.tools import rename_gen, reformatting_json, reformat_forecast_dataframe
from database.connection import ScadaSessionLocal
from database.crud import get_scada_data
from .request_information import api_url

headers = {
    'accept': 'application/json',
}


def extract_data(rename, start_time: str, end_time: str, logger):
    try:
        with ScadaSessionLocal() as db:
            scada = get_scada_data(db, rename, start_time, end_time)
    except OperationalError:
        raise logger.warning(f'데이터베이스 서버에 접속 할 수 없습니다.')

    if len(scada) == 0:
        return 0

    else:
        json_data = reformatting_json(scada)
        logger.info(f'{rename} - {start_time} Data\n{json_data}')

        return json_data.to_dict()


def forecast_api(generator: str, start_time: str, end_time: str, logger):
    rename = rename_gen(generator)

    json_data = extract_data(rename, start_time, end_time, logger)
    if json_data != 0:
        params = {
            'generator': rename,
        }
        response = requests.post(api_url, params=params, headers=headers,
                                 json=json_data)

        result_dataframe = reformat_forecast_dataframe(response.json())

        return result_dataframe
    else:
        logger.warning('해당 날의 데이터가 없거나, 날짜를 잘못 입력하였습니다.')
