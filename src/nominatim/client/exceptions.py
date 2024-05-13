class NominatimError(Exception):
    ...


class NominatimRequestError(NominatimError):
    ...


class NominatimInvalidSearchQueryParamsError(NominatimError):
    ...


class NominatimUnexpectedResponseError(NominatimError):
    ...
