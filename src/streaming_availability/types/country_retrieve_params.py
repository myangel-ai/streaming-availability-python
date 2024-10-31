# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CountryRetrieveParams"]


class CountryRetrieveParams(TypedDict, total=False):
    output_language: Literal["en", "es", "tr", "fr"]
    """
    [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
    language. Determines in which language the output will be in.
    """
