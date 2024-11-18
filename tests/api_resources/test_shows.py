# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from streaming_availability import StreamingAvailability, AsyncStreamingAvailability
from streaming_availability.types import (
    ShowTopResponse,
    ShowRetrieveResponse,
    ShowSearchTitleResponse,
    ShowSearchFiltersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: StreamingAvailability) -> None:
        show = client.shows.retrieve(
            id="id",
        )
        assert_matches_type(ShowRetrieveResponse, show, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: StreamingAvailability) -> None:
        show = client.shows.retrieve(
            id="id",
            country="country",
            output_language="en",
            series_granularity="show",
        )
        assert_matches_type(ShowRetrieveResponse, show, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StreamingAvailability) -> None:
        response = client.shows.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = response.parse()
        assert_matches_type(ShowRetrieveResponse, show, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StreamingAvailability) -> None:
        with client.shows.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = response.parse()
            assert_matches_type(ShowRetrieveResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StreamingAvailability) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shows.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_search_filters(self, client: StreamingAvailability) -> None:
        show = client.shows.search_filters(
            country="country",
        )
        assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

    @parametrize
    def test_method_search_filters_with_all_params(self, client: StreamingAvailability) -> None:
        show = client.shows.search_filters(
            country="country",
            catalogs=["string"],
            cursor="cursor",
            genres=["string"],
            genres_relation="and",
            keyword="keyword",
            order_by="original_title",
            order_direction="asc",
            output_language="en",
            rating_max=0,
            rating_min=0,
            series_granularity="show",
            show_original_language="show_original_language",
            show_type="movie",
            year_max=0,
            year_min=0,
        )
        assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

    @parametrize
    def test_raw_response_search_filters(self, client: StreamingAvailability) -> None:
        response = client.shows.with_raw_response.search_filters(
            country="country",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = response.parse()
        assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

    @parametrize
    def test_streaming_response_search_filters(self, client: StreamingAvailability) -> None:
        with client.shows.with_streaming_response.search_filters(
            country="country",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = response.parse()
            assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search_title(self, client: StreamingAvailability) -> None:
        show = client.shows.search_title(
            country="country",
            title="title",
        )
        assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

    @parametrize
    def test_method_search_title_with_all_params(self, client: StreamingAvailability) -> None:
        show = client.shows.search_title(
            country="country",
            title="title",
            output_language="en",
            series_granularity="show",
            show_type="movie",
        )
        assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

    @parametrize
    def test_raw_response_search_title(self, client: StreamingAvailability) -> None:
        response = client.shows.with_raw_response.search_title(
            country="country",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = response.parse()
        assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

    @parametrize
    def test_streaming_response_search_title(self, client: StreamingAvailability) -> None:
        with client.shows.with_streaming_response.search_title(
            country="country",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = response.parse()
            assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_top(self, client: StreamingAvailability) -> None:
        show = client.shows.top(
            country="country",
            service="service",
        )
        assert_matches_type(ShowTopResponse, show, path=["response"])

    @parametrize
    def test_method_top_with_all_params(self, client: StreamingAvailability) -> None:
        show = client.shows.top(
            country="country",
            service="service",
            output_language="en",
            show_type="movie",
        )
        assert_matches_type(ShowTopResponse, show, path=["response"])

    @parametrize
    def test_raw_response_top(self, client: StreamingAvailability) -> None:
        response = client.shows.with_raw_response.top(
            country="country",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = response.parse()
        assert_matches_type(ShowTopResponse, show, path=["response"])

    @parametrize
    def test_streaming_response_top(self, client: StreamingAvailability) -> None:
        with client.shows.with_streaming_response.top(
            country="country",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = response.parse()
            assert_matches_type(ShowTopResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.retrieve(
            id="id",
        )
        assert_matches_type(ShowRetrieveResponse, show, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.retrieve(
            id="id",
            country="country",
            output_language="en",
            series_granularity="show",
        )
        assert_matches_type(ShowRetrieveResponse, show, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.shows.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = await response.parse()
        assert_matches_type(ShowRetrieveResponse, show, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.shows.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = await response.parse()
            assert_matches_type(ShowRetrieveResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStreamingAvailability) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shows.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_search_filters(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.search_filters(
            country="country",
        )
        assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

    @parametrize
    async def test_method_search_filters_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.search_filters(
            country="country",
            catalogs=["string"],
            cursor="cursor",
            genres=["string"],
            genres_relation="and",
            keyword="keyword",
            order_by="original_title",
            order_direction="asc",
            output_language="en",
            rating_max=0,
            rating_min=0,
            series_granularity="show",
            show_original_language="show_original_language",
            show_type="movie",
            year_max=0,
            year_min=0,
        )
        assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

    @parametrize
    async def test_raw_response_search_filters(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.shows.with_raw_response.search_filters(
            country="country",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = await response.parse()
        assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

    @parametrize
    async def test_streaming_response_search_filters(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.shows.with_streaming_response.search_filters(
            country="country",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = await response.parse()
            assert_matches_type(ShowSearchFiltersResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search_title(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.search_title(
            country="country",
            title="title",
        )
        assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

    @parametrize
    async def test_method_search_title_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.search_title(
            country="country",
            title="title",
            output_language="en",
            series_granularity="show",
            show_type="movie",
        )
        assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

    @parametrize
    async def test_raw_response_search_title(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.shows.with_raw_response.search_title(
            country="country",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = await response.parse()
        assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

    @parametrize
    async def test_streaming_response_search_title(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.shows.with_streaming_response.search_title(
            country="country",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = await response.parse()
            assert_matches_type(ShowSearchTitleResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_top(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.top(
            country="country",
            service="service",
        )
        assert_matches_type(ShowTopResponse, show, path=["response"])

    @parametrize
    async def test_method_top_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        show = await async_client.shows.top(
            country="country",
            service="service",
            output_language="en",
            show_type="movie",
        )
        assert_matches_type(ShowTopResponse, show, path=["response"])

    @parametrize
    async def test_raw_response_top(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.shows.with_raw_response.top(
            country="country",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        show = await response.parse()
        assert_matches_type(ShowTopResponse, show, path=["response"])

    @parametrize
    async def test_streaming_response_top(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.shows.with_streaming_response.top(
            country="country",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            show = await response.parse()
            assert_matches_type(ShowTopResponse, show, path=["response"])

        assert cast(Any, response.is_closed) is True
