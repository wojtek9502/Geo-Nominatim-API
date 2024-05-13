import os
from typing import Optional, List, Dict
import logging

from src.nominatim.client.NominatimClient import NominatimClient
from src.nominatim.client.NominatimClientAbstract import NominatimClientAbstract
from src.nominatim.types import NominatimSearchQuery, NominatimSearchResponse, NominatimSearchType, Coordinates, \
    NominatimReverseResponse, NominatimReverseAddressResponse

logger = logging.getLogger(__name__)


class NominatimService:
    def __init__(self, client: NominatimClientAbstract = None):
        self.client = client
        if not self.client:
            self.client = NominatimClient(
                base_url=os.environ['NOMINATIM_URL'],
                auth_token=None
            )

    @staticmethod
    def _convert_response_to_coordinates(nominatim_data: NominatimSearchResponse) -> Coordinates:
        return Coordinates(
            latitude=float(nominatim_data.latitude),
            longitude=float(nominatim_data.longitude)
        )

    def get_address_coordinates(self, nominatim_response: Optional[List[NominatimSearchResponse]]) -> Optional[Coordinates]:
        if nominatim_response:
            return self._convert_response_to_coordinates(nominatim_response[0])
        return None

    def search_address(self, address_query: NominatimSearchQuery, limit: int = 0,
                       search_type: NominatimSearchType = NominatimSearchType.COMPLEX_SEARCH) \
            -> Optional[List[NominatimSearchResponse]]:
        address_search_results = []
        nominatim_search_results = self.client.nominatim_search(
            address_query=address_query,
            limit=limit,
            search_type=search_type
        )

        if len(nominatim_search_results):
            for search_result in nominatim_search_results:
                result = NominatimSearchResponse(
                    latitude=search_result['lat'],
                    longitude=search_result['lon'],
                    display_name=search_result.get('display_name', ''),
                    place_id=search_result.get('place_id', ''),
                    licence=search_result.get('licence', ''),
                    osm_id=int(search_result.get('osm_id', '0')),
                    osm_type=search_result.get('osm_type', ''),
                    bounding_box=search_result.get('boundingbox', []),
                    object_type=search_result.get('class', ''),
                    type=search_result.get('type', ''),
                    importance=float(search_result.get('importance', '0.0'))
                )
                address_search_results.append(result)
                return address_search_results
        return None

    def reverse_coords(self, coords: Coordinates) -> NominatimReverseResponse:
        nominatim_reverse_result = self.client.nominatim_reverse(
            lat=coords.latitude,
            lon=coords.longitude
        )
        if len(nominatim_reverse_result):
            reversed_address = nominatim_reverse_result['address']
            nominatim_reverse_address = NominatimReverseAddressResponse(
                amenity=reversed_address.get('amenity', ''),
                road=reversed_address.get('road', ''),
                neighbourhood=reversed_address.get('neighbourhood', ''),
                quarter=reversed_address.get('quarter', ''),
                suburb=reversed_address.get('suburb', ''),
                city=reversed_address.get('city', ''),
                state=reversed_address.get('state', ''),
                ISO3166_2_lvl4=reversed_address.get('ISO3166-2-lvl4', ''),
                postcode=reversed_address.get('postcode', ''),
                country=reversed_address.get('country', ''),
                country_code=reversed_address.get('country_code', '')
            )
            return NominatimReverseResponse(
                place_id=str(nominatim_reverse_result['place_id']),
                licence=nominatim_reverse_result['licence'],
                lat=float(nominatim_reverse_result['lat']),
                lon=float(nominatim_reverse_result['lon']),
                address=nominatim_reverse_address
            )

    def get_nominatim_status(self) -> Dict:
        server_status = self.client.get_server_status()
        return server_status
