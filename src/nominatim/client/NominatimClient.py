import json
from typing import List, Optional, Dict
import urllib.parse

import requests
from fastapi import HTTPException

from src.nominatim.client.exceptions import NominatimRequestError, \
    NominatimUnexpectedResponseError, NominatimError

import logging

from src.nominatim.client.utils import _validate_complex_search_query
from src.nominatim.types import NominatimSearchQuery, NominatimSearchType

logger = logging.getLogger('nominatim')


class NominatimClient:
    def __init__(self, base_url: str, auth_token: Optional[str], timeout=5):
        self.base_url = base_url
        self.auth_token = auth_token
        self.timeout = timeout

    def _get_text_search_query(self, address_query: NominatimSearchQuery) -> str:
        search_url = f'{self.base_url}/search?'
        street = f'{address_query.street},' if len(address_query.street) else ''
        city = f'{address_query.city},' if len(address_query.city) else ''
        postal_code = f'{address_query.postalcode},' if len(address_query.postalcode) else ''
        state = f'{address_query.state},' if len(address_query.state) else ''
        country = f'{address_query.country},' if len(address_query.country) else ''

        search_query = f'{street} {city} {postal_code} {state} {country}'.strip(',')
        query_params = dict(q=search_query)
        logger.info(f"Nominatim search query: {address_query}")
        search_url += urllib.parse.urlencode(query_params)
        return search_url

    def _get_complex_search_query(self, address_query: NominatimSearchQuery) -> str:
        search_url = f'{self.base_url}/search?'

        logger.info(f"Nominatim search query: {address_query}")
        query_dict = dict(
            city=address_query.city,
            country=address_query.country,
            county=address_query.county,
            postalcode=address_query.postalcode,
            state=address_query.state,
            street=address_query.street
        )
        _validate_complex_search_query(query=query_dict)
        search_url += urllib.parse.urlencode(query_dict)
        return search_url

    def _build_search_query(self, address_query: NominatimSearchQuery, limit: int, search_type: NominatimSearchType) -> str:
        query_url = ''
        if search_type == search_type.TEXT_SEARCH:
            query_url = self._get_text_search_query(address_query=address_query)
        elif search_type == search_type.COMPLEX_SEARCH:
            query_url = self._get_complex_search_query(address_query=address_query)
        query_url += f'&format=json'
        if limit > 0:
            query_url += f'&limit={limit}'
        return query_url

    def _build_reverse_query(self, lat: float, lon: float) -> str:
        query_url = f'{self.base_url}/reverse?'
        query_params = dict(lat=str(lat), lon=str(lon))

        logger.info(f"Nominatim reverse query: {query_params}")
        query_url += urllib.parse.urlencode(query_params)
        query_url += f'&format=json&zoom=18&addressdetails=1'
        return query_url

    def nominatim_request(self, url):
        headers = {}
        if self.auth_token:
            headers = {
                'Authorization': f'Basic {self.auth_token}'
            }
        response = requests.get(
            url=url,
            timeout=self.timeout,
            headers=headers
        )
        if response.status_code != 200:
            msg = f'Nominatim request error. Code: {response.status_code}, reason: {response.reason}, ' \
                  f'request url: {response.request.url} '
            logger.error(msg)
            raise NominatimRequestError(msg)

        try:
            response_data = response.json()
        except json.decoder.JSONDecodeError:
            raise NominatimUnexpectedResponseError(response.content)
        return response_data

    def nominatim_search(self, address_query: NominatimSearchQuery, limit: int,
                         search_type: NominatimSearchType = NominatimSearchType.COMPLEX_SEARCH) -> Optional[List[Dict]]:
        query_url = self._build_search_query(
            address_query=address_query,
            limit=limit,
            search_type=search_type
        )
        try:
            response = self.nominatim_request(url=query_url)
        except NominatimError as e:
            msg = f'Nominatim error. Check Nominatim server status'
            logger.info(msg)
            raise HTTPException(500, detail=msg)

        if len(response) == 0:
            msg = f'Nominatim not found data for query {address_query}'
            logger.info(msg)
            raise HTTPException(404, detail=msg)
        return response

    def nominatim_reverse(self, lat: float, lon: float) -> Optional[Dict]:
        query_url = self._build_reverse_query(
            lat=lat,
            lon=lon
        )
        try:
            response = self.nominatim_request(url=query_url)
        except NominatimError:
            msg = f'Nominatim error. Check Nominatim server status'
            logger.info(msg)
            raise HTTPException(500, detail=str(msg))

        if len(response) == 0:
            msg = f'Nominatim not found address for data lat:"{lat}", lon: "{lon}"'
            logger.info(msg)
            raise HTTPException(404, detail=msg)
        return response

    def get_server_status(self) -> Optional[Dict]:
        query_url = f'{self.base_url}/status?format=json'

        try:
            response = self.nominatim_request(url=query_url)
        except NominatimError:
            msg = f'Nominatim error. Check Nominatim server status'
            logger.info(msg)
            raise HTTPException(500, detail=msg)
        return response
