import logging
from typing import Dict

from src.nominatim.client.exceptions import NominatimInvalidSearchQueryParamsError

logger = logging.getLogger('nominatim')


def _validate_complex_search_query(query: Dict):
    allowed_search_params = ['street', 'city', 'county', 'state', 'country', 'postalcode']
    for param in query.keys():
        if param not in allowed_search_params:
            msg = f'Nominatim invalid search params. Allowed params: {allowed_search_params}. ' \
                  f'See: https://nominatim.org/release-docs/latest/api/Search/'
            logger.error(msg)
            raise NominatimInvalidSearchQueryParamsError(msg)
