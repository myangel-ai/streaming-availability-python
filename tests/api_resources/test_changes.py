# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from streaming_availability import StreamingAvailability, AsyncStreamingAvailability
from streaming_availability.types import ChangeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: StreamingAvailability) -> None:
        change = client.changes.list(
            change_type="new",
            country="country",
            item_type="show",
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: StreamingAvailability) -> None:
        change = client.changes.list(
            change_type="new",
            country="country",
            item_type="show",
            catalogs=["string"],
            cursor="cursor",
            from_=0,
            include_unknown_dates=True,
            order_direction="asc",
            output_language="en",
            show_type="movie",
            to=0,
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StreamingAvailability) -> None:
        response = client.changes.with_raw_response.list(
            change_type="new",
            country="country",
            item_type="show",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = response.parse()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StreamingAvailability) -> None:
        with client.changes.with_streaming_response.list(
            change_type="new",
            country="country",
            item_type="show",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = response.parse()
            assert_matches_type(ChangeListResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChanges:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStreamingAvailability) -> None:
        change = await async_client.changes.list(
            change_type="new",
            country="country",
            item_type="show",
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStreamingAvailability) -> None:
        change = await async_client.changes.list(
            change_type="new",
            country="country",
            item_type="show",
            catalogs=["string"],
            cursor="cursor",
            from_=0,
            include_unknown_dates=True,
            order_direction="asc",
            output_language="en",
            show_type="movie",
            to=0,
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStreamingAvailability) -> None:
        response = await async_client.changes.with_raw_response.list(
            change_type="new",
            country="country",
            item_type="show",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = await response.parse()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStreamingAvailability) -> None:
        async with async_client.changes.with_streaming_response.list(
            change_type="new",
            country="country",
            item_type="show",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = await response.parse()
            assert_matches_type(ChangeListResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True
