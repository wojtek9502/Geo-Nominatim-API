import dataclasses
from enum import Enum
from typing import List


class NominatimSearchPrecisionEnum(Enum):
    MAX_PRECISION = 'MAX_PRECISION'
    POSTAL_CODE = 'POSTAL_CODE'
    CITY = 'CITY'
    STATE = 'STATE'


class NominatimSearchType(Enum):
    TEXT_SEARCH = 'TEXT_SEARCH'
    COMPLEX_SEARCH = 'COMPLEX_SEARCH'


@dataclasses.dataclass
class NominatimSearchQuery:
    street: str = ''
    city: str = ''
    county: str = ''
    country: str = ''
    postalcode: str = ''
    state: str = ''

    def to_dict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class NominatimSearchResponse:
    place_id: str = ''
    licence: str = ''
    osm_id: int = 123
    osm_type: str = ''
    bounding_box: List[int] = dataclasses.field(default_factory=list)
    display_name: str = ''
    latitude: str = ''
    longitude: str = ''
    object_type: str = ''
    type: str = ''
    importance: float = 1.0

    def to_dict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class NominatimReverseAddressResponse:
    amenity: str = ''
    road: str = ''
    neighbourhood: str = ''
    quarter: str = ''
    suburb: str = ''
    city: str = ''
    state: str = ''
    ISO3166_2_lvl4: str = ''
    postcode: str = ''
    country: str = ''
    country_code: str = ''

    def to_dict(self):
        return dataclasses.asdict(self)

@dataclasses.dataclass
class NominatimReverseResponse:
    place_id: str = ''
    licence: str = ''
    lat: float = 0.0
    lon: float = 0.0
    address: NominatimReverseAddressResponse = NominatimReverseAddressResponse()

    def to_dict(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class Coordinates:
    latitude: float
    longitude: float
