from config import config
from fastapi import Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="Authorization")


def authenticate(api_key: str = Depends(api_key_header)):
    if api_key != config.API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid API Key")
