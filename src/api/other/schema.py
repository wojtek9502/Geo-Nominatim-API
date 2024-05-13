from pydantic import BaseModel


class HealthzSchema(BaseModel):
    status: str = 'ok'
