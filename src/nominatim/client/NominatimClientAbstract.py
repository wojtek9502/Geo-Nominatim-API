import abc
from typing import List, Optional, Dict

from src.nominatim.types import NominatimSearchQuery, NominatimSearchType


class NominatimClientAbstract(abc.ABC):
    @abc.abstractmethod
    def nominatim_search(self, address_query: NominatimSearchQuery, limit: int,
                         search_type: NominatimSearchType = NominatimSearchType.COMPLEX_SEARCH) -> Optional[List[Dict]]:
        ...

    @abc.abstractmethod
    def nominatim_reverse(self, lat: float, lon: float) -> Optional[Dict]:
        ...
