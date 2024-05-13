from pathlib import Path

from fastapi import FastAPI

import logging
from src import configs

# get config
app_config = configs.get_predefined_config(config_name=configs.config_name)

# logger
Path(app_config.LOGS_DIR).mkdir(parents=True, exist_ok=True)
logging.basicConfig(
     filename=f"{app_config.LOGS_DIR}/logs.log",
     level=logging.INFO,
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger()

# Fastapi
app = FastAPI(
    docs_url=f'/swagger-ui',
    redoc_url=f'/redoc',
    openapi_url=f'/openapi.json',
    dependencies=[],
)

from src.api.other.router import router as other_router
from src.api.geo.router import router as geo_router
app.include_router(geo_router)
app.include_router(other_router)

