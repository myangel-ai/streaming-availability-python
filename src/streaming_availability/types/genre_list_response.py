# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["GenreListResponse", "GenreListResponseItem"]


class GenreListResponseItem(BaseModel):
    id: str
    """Id of the genre"""

    name: str
    """Name of the genre"""


GenreListResponse: TypeAlias = List[GenreListResponseItem]
