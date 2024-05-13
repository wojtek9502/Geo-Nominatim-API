from abc import ABC, abstractmethod
from typing import Optional, List

from src.nominatim.services import NominatimService
from src.nominatim.types import NominatimSearchQuery, NominatimSearchResponse, NominatimSearchPrecisionEnum


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, query: NominatimSearchQuery) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, query: NominatimSearchQuery) -> Optional[List[NominatimSearchResponse]]:
        if self._next_handler:
            return self._next_handler.handle(query)
        return None


class SearchByAllParamsHandler(AbstractHandler):
    def handle(self, query: NominatimSearchQuery) -> Optional[List[NominatimSearchResponse]]:
        service = NominatimService()
        nominatim_response = service.search_address(query)

        if nominatim_response:
            return nominatim_response
        else:
            return super().handle(query)


class SearchWithPostalCodePrecision(AbstractHandler):
    def handle(self, query: NominatimSearchQuery) -> Optional[List[NominatimSearchResponse]]:
        service = NominatimService()
        new_query = NominatimSearchQuery(**query.__dict__)
        new_query.street = ''
        nominatim_response = service.search_address(new_query)

        if nominatim_response:
            return nominatim_response
        else:
            return super().handle(query)


class SearchWithCityPrecision(AbstractHandler):
    def handle(self, query: NominatimSearchQuery) -> Optional[List[NominatimSearchResponse]]:
        service = NominatimService()
        new_query = NominatimSearchQuery(**query.__dict__)
        new_query.street = ''
        new_query.postalcode = ''
        nominatim_response = service.search_address(new_query)

        if nominatim_response:
            return nominatim_response
        else:
            return super().handle(query)


class SearchWithStatePrecision(AbstractHandler):
    def handle(self, query: NominatimSearchQuery) -> Optional[List[NominatimSearchResponse]]:
        service = NominatimService()
        new_query = NominatimSearchQuery(**query.__dict__)
        new_query.street = ''
        new_query.postalcode = ''
        new_query.city = ''
        nominatim_response = service.search_address(new_query)

        if nominatim_response:
            return nominatim_response
        else:
            return super().handle(query)


class NominatimChain:
    def get_chain(self, minimum_precision: NominatimSearchPrecisionEnum):
        all_parameters_handler = SearchByAllParamsHandler()
        postal_code_precision_handler = SearchWithPostalCodePrecision()
        city_precision_handler = SearchWithCityPrecision()
        state_precision_handler = SearchWithStatePrecision()

        chain = all_parameters_handler
        if minimum_precision == NominatimSearchPrecisionEnum.MAX_PRECISION:
            chain = all_parameters_handler

        if minimum_precision == NominatimSearchPrecisionEnum.POSTAL_CODE:
            chain = all_parameters_handler \
                .set_next(postal_code_precision_handler)

        if minimum_precision == NominatimSearchPrecisionEnum.CITY:
            chain = all_parameters_handler \
                .set_next(postal_code_precision_handler) \
                .set_next(city_precision_handler)

        if minimum_precision == NominatimSearchPrecisionEnum.STATE:
            chain = all_parameters_handler \
                .set_next(postal_code_precision_handler) \
                .set_next(city_precision_handler) \
                .set_next(state_precision_handler)
        return chain

