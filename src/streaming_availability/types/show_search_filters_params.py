# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ShowSearchFiltersParams"]


class ShowSearchFiltersParams(TypedDict, total=False):
    country: Required[str]
    """
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
    the target country. See /countries endpoint to get the list of supported
    countries.
    """

    catalogs: List[str]
    """
    A comma separated list of up to 32 catalogs to search in. See /countries
    endpoint to get the supported services in each country and their ids.

    When multiple catalogs are passed as a comma separated list, any show that is in
    at least one of the catalogs will be included in the result.

    If no catalogs are passed, the endpoint will search in all the available
    catalogs in the country.

    Syntax of the catalogs supplied in the list can be as the followings:

    - <sevice_id>: Searches in the entire catalog of that service, including (if
      applicable) rentable, buyable shows or shows available through addons e.g.
      netflix, prime, apple

    - <sevice_id>.<streaming_option_type>: Only returns the shows that are available
      in that service with the given streaming option type. Valid streaming option
      types are subscription, free, rent, buy and addon e.g. peacock.free only
      returns the shows on Peacock that are free to watch, prime.subscription only
      returns the shows on Prime Video that are available to watch with a Prime
      subscription. hulu.addon only returns the shows on Hulu that are available via
      an addon, prime.rent only returns the shows on Prime Video that are rentable.

    - <sevice_id>.addon.<addon_id>: Only returns the shows that are available in
      that service with the given addon. Check /countries endpoint to fetch the
      available addons for a service in each country. Some sample values are:
      hulu.addon.hbo, prime.addon.hbomaxus.
    """

    cursor: str
    """
    Cursor is used for pagination. After each request, the response includes a
    hasMore boolean field to tell if there are more results that did not fit into
    the returned list. If it is set as true, to get the rest of the result set, send
    a new request (with the same parameters for other fields), and set the cursor
    parameter as the nextCursor value of the response of the previous request. Do
    not forget to escape the cursor value before putting it into a query as it might
    contain characters such as ?and &.

    The first request naturally does not require a cursor parameter.
    """

    genres: List[str]
    """
    A comma seperated list of genre ids to only search within the shows in those
    genre. See /genres endpoint to see the available genres and their ids. Use
    genres_relation parameter to specify between returning shows that have at least
    one of the given genres or returning shows that have all of the given genres.
    """

    genres_relation: Literal["and", "or"]
    """Only used when there are multiple genres supplied in genres parameter.

    When or, the endpoint returns any show that has at least one of the given
    genres. When and, it only returns the shows that have all of the given genres.
    """

    keyword: str
    """
    A keyword to only search within the shows have that keyword in their overview or
    title.
    """

    order_by: Literal[
        "original_title",
        "release_date",
        "rating",
        "popularity_alltime",
        "popularity_1year",
        "popularity_1month",
        "popularity_1week",
    ]
    """Determines the ordering of the shows.

    You can switch between ascending and descending order by using the
    order_direction parameter.
    """

    order_direction: Literal["asc", "desc"]
    """Determines whether to order the results in ascending or descending order.

    Default value when ordering alphabetically or based on dates/times is asc.

    Default value when ordering by rating or popularity is desc.
    """

    output_language: Literal["en", "es", "tr", "fr"]
    """
    [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
    language. Determines in which language the output will be in.
    """

    rating_max: int
    """Maximum rating of the shows."""

    rating_min: int
    """Minimum rating of the shows."""

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

    show_original_language: str
    """
    [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code to only
    search within the shows whose original language matches with the provided
    language.
    """

    show_type: Literal["movie", "series"]
    """
    Type of shows to search in. If not supplied, both movies and series will be
    included in the search results.
    """

    year_max: int
    """Maximum release/air year of the shows."""

    year_min: int
    """Minimum release/air year of the shows."""
