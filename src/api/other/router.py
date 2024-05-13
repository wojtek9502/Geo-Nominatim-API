import logging

from fastapi import APIRouter
from src.api.other.schema import HealthzSchema

# Import router in src/__init__.py
router = APIRouter(tags=['tools'])
logger = logging.getLogger()


@router.get("/healthz", status_code=200, response_model=HealthzSchema)
async def healthz():
    return {"status": "ok"}
