from typing import Optional, Dict, List

from src.nominatim.client.NominatimClientAbstract import NominatimClientAbstract
from src.nominatim.types import NominatimSearchQuery, NominatimSearchType
from tests.utils.response_mocks import nominatim_search_response_mock, nominatim_reverse_response_mock


class NominatimTestClient(NominatimClientAbstract):
    def nominatim_search(self, address_query: NominatimSearchQuery, limit: int,
                         search_type: NominatimSearchType = NominatimSearchType.COMPLEX_SEARCH) -> Optional[List[Dict]]:
        return nominatim_search_response_mock

    def nominatim_reverse(self, lat: float, lon: float) -> Optional[Dict]:
        return nominatim_reverse_response_mock
