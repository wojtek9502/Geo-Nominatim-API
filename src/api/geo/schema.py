from pydantic import BaseModel

from src.nominatim.types import NominatimSearchPrecisionEnum


class NominatimSearchRequestSchema(BaseModel):
    street: str = ''
    city: str = ''
    county: str = ''
    country: str = ''
    postalcode: str = ''
    state: str = ''
    precision: NominatimSearchPrecisionEnum = NominatimSearchPrecisionEnum.MAX_PRECISION


class NominatimSearchResponseSchema(BaseModel):
    latitude: float
    longitude: float
    precision: NominatimSearchPrecisionEnum = NominatimSearchPrecisionEnum.MAX_PRECISION


class NominatimReverseRequestSchema(BaseModel):
    latitude: float
    longitude: float


class NominatimReverseAddressResponseSchema(BaseModel):
    amenity: str
    road: str
    neighbourhood: str
    quarter: str
    suburb: str
    city: str
    state: str
    ISO3166_2_lvl4: str
    postcode: str
    country: str
    country_code: str


class NominatimReverseResponseSchema(BaseModel):
    place_id: str
    licence: str
    lat: float
    lon: float
    address: NominatimReverseAddressResponseSchema
