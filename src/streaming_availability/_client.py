# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import shows, genres, changes, countries
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, StreamingAvailabilityError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "StreamingAvailability",
    "AsyncStreamingAvailability",
    "Client",
    "AsyncClient",
]


class StreamingAvailability(SyncAPIClient):
    countries: countries.CountriesResource
    genres: genres.GenresResource
    shows: shows.ShowsResource
    changes: changes.ChangesResource
    with_raw_response: StreamingAvailabilityWithRawResponse
    with_streaming_response: StreamingAvailabilityWithStreamedResponse

    # client options
    rapidapi_key: str

    def __init__(
        self,
        *,
        rapidapi_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous streaming-availability client instance.

        This automatically infers the `rapidapi_key` argument from the `X_RAPIDAPI_KEY` environment variable if it is not provided.
        """
        if rapidapi_key is None:
            rapidapi_key = os.environ.get("X_RAPIDAPI_KEY")
        if rapidapi_key is None:
            raise StreamingAvailabilityError(
                "The rapidapi_key client option must be set either by passing rapidapi_key to the client or by setting the X_RAPIDAPI_KEY environment variable"
            )
        self.rapidapi_key = rapidapi_key

        if base_url is None:
            base_url = os.environ.get("STREAMING_AVAILABILITY_BASE_URL")
        if base_url is None:
            base_url = f"https://streaming-availability.p.rapidapi.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.countries = countries.CountriesResource(self)
        self.genres = genres.GenresResource(self)
        self.shows = shows.ShowsResource(self)
        self.changes = changes.ChangesResource(self)
        self.with_raw_response = StreamingAvailabilityWithRawResponse(self)
        self.with_streaming_response = StreamingAvailabilityWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        rapidapi_key = self.rapidapi_key
        return {"X-RapidAPI-Key": rapidapi_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        rapidapi_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            rapidapi_key=rapidapi_key or self.rapidapi_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncStreamingAvailability(AsyncAPIClient):
    countries: countries.AsyncCountriesResource
    genres: genres.AsyncGenresResource
    shows: shows.AsyncShowsResource
    changes: changes.AsyncChangesResource
    with_raw_response: AsyncStreamingAvailabilityWithRawResponse
    with_streaming_response: AsyncStreamingAvailabilityWithStreamedResponse

    # client options
    rapidapi_key: str

    def __init__(
        self,
        *,
        rapidapi_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async streaming-availability client instance.

        This automatically infers the `rapidapi_key` argument from the `X_RAPIDAPI_KEY` environment variable if it is not provided.
        """
        if rapidapi_key is None:
            rapidapi_key = os.environ.get("X_RAPIDAPI_KEY")
        if rapidapi_key is None:
            raise StreamingAvailabilityError(
                "The rapidapi_key client option must be set either by passing rapidapi_key to the client or by setting the X_RAPIDAPI_KEY environment variable"
            )
        self.rapidapi_key = rapidapi_key

        if base_url is None:
            base_url = os.environ.get("STREAMING_AVAILABILITY_BASE_URL")
        if base_url is None:
            base_url = f"https://streaming-availability.p.rapidapi.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.countries = countries.AsyncCountriesResource(self)
        self.genres = genres.AsyncGenresResource(self)
        self.shows = shows.AsyncShowsResource(self)
        self.changes = changes.AsyncChangesResource(self)
        self.with_raw_response = AsyncStreamingAvailabilityWithRawResponse(self)
        self.with_streaming_response = AsyncStreamingAvailabilityWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        rapidapi_key = self.rapidapi_key
        return {"X-RapidAPI-Key": rapidapi_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        rapidapi_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            rapidapi_key=rapidapi_key or self.rapidapi_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class StreamingAvailabilityWithRawResponse:
    def __init__(self, client: StreamingAvailability) -> None:
        self.countries = countries.CountriesResourceWithRawResponse(client.countries)
        self.genres = genres.GenresResourceWithRawResponse(client.genres)
        self.shows = shows.ShowsResourceWithRawResponse(client.shows)
        self.changes = changes.ChangesResourceWithRawResponse(client.changes)


class AsyncStreamingAvailabilityWithRawResponse:
    def __init__(self, client: AsyncStreamingAvailability) -> None:
        self.countries = countries.AsyncCountriesResourceWithRawResponse(client.countries)
        self.genres = genres.AsyncGenresResourceWithRawResponse(client.genres)
        self.shows = shows.AsyncShowsResourceWithRawResponse(client.shows)
        self.changes = changes.AsyncChangesResourceWithRawResponse(client.changes)


class StreamingAvailabilityWithStreamedResponse:
    def __init__(self, client: StreamingAvailability) -> None:
        self.countries = countries.CountriesResourceWithStreamingResponse(client.countries)
        self.genres = genres.GenresResourceWithStreamingResponse(client.genres)
        self.shows = shows.ShowsResourceWithStreamingResponse(client.shows)
        self.changes = changes.ChangesResourceWithStreamingResponse(client.changes)


class AsyncStreamingAvailabilityWithStreamedResponse:
    def __init__(self, client: AsyncStreamingAvailability) -> None:
        self.countries = countries.AsyncCountriesResourceWithStreamingResponse(client.countries)
        self.genres = genres.AsyncGenresResourceWithStreamingResponse(client.genres)
        self.shows = shows.AsyncShowsResourceWithStreamingResponse(client.shows)
        self.changes = changes.AsyncChangesResourceWithStreamingResponse(client.changes)


Client = StreamingAvailability

AsyncClient = AsyncStreamingAvailability
