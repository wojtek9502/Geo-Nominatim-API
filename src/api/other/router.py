import logging
from typing import Dict

from fastapi import APIRouter
from src.api.other.schema import HealthzSchema
from src.nominatim.services import NominatimService

# Import router in src/__init__.py
router = APIRouter(tags=['tools'])
logger = logging.getLogger()


@router.get("/healthz", status_code=200, response_model=HealthzSchema)
async def healthz():
    return {"status": "ok"}

@router.get("/nominatim/status", status_code=200, response_model=Dict)
async def nominatim_server_status():
    service = NominatimService()
    server_status = service.get_nominatim_status()
    return server_status
