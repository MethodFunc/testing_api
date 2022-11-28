import requests
from sqlalchemy.exc import OperationalError

from bin.tools import rename_gen, reformatting_json, reformat_forecast_dataframe
from database.connection import ScadaSessionLocal
from database.crud import get_scada_data

api_url = r'http://127.0.0.1:8123/forecast/json_query'
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
        raise logger.warning('해당 날의 데이터가 없거나, 날짜를 잘못 입력하였습니다.')

    json_data = reformatting_json(scada)

    return json_data


def forecast_api(generator: str, start_time: str, end_time: str, logger):
    rename = rename_gen(generator)
    logger.info(f'{rename} Forcast start')

    json_data = extract_data(rename, start_time, end_time, logger)

    params = {
        'generator': rename,
    }
    response = requests.post(api_url, params=params, headers=headers,
                             json=json_data)

    result_dataframe = reformat_forecast_dataframe(response.json())

    return result_dataframe
