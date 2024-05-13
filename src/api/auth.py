import os

from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY_NAME = 'X-API-KEY'
API_KEY = os.environ['API_AUTH_TOKEN']
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def _is_token_valid_with_main_token(api_key) -> bool:
    if api_key == API_KEY:
        return True
    return False


async def validate_api_key(api_key: str = Security(api_key_header)):
    is_token_valid = _is_token_valid_with_main_token(api_key=api_key)

    if not is_token_valid:
        raise HTTPException(status_code=401, detail='Invalid or missing API Key')
