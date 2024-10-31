# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    show_top_params,
    show_retrieve_params,
    show_search_title_params,
    show_search_filters_params,
)
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
from ..types.show_top_response import ShowTopResponse
from ..types.show_retrieve_response import ShowRetrieveResponse
from ..types.show_search_title_response import ShowSearchTitleResponse
from ..types.show_search_filters_response import ShowSearchFiltersResponse

__all__ = ["ShowsResource", "AsyncShowsResource"]


class ShowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return ShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return ShowsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        country: str | NotGiven = NOT_GIVEN,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        series_granularity: Literal["show", "season", "episode"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowRetrieveResponse:
        """
        Get the details of a show via id, imdbId or tmdbId, including the global
        streaming availability info.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the optional target country. If this parameter is not supplied, global streaming
              availability across all the countries will be returned. If it is supplied, only
              the streaming availability info from the given country will be returned. If you
              are only interested in the streaming availability in a single country, then it
              is recommended to use this parameter to reduce the size of the response and
              increase the performance of the endpoint. See /countries endpoint to get the
              list of supported countries.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          series_granularity: series_granularity determines the level of detail for series. It does not affect
              movies.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/shows/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "output_language": output_language,
                        "series_granularity": series_granularity,
                    },
                    show_retrieve_params.ShowRetrieveParams,
                ),
            ),
            cast_to=ShowRetrieveResponse,
        )

    def search_filters(
        self,
        *,
        country: str,
        catalogs: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        genres: List[str] | NotGiven = NOT_GIVEN,
        genres_relation: Literal["and", "or"] | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        order_by: Literal[
            "original_title",
            "release_date",
            "rating",
            "popularity_alltime",
            "popularity_1year",
            "popularity_1month",
            "popularity_1week",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        rating_max: int | NotGiven = NOT_GIVEN,
        rating_min: int | NotGiven = NOT_GIVEN,
        series_granularity: Literal["show", "season", "episode"] | NotGiven = NOT_GIVEN,
        show_original_language: str | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        year_max: int | NotGiven = NOT_GIVEN,
        year_min: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowSearchFiltersResponse:
        """
        Search through the catalog of the given streaming services in the given country.
        Provides filters such as show language, genres, keyword and release year. Output
        includes all the information about the shows, such as title, IMDb ID, TMDb ID,
        release year, deep links to streaming services, available subtitles, audios,
        available video quality and many more! Apart from the info about the given
        country-service combinations, output also includes information about streaming
        availability in the other services for the given country. Streaming availability
        info from the other countries are not included in the response.

        When show_type is movie or series_granularity is show, items per page is 20.
        When show_type is series and series_granularity is episode items per page is 10.
        Otherwise, items per page is 15.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

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

          genres: A comma seperated list of genre ids to only search within the shows in those
              genre. See /genres endpoint to see the available genres and their ids. Use
              genres_relation parameter to specify between returning shows that have at least
              one of the given genres or returning shows that have all of the given genres.

          genres_relation: Only used when there are multiple genres supplied in genres parameter.

              When or, the endpoint returns any show that has at least one of the given
              genres. When and, it only returns the shows that have all of the given genres.

          keyword: A keyword to only search within the shows have that keyword in their overview or
              title.

          order_by: Determines the ordering of the shows.

              You can switch between ascending and descending order by using the
              order_direction parameter.

          order_direction: Determines whether to order the results in ascending or descending order.

              Default value when ordering alphabetically or based on dates/times is asc.

              Default value when ordering by rating or popularity is desc.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          rating_max: Maximum rating of the shows.

          rating_min: Minimum rating of the shows.

          series_granularity: series_granularity determines the level of detail for series. It does not affect
              movies.

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

          show_original_language: [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code to only
              search within the shows whose original language matches with the provided
              language.

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          year_max: Maximum release/air year of the shows.

          year_min: Minimum release/air year of the shows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/shows/search/filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "catalogs": catalogs,
                        "cursor": cursor,
                        "genres": genres,
                        "genres_relation": genres_relation,
                        "keyword": keyword,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "output_language": output_language,
                        "rating_max": rating_max,
                        "rating_min": rating_min,
                        "series_granularity": series_granularity,
                        "show_original_language": show_original_language,
                        "show_type": show_type,
                        "year_max": year_max,
                        "year_min": year_min,
                    },
                    show_search_filters_params.ShowSearchFiltersParams,
                ),
            ),
            cast_to=ShowSearchFiltersResponse,
        )

    def search_title(
        self,
        *,
        country: str,
        title: str,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        series_granularity: Literal["show", "season", "episode"] | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowSearchTitleResponse:
        """Search for movies and series by a title.

        Maximum amount of items returned are 20
        unless there are more than 20 shows with the exact given title input. In that
        case all the items have 100% match with the title will be returned.

        Streaming availability info for the target country is included in the response,
        but not for the other countries.

        Results might include shows that are not streamable in the target country. Only
        criteria for the search are the title and the show type.

        No pagination is supported.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

          title: Title phrase to search for.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          series_granularity: series_granularity determines the level of detail for series. It does not affect
              movies.

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

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/shows/search/title",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "title": title,
                        "output_language": output_language,
                        "series_granularity": series_granularity,
                        "show_type": show_type,
                    },
                    show_search_title_params.ShowSearchTitleParams,
                ),
            ),
            cast_to=ShowSearchTitleResponse,
        )

    def top(
        self,
        *,
        country: str,
        service: str,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowTopResponse:
        """Get the official top shows in a service.

        Top shows are determined by the
        streaming service itself.

        Supported streaming services are:

        - Netflix: netflix
        - Amazon Prime Video: prime
        - Apple TV: apple
        - Max: hbo

        For unsupported services, this endpoint will return an empty list.

        Series granularity is always show for this endpoint, meaning that the output
        will not include season and episode info.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

          service: Id of the target service.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/shows/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "service": service,
                        "output_language": output_language,
                        "show_type": show_type,
                    },
                    show_top_params.ShowTopParams,
                ),
            ),
            cast_to=ShowTopResponse,
        )


class AsyncShowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return AsyncShowsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        country: str | NotGiven = NOT_GIVEN,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        series_granularity: Literal["show", "season", "episode"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowRetrieveResponse:
        """
        Get the details of a show via id, imdbId or tmdbId, including the global
        streaming availability info.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the optional target country. If this parameter is not supplied, global streaming
              availability across all the countries will be returned. If it is supplied, only
              the streaming availability info from the given country will be returned. If you
              are only interested in the streaming availability in a single country, then it
              is recommended to use this parameter to reduce the size of the response and
              increase the performance of the endpoint. See /countries endpoint to get the
              list of supported countries.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          series_granularity: series_granularity determines the level of detail for series. It does not affect
              movies.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/shows/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "output_language": output_language,
                        "series_granularity": series_granularity,
                    },
                    show_retrieve_params.ShowRetrieveParams,
                ),
            ),
            cast_to=ShowRetrieveResponse,
        )

    async def search_filters(
        self,
        *,
        country: str,
        catalogs: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        genres: List[str] | NotGiven = NOT_GIVEN,
        genres_relation: Literal["and", "or"] | NotGiven = NOT_GIVEN,
        keyword: str | NotGiven = NOT_GIVEN,
        order_by: Literal[
            "original_title",
            "release_date",
            "rating",
            "popularity_alltime",
            "popularity_1year",
            "popularity_1month",
            "popularity_1week",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        rating_max: int | NotGiven = NOT_GIVEN,
        rating_min: int | NotGiven = NOT_GIVEN,
        series_granularity: Literal["show", "season", "episode"] | NotGiven = NOT_GIVEN,
        show_original_language: str | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        year_max: int | NotGiven = NOT_GIVEN,
        year_min: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowSearchFiltersResponse:
        """
        Search through the catalog of the given streaming services in the given country.
        Provides filters such as show language, genres, keyword and release year. Output
        includes all the information about the shows, such as title, IMDb ID, TMDb ID,
        release year, deep links to streaming services, available subtitles, audios,
        available video quality and many more! Apart from the info about the given
        country-service combinations, output also includes information about streaming
        availability in the other services for the given country. Streaming availability
        info from the other countries are not included in the response.

        When show_type is movie or series_granularity is show, items per page is 20.
        When show_type is series and series_granularity is episode items per page is 10.
        Otherwise, items per page is 15.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

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

          genres: A comma seperated list of genre ids to only search within the shows in those
              genre. See /genres endpoint to see the available genres and their ids. Use
              genres_relation parameter to specify between returning shows that have at least
              one of the given genres or returning shows that have all of the given genres.

          genres_relation: Only used when there are multiple genres supplied in genres parameter.

              When or, the endpoint returns any show that has at least one of the given
              genres. When and, it only returns the shows that have all of the given genres.

          keyword: A keyword to only search within the shows have that keyword in their overview or
              title.

          order_by: Determines the ordering of the shows.

              You can switch between ascending and descending order by using the
              order_direction parameter.

          order_direction: Determines whether to order the results in ascending or descending order.

              Default value when ordering alphabetically or based on dates/times is asc.

              Default value when ordering by rating or popularity is desc.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          rating_max: Maximum rating of the shows.

          rating_min: Minimum rating of the shows.

          series_granularity: series_granularity determines the level of detail for series. It does not affect
              movies.

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

          show_original_language: [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code to only
              search within the shows whose original language matches with the provided
              language.

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          year_max: Maximum release/air year of the shows.

          year_min: Minimum release/air year of the shows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/shows/search/filters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "catalogs": catalogs,
                        "cursor": cursor,
                        "genres": genres,
                        "genres_relation": genres_relation,
                        "keyword": keyword,
                        "order_by": order_by,
                        "order_direction": order_direction,
                        "output_language": output_language,
                        "rating_max": rating_max,
                        "rating_min": rating_min,
                        "series_granularity": series_granularity,
                        "show_original_language": show_original_language,
                        "show_type": show_type,
                        "year_max": year_max,
                        "year_min": year_min,
                    },
                    show_search_filters_params.ShowSearchFiltersParams,
                ),
            ),
            cast_to=ShowSearchFiltersResponse,
        )

    async def search_title(
        self,
        *,
        country: str,
        title: str,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        series_granularity: Literal["show", "season", "episode"] | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowSearchTitleResponse:
        """Search for movies and series by a title.

        Maximum amount of items returned are 20
        unless there are more than 20 shows with the exact given title input. In that
        case all the items have 100% match with the title will be returned.

        Streaming availability info for the target country is included in the response,
        but not for the other countries.

        Results might include shows that are not streamable in the target country. Only
        criteria for the search are the title and the show type.

        No pagination is supported.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

          title: Title phrase to search for.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          series_granularity: series_granularity determines the level of detail for series. It does not affect
              movies.

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

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/shows/search/title",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "title": title,
                        "output_language": output_language,
                        "series_granularity": series_granularity,
                        "show_type": show_type,
                    },
                    show_search_title_params.ShowSearchTitleParams,
                ),
            ),
            cast_to=ShowSearchTitleResponse,
        )

    async def top(
        self,
        *,
        country: str,
        service: str,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        show_type: Literal["movie", "series"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShowTopResponse:
        """Get the official top shows in a service.

        Top shows are determined by the
        streaming service itself.

        Supported streaming services are:

        - Netflix: netflix
        - Amazon Prime Video: prime
        - Apple TV: apple
        - Max: hbo

        For unsupported services, this endpoint will return an empty list.

        Series granularity is always show for this endpoint, meaning that the output
        will not include season and episode info.

        Args:
          country: [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code of
              the target country. See /countries endpoint to get the list of supported
              countries.

          service: Id of the target service.

          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          show_type: Type of shows to search in. If not supplied, both movies and series will be
              included in the search results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/shows/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "service": service,
                        "output_language": output_language,
                        "show_type": show_type,
                    },
                    show_top_params.ShowTopParams,
                ),
            ),
            cast_to=ShowTopResponse,
        )


class ShowsResourceWithRawResponse:
    def __init__(self, shows: ShowsResource) -> None:
        self._shows = shows

        self.retrieve = to_raw_response_wrapper(
            shows.retrieve,
        )
        self.search_filters = to_raw_response_wrapper(
            shows.search_filters,
        )
        self.search_title = to_raw_response_wrapper(
            shows.search_title,
        )
        self.top = to_raw_response_wrapper(
            shows.top,
        )


class AsyncShowsResourceWithRawResponse:
    def __init__(self, shows: AsyncShowsResource) -> None:
        self._shows = shows

        self.retrieve = async_to_raw_response_wrapper(
            shows.retrieve,
        )
        self.search_filters = async_to_raw_response_wrapper(
            shows.search_filters,
        )
        self.search_title = async_to_raw_response_wrapper(
            shows.search_title,
        )
        self.top = async_to_raw_response_wrapper(
            shows.top,
        )


class ShowsResourceWithStreamingResponse:
    def __init__(self, shows: ShowsResource) -> None:
        self._shows = shows

        self.retrieve = to_streamed_response_wrapper(
            shows.retrieve,
        )
        self.search_filters = to_streamed_response_wrapper(
            shows.search_filters,
        )
        self.search_title = to_streamed_response_wrapper(
            shows.search_title,
        )
        self.top = to_streamed_response_wrapper(
            shows.top,
        )


class AsyncShowsResourceWithStreamingResponse:
    def __init__(self, shows: AsyncShowsResource) -> None:
        self._shows = shows

        self.retrieve = async_to_streamed_response_wrapper(
            shows.retrieve,
        )
        self.search_filters = async_to_streamed_response_wrapper(
            shows.search_filters,
        )
        self.search_title = async_to_streamed_response_wrapper(
            shows.search_title,
        )
        self.top = async_to_streamed_response_wrapper(
            shows.top,
        )
