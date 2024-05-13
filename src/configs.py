import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
config_name = os.environ['APP_ENV']


class AppConfig:
    APP_ENV = ...
    RUN_PATH = os.path.dirname(os.path.dirname(__file__))
    PROJECT_DIR = RUN_PATH

    LOGS_DIR = Path(PROJECT_DIR, 'logs')
    LOG_NAME = APP_ENV

    API_AUTH_TOKEN = os.environ['API_AUTH_TOKEN']


class DevelopmentAppConfig(AppConfig):
    def __init__(self):
        super().__init__()

    DEBUG = True
    TESTING = True


class TestAppConfig(AppConfig):
    def __init__(self):
        super().__init__()

    DEBUG = True
    TESTING = True


class ProductionAppConfig(AppConfig):
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    LOG_NAME = 'prod'


def get_predefined_config(config_name: str) -> AppConfig:
    available_configurations = dict(
        dev=DevelopmentAppConfig,
        test=TestAppConfig,
        production=ProductionAppConfig
    )
    config_class = available_configurations.get(config_name)
    if not config_class:
        raise Exception('Unknown predefined config name "%s"' % config_name)
    return config_class()


available_configurations = dict(
    dev=DevelopmentAppConfig,
    test=TestAppConfig,
    production=ProductionAppConfig
)
