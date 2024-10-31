# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChangeListParams"]


class ChangeListParams(TypedDict, total=False):
    change_type: Required[Literal["new", "removed", "updated", "expiring", "upcoming"]]
    """Type of changes to query."""

    country: Required[str]
    """
    [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
    the target country. See /countries endpoint to get the list of supported
    countries.
    """

    item_type: Required[Literal["show", "season", "episode"]]
    """
    Type of items to search in. If item_type is show, you can use show_type
    parameter to only search for movies or series.
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

    from_: Annotated[int, PropertyInfo(alias="from")]
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) to only query the changes
    happened/happening after this date (inclusive). For past changes such as new,
    removed or updated, the timestamp must be between today and 31 days ago. For
    future changes such as expiring or upcoming, the timestamp must be between today
    and 31 days from now in the future.

    If not supplied, the default value for past changes is 31 days ago, and for
    future changes is today.
    """

    include_unknown_dates: bool
    """
    Whether to include the changes with unknown dates. past changes such as new,
    removed or updated will always have a timestamp thus this parameter does not
    affect them. future changes such as expiring or upcoming may not have a
    timestamp if the exact date is not known (e.g. some services do not explicitly
    state the exact date of some of the upcoming/expiring shows). If set as true,
    the changes with unknown dates will be included in the response. If set as
    false, the changes with unknown dates will be excluded from the response.

    When ordering, the changes with unknown dates will be treated as if their
    timestamp is 0. Thus, they will appear first in the ascending order and last in
    the descending order.
    """

    order_direction: Literal["asc", "desc"]
    """Determines whether to order the results in ascending or descending order."""

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

    to: int
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) to only query the changes
    happened/happening before this date (inclusive). For past changes such as new,
    removed or updated, the timestamp must be between today and 31 days ago. For
    future changes such as expiring or upcoming, the timestamp must be between today
    and 31 days from now in the future.

    If not supplied, the default value for past changes is today, and for future
    changes is 31 days from now.
    """
