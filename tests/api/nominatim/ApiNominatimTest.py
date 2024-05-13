import os
from typing import List

import pytest

from src.nominatim.types import NominatimSearchResponse, NominatimReverseResponse, NominatimReverseAddressResponse
from tests.api.ApiBaseTest import ApiBaseTest


class ApiNominatimTest(ApiBaseTest):
    @pytest.mark.parametrize("precision", ["MAX_PRECISION", "POSTAL_CODE", "CITY", "STATE"])
    def test_location_search(self, mocker, precision):
        # given - mock service response
        mock_value: List[NominatimSearchResponse] = [
            NominatimSearchResponse(
                display_name='Warszawa',
                latitude='52.237049',
                longitude='21.017532'
            )
        ]
        mocker.patch(
            'src.nominatim.services.NominatimService.search_address',
            return_value=mock_value
        )

        # given
        payload = dict(
            street="",
            city="Warszawa",
            county="",
            country="",
            postalcode="",
            state="",
            precision=precision
        )

        # when
        response = self.test_api.post(
            url="/geo/get_coordinates",
            json=payload,
            headers={'X-API-KEY': os.environ['API_AUTH_TOKEN']}
        )
        response_json = response.json()

        # then
        assert response.status_code == 200
        assert 'latitude' in response_json.keys()
        assert 'longitude' in response_json.keys()
        assert 'precision' in response_json.keys()

    def test_reverse(self, mocker):
        # given - mock service response
        mock_value: NominatimReverseResponse = NominatimReverseResponse(
            lat=52.237049,
            lon=21.017532,
            address=NominatimReverseAddressResponse(
                country_code='PL',
                country='Polska',
                city='Warszawa'
            )
        )

        mocker.patch(
            'src.nominatim.services.NominatimService.reverse_coords',
            return_value=mock_value
        )

        # given
        payload = dict(
            latitude=52.237049,
            longitude=21.017532
        )

        # when
        response = self.test_api.post(
            url="/geo/reverse",
            json=payload,
            headers={'X-API-KEY': os.environ['API_AUTH_TOKEN']}
        )
        response_json = response.json()

        # then
        assert response.status_code == 200
        assert 'address' in response_json.keys()
        assert response_json['address']['country'] == 'Polska'
        assert response_json['address']['city'] == 'Warszawa'
