# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShowSearchTitleParams"]


class ShowSearchTitleParams(TypedDict, total=False):
    country: Required[str]
    """
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
    the target country. See /countries endpoint to get the list of supported
    countries.
    """

    title: Required[str]
    """Title phrase to search for."""

    output_language: Literal["en", "es", "tr", "fr"]
    """
    [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
    language. Determines in which language the output will be in.
    """

    series_granularity: Literal["show", "season", "episode"]
    """series_granularity determines the level of detail for series.

    It does not affect movies.

    If series_granularity is show, then the output will not include season and
    episode info.

    If series_granularity is season, then the output will include season info but
    not episode info.

    If series_granularity is episode, then the output will include season and
    episode info.

    If you do not need season and episode info, then it is recommended to set
    series_granularity as show to reduce the size of the response and increase the
    performance of the endpoint.

    If you need deep links for individual seasons and episodes, then you should set
    series_granularity as episode. In this case response will include full streaming
    info for seasons and episodes, similar to the streaming info for movies and
    series; including deep links into seasons and episodes, individual
    subtitle/audio and video quality info etc.
    """

    show_type: Literal["movie", "series"]
    """
    Type of shows to search in. If not supplied, both movies and series will be
    included in the search results.
    """
