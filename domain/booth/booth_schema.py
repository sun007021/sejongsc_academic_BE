from typing import Union

from pydantic import BaseModel


class BoothCreate(BaseModel):
    name: str
    description: Union[str, None] = None
    mapx: str
    mapy: str
class BoothUpdate(BaseModel):
    name: str
    description: Union[str, None] = None
