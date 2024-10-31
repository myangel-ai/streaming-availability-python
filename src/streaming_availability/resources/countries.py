# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import country_list_params, country_retrieve_params
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
from ..types.country_list_response import CountryListResponse
from ..types.country_retrieve_response import CountryRetrieveResponse

__all__ = ["CountriesResource", "AsyncCountriesResource"]


class CountriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return CountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return CountriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        country_code: str,
        *,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryRetrieveResponse:
        """
        Get a country and the list of the supported services and their details.

        Details of services include names, logos, supported streaming types
        (subscription, rent, buy, free etc.) and list of available addons/channels.

        Args:
          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            f"/countries/{country_code}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"output_language": output_language}, country_retrieve_params.CountryRetrieveParams
                ),
            ),
            cast_to=CountryRetrieveResponse,
        )

    def list(
        self,
        *,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryListResponse:
        """
        Get all the supported countries and the list of the supported services and their
        details for each country.

        Details of services include names, logos, supported streaming types
        (subscription, rent, buy, free etc.) and list of available addons/channels.

        Args:
          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"output_language": output_language}, country_list_params.CountryListParams),
            ),
            cast_to=CountryListResponse,
        )


class AsyncCountriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return AsyncCountriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        country_code: str,
        *,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryRetrieveResponse:
        """
        Get a country and the list of the supported services and their details.

        Details of services include names, logos, supported streaming types
        (subscription, rent, buy, free etc.) and list of available addons/channels.

        Args:
          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            f"/countries/{country_code}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"output_language": output_language}, country_retrieve_params.CountryRetrieveParams
                ),
            ),
            cast_to=CountryRetrieveResponse,
        )

    async def list(
        self,
        *,
        output_language: Literal["en", "es", "tr", "fr"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryListResponse:
        """
        Get all the supported countries and the list of the supported services and their
        details for each country.

        Details of services include names, logos, supported streaming types
        (subscription, rent, buy, free etc.) and list of available addons/channels.

        Args:
          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/countries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"output_language": output_language}, country_list_params.CountryListParams
                ),
            ),
            cast_to=CountryListResponse,
        )


class CountriesResourceWithRawResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.retrieve = to_raw_response_wrapper(
            countries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            countries.list,
        )


class AsyncCountriesResourceWithRawResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.retrieve = async_to_raw_response_wrapper(
            countries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            countries.list,
        )


class CountriesResourceWithStreamingResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.retrieve = to_streamed_response_wrapper(
            countries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            countries.list,
        )


class AsyncCountriesResourceWithStreamingResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.retrieve = async_to_streamed_response_wrapper(
            countries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            countries.list,
        )
