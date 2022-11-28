import yaml
import os
import logging.config


def settings():
    with open('./setting.yaml') as f:
        films = yaml.load(f, Loader=yaml.FullLoader)

    return films


def load_logger():
    logging_config_path = 'logging.yaml'
    if os.path.exists(logging_config_path):
        with open(logging_config_path, 'rt') as f:
            logging_config = yaml.load(f, Loader=yaml.FullLoader)
            logging.config.dictConfig(logging_config)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.getLogger(__name__)

    return logging
