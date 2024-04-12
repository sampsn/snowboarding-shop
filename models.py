from pydantic import BaseModel
from enum import Enum


class Brand(Enum):
    NITRO = "Nitro"
    SALOMAN = "Saloman"
    BURTON = "Burton"


class Board(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Brand


class BoardRequest(BaseModel):
    length: int
    color: str
    has_bindings: bool
    brand: Brand
