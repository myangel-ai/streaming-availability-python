# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from streaming_availability import StreamingAvailability, AsyncStreamingAvailability
from streaming_availability.types import (
    CountryListResponse,
    CountryRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCountries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: StreamingAvailability) -> None:
        country = client.countries.retrieve(
            country_code="country-code",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: StreamingAvailability) -> None:
        country = client.countries.retrieve(
            country_code="country-code",
            output_language="en",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StreamingAvailability) -> None:
        response = client.countries.with_raw_response.retrieve(
            country_code="country-code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StreamingAvailability) -> None:
        with client.countries.with_streaming_response.retrieve(
            country_code="country-code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryRetrieveResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StreamingAvailability) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.countries.with_raw_response.retrieve(
                country_code="",
            )

    @parametrize
    def test_method_list(self, client: StreamingAvailability) -> None:
        country = client.countries.list()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: StreamingAvailability) -> None:
        country = client.countries.list(
            output_language="en",
        )
        assert_matches_type(CountryListResponse, country, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StreamingAvailability) -> None:
        response = client.countries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StreamingAvailability) -> None:
        with client.countries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryListResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCountries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        country = await async_client.countries.retrieve(
            country_code="country-code",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        country = await async_client.countries.retrieve(
            country_code="country-code",
            output_language="en",
        )
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.countries.with_raw_response.retrieve(
            country_code="country-code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryRetrieveResponse, country, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.countries.with_streaming_response.retrieve(
            country_code="country-code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryRetrieveResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.countries.with_raw_response.retrieve(
                country_code="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStreamingAvailability) -> None:
        country = await async_client.countries.list()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        country = await async_client.countries.list(
            output_language="en",
        )
        assert_matches_type(CountryListResponse, country, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.countries.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryListResponse, country, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.countries.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryListResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True
