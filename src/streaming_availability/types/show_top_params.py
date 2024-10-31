# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShowTopParams"]


class ShowTopParams(TypedDict, total=False):
    country: Required[str]
    """
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
    the target country. See /countries endpoint to get the list of supported
    countries.
    """

    service: Required[str]
    """Id of the target service."""

    output_language: Literal["en", "es", "tr", "fr"]
    """
    [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
    language. Determines in which language the output will be in.
    """

    show_type: Literal["movie", "series"]
    """
    Type of shows to search in. If not supplied, both movies and series will be
    included in the search results.
    """
