# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import genre_list_params
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
from ..types.genre_list_response import GenreListResponse

__all__ = ["GenresResource", "AsyncGenresResource"]


class GenresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return GenresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return GenresResourceWithStreamingResponse(self)

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
    ) -> GenreListResponse:
        """
        Get the list of supported genres.

        Args:
          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/genres",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"output_language": output_language}, genre_list_params.GenreListParams),
            ),
            cast_to=GenreListResponse,
        )


class AsyncGenresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/streaming-availability-python#with_streaming_response
        """
        return AsyncGenresResourceWithStreamingResponse(self)

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
    ) -> GenreListResponse:
        """
        Get the list of supported genres.

        Args:
          output_language: [ISO 639-1 code](https://en.wikipedia.org/wiki/ISO_639-1) of the output
              language. Determines in which language the output will be in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/genres",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"output_language": output_language}, genre_list_params.GenreListParams
                ),
            ),
            cast_to=GenreListResponse,
        )


class GenresResourceWithRawResponse:
    def __init__(self, genres: GenresResource) -> None:
        self._genres = genres

        self.list = to_raw_response_wrapper(
            genres.list,
        )


class AsyncGenresResourceWithRawResponse:
    def __init__(self, genres: AsyncGenresResource) -> None:
        self._genres = genres

        self.list = async_to_raw_response_wrapper(
            genres.list,
        )


class GenresResourceWithStreamingResponse:
    def __init__(self, genres: GenresResource) -> None:
        self._genres = genres

        self.list = to_streamed_response_wrapper(
            genres.list,
        )


class AsyncGenresResourceWithStreamingResponse:
    def __init__(self, genres: AsyncGenresResource) -> None:
        self._genres = genres

        self.list = async_to_streamed_response_wrapper(
            genres.list,
        )
