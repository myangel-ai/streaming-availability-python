# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import change_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.change_list_response import ChangeListResponse

__all__ = ["ChangesResource", "AsyncChangesResource"]


class ChangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return ChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return ChangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        change_type: Literal["new", "removed", "updated", "expiring", "upcoming"],
        country: str,
        item_type: Literal["show", "season", "episode"],
        catalogs: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        from_: int | NotGiven = NOT_GIVEN,
        include_unknown_dates: bool | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        to: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChangeListResponse:
        """
        Query the new, removed, updated, expiring or upcoming
        movies/series/seasons/episodes in a given list of streaming services. Results
        are ordered by the date of the changes. Changes listed per page is 25.

        Changes are listed under changes field, and shows affected by these changes are
        listed under shows field.

        Note that upcoming changes are only supported for Apple TV, Disney+, Max,
        Netflix and Prime Video. For other services, upcoming changes will return an
        empty list.

        Args:
          change_type: Type of changes to query.

          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

          item_type: Type of items to search in. If item_type is show, you can use show_type
              parameter to only search for movies or series.

          catalogs: A comma separated list of up to 32 catalogs to search in. See /countries
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

          cursor: Cursor is used for pagination. After each request, the response includes a
              hasMore boolean field to tell if there are more results that did not fit into
              the returned list. If it is set as true, to get the rest of the result set, send
              a new request (with the same parameters for other fields), and set the cursor
              parameter as the nextCursor value of the response of the previous request. Do
              not forget to escape the cursor value before putting it into a query as it might
              contain characters such as ?and &.

              The first request naturally does not require a cursor parameter.

          from_: [Unix Time Stamp](https://www.unixtimestamp.com/) to only query the changes
              happened/happening after this date (inclusive). For past changes such as new,
              removed or updated, the timestamp must be between today and 31 days ago. For
              future changes such as expiring or upcoming, the timestamp must be between today
              and 31 days from now in the future.

              If not supplied, the default value for past changes is 31 days ago, and for
              future changes is today.

          include_unknown_dates: Whether to include the changes with unknown dates. past changes such as new,
              removed or updated will always have a timestamp thus this parameter does not
              affect them. future changes such as expiring or upcoming may not have a
              timestamp if the exact date is not known (e.g. some services do not explicitly
              state the exact date of some of the upcoming/expiring shows). If set as true,
              the changes with unknown dates will be included in the response. If set as
              false, the changes with unknown dates will be excluded from the response.

              When ordering, the changes with unknown dates will be treated as if their
              timestamp is 0. Thus, they will appear first in the ascending order and last in
              the descending order.

          order_direction: Determines whether to order the results in ascending or descending order.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          to: [Unix Time Stamp](https://www.unixtimestamp.com/) to only query the changes
              happened/happening before this date (inclusive). For past changes such as new,
              removed or updated, the timestamp must be between today and 31 days ago. For
              future changes such as expiring or upcoming, the timestamp must be between today
              and 31 days from now in the future.

              If not supplied, the default value for past changes is today, and for future
              changes is 31 days from now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "change_type": change_type,
                        "country": country,
                        "item_type": item_type,
                        "catalogs": catalogs,
                        "cursor": cursor,
                        "from_": from_,
                        "include_unknown_dates": include_unknown_dates,
                        "order_direction": order_direction,
                        "output_language": output_language,
                        "show_type": show_type,
                        "to": to,
                    },
                    change_list_params.ChangeListParams,
                ),
            ),
            cast_to=ChangeListResponse,
        )


class AsyncChangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return AsyncChangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        change_type: Literal["new", "removed", "updated", "expiring", "upcoming"],
        country: str,
        item_type: Literal["show", "season", "episode"],
        catalogs: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        from_: int | NotGiven = NOT_GIVEN,
        include_unknown_dates: bool | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        to: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChangeListResponse:
        """
        Query the new, removed, updated, expiring or upcoming
        movies/series/seasons/episodes in a given list of streaming services. Results
        are ordered by the date of the changes. Changes listed per page is 25.

        Changes are listed under changes field, and shows affected by these changes are
        listed under shows field.

        Note that upcoming changes are only supported for Apple TV, Disney+, Max,
        Netflix and Prime Video. For other services, upcoming changes will return an
        empty list.

        Args:
          change_type: Type of changes to query.

          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

          item_type: Type of items to search in. If item_type is show, you can use show_type
              parameter to only search for movies or series.

          catalogs: A comma separated list of up to 32 catalogs to search in. See /countries
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

          cursor: Cursor is used for pagination. After each request, the response includes a
              hasMore boolean field to tell if there are more results that did not fit into
              the returned list. If it is set as true, to get the rest of the result set, send
              a new request (with the same parameters for other fields), and set the cursor
              parameter as the nextCursor value of the response of the previous request. Do
              not forget to escape the cursor value before putting it into a query as it might
              contain characters such as ?and &.

              The first request naturally does not require a cursor parameter.

          from_: [Unix Time Stamp](https://www.unixtimestamp.com/) to only query the changes
              happened/happening after this date (inclusive). For past changes such as new,
              removed or updated, the timestamp must be between today and 31 days ago. For
              future changes such as expiring or upcoming, the timestamp must be between today
              and 31 days from now in the future.

              If not supplied, the default value for past changes is 31 days ago, and for
              future changes is today.

          include_unknown_dates: Whether to include the changes with unknown dates. past changes such as new,
              removed or updated will always have a timestamp thus this parameter does not
              affect them. future changes such as expiring or upcoming may not have a
              timestamp if the exact date is not known (e.g. some services do not explicitly
              state the exact date of some of the upcoming/expiring shows). If set as true,
              the changes with unknown dates will be included in the response. If set as
              false, the changes with unknown dates will be excluded from the response.

              When ordering, the changes with unknown dates will be treated as if their
              timestamp is 0. Thus, they will appear first in the ascending order and last in
              the descending order.

          order_direction: Determines whether to order the results in ascending or descending order.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          to: [Unix Time Stamp](https://www.unixtimestamp.com/) to only query the changes
              happened/happening before this date (inclusive). For past changes such as new,
              removed or updated, the timestamp must be between today and 31 days ago. For
              future changes such as expiring or upcoming, the timestamp must be between today
              and 31 days from now in the future.

              If not supplied, the default value for past changes is today, and for future
              changes is 31 days from now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "change_type": change_type,
                        "country": country,
                        "item_type": item_type,
                        "catalogs": catalogs,
                        "cursor": cursor,
                        "from_": from_,
                        "include_unknown_dates": include_unknown_dates,
                        "order_direction": order_direction,
                        "output_language": output_language,
                        "show_type": show_type,
                        "to": to,
                    },
                    change_list_params.ChangeListParams,
                ),
            ),
            cast_to=ChangeListResponse,
        )


class ChangesResourceWithRawResponse:
    def __init__(self, changes: ChangesResource) -> None:
        self._changes = changes

        self.list = to_raw_response_wrapper(
            changes.list,
        )


class AsyncChangesResourceWithRawResponse:
    def __init__(self, changes: AsyncChangesResource) -> None:
        self._changes = changes

        self.list = async_to_raw_response_wrapper(
            changes.list,
        )


class ChangesResourceWithStreamingResponse:
    def __init__(self, changes: ChangesResource) -> None:
        self._changes = changes

        self.list = to_streamed_response_wrapper(
            changes.list,
        )


class AsyncChangesResourceWithStreamingResponse:
    def __init__(self, changes: AsyncChangesResource) -> None:
        self._changes = changes

        self.list = async_to_streamed_response_wrapper(
            changes.list,
        )
