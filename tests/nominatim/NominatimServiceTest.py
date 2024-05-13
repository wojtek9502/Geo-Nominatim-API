from src.nominatim.services import NominatimService
from src.nominatim.types import NominatimSearchQuery, NominatimSearchType
from tests.BaseTest import BaseTest
from tests.utils.NominatimTestClient import NominatimTestClient


class NominatimServiceTest(BaseTest):
    def test_get_coords_from_existing_address_PL_text_search(self):
        # given
        nominatim_client = NominatimTestClient()
        service = NominatimService(client=nominatim_client)
        address_query = NominatimSearchQuery(
            city='Warszawa',
            country='PL'
        )

        # when
        nominatim_response = service.search_address(
            address_query=address_query,
            search_type=NominatimSearchType.TEXT_SEARCH
        )
        place_coords = service.get_address_coordinates(nominatim_response)

        # then
        assert place_coords
        assert place_coords.longitude
        assert place_coords.longitude

    def test_get_coords_from_existing_address_PL(self):
        # given
        nominatim_client = NominatimTestClient()
        service = NominatimService(client=nominatim_client)
        address_query = NominatimSearchQuery(
            city='Warszawa',
            country='PL'
        )

        # when
        nominatim_response = service.search_address(
            address_query=address_query,
            search_type=NominatimSearchType.COMPLEX_SEARCH
        )
        place_coords = service.get_address_coordinates(nominatim_response)

        # then
        assert place_coords
        assert place_coords.longitude
        assert place_coords.longitude


    def test_get_coords_from_postal_code_only_PL(self):
        # given
        nominatim_client = NominatimTestClient()
        service = NominatimService(client=nominatim_client)
        address_query = NominatimSearchQuery(
            postalcode='25-520',
        )

        # when
        nominatim_response = service.search_address(
            address_query=address_query,
            search_type=NominatimSearchType.COMPLEX_SEARCH
        )
        place_coords = service.get_address_coordinates(nominatim_response)

        # then
        assert place_coords
        assert place_coords.longitude
        assert place_coords.longitude

