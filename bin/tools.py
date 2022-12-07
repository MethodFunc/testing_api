from datetime import timedelta

import pandas as pd


def reformatting_json(data):
    dataframe = pd.DataFrame(data)
    dataframe.rename(columns={
        'record_date': 'ds',
        'wind_speed': 'WS',
        'wind_direction': 'WD',
        'active_power': 'y'
    }, inplace=True)

    dataframe['ds'] = dataframe['ds'].astype('str')

    return dataframe


def reformat_forecast_dataframe(json_string: str):
    dataframe = pd.DataFrame(json_string)
    dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])
    dataframe['datetime'] = dataframe['datetime'].apply(lambda x: x + timedelta(hours=9))
    dataframe['datetime'] = dataframe['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

    return dataframe


def rename_gen(generator_name):
    """
    :param generator_name:
    :return:
    """
    rename_generator = {
        'DB01': 'DB_HJ01',
        'DB02': 'DB_HJ02',
        'DB03': 'DB_HJ03',
        'DB04': 'DB_HJ04',
        'DB05': 'DB_HJ05',
        'DB06': 'DB_HJ06',
        'DB07': 'DB_HJ07',
        'DB08': 'DB_HJ08',
        'DB09': 'DB_HJ09',
        'DB10': 'DB_HJ10',
        'DB11': 'DB_HJ11',
        'DB12': 'DB_HJ12',
        'DB13': 'DB_HJ13',
        'DB14': 'DB_HJ14',
        'DB15': 'DB_HJ15',
        'GN02': 'GN_US01',
        'GS07': 'GS_HJ01',
        'GS08': 'GS_HJ02',
        'GS09': 'GS_HJ03',
        'GS10': 'GS_HJ04',
        'GS11': 'GS_HJ05',
        'GS12': 'GS_HJ06',
        'GS13': 'GS_HJ07',
        'GS01': 'GS_HS01',
        'GS02': 'GS_US01',
        'GS03': 'GS_HS03',
        'GS04': 'GS_US02',
        'GS05': 'GS_US03',
        'HW17': 'HW_DS01',
        'HW16': 'HW_HD01',
        'HW05': 'HW_HJ01',
        'HW04': 'HW_US01',
        'HW06': 'HW_VT01',
        'HW10': 'HW_VT04',
        'HW11': 'HW_VT05',
        'HW13': 'HW_VT07',
        'HW14': 'HW_VT08',
        'HW15': 'HW_VT09',
        'SC01': 'SC_VT01',
        'SC02': 'SC_VT02'}

    if generator_name.islower:
        generator = generator_name.upper()

    try:
        rename_generator[generator]
    except KeyError:
        raise KeyError(f'{generator} is not support')

    gen_ = rename_generator.get(generator)

    if gen_ is None:
        gen_ = generator

    return gen_
