import dataclasses
import logging

from fastapi import APIRouter, Depends

from src.api import auth
from src.api.geo.schema import NominatimSearchRequestSchema, NominatimSearchResponseSchema, \
    NominatimReverseResponseSchema, NominatimReverseRequestSchema
from src.nominatim.handler import NominatimChain
from src.nominatim.services import NominatimService
from src.nominatim.types import NominatimSearchQuery, Coordinates

router = APIRouter(tags=['geo'], prefix='/geo')
logger = logging.getLogger()


@router.post("/get_coordinates", status_code=200, response_model=NominatimSearchResponseSchema,
             dependencies=[Depends(auth.validate_api_key)])
async def get_coordinates(request_data: NominatimSearchRequestSchema):
    service = NominatimService()
    nominatim_query = NominatimSearchQuery(
        street=request_data.street,
        city=request_data.city,
        country=request_data.country,
        county=request_data.county,
        postalcode=request_data.postalcode,
        state=request_data.state
    )

    nominatim_chain = NominatimChain().get_chain(minimum_precision=request_data.precision)
    nominatim_response = nominatim_chain.handle(query=nominatim_query)
    coordinates = service.get_address_coordinates(nominatim_response)

    return NominatimSearchResponseSchema(
        latitude=coordinates.latitude,
        longitude=coordinates.longitude,
        precision=request_data.precision
    )


@router.post("/reverse", status_code=200, response_model=NominatimReverseResponseSchema,
             dependencies=[Depends(auth.validate_api_key)])
async def get_coordinates(request_data: NominatimReverseRequestSchema):
    service = NominatimService()
    coords = Coordinates(latitude=request_data.latitude, longitude=request_data.longitude)
    nominatim_response = service.reverse_coords(coords=coords)
    return NominatimReverseResponseSchema(**dataclasses.asdict(nominatim_response))
