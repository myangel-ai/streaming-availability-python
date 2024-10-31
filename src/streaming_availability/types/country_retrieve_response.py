# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "CountryRetrieveResponse",
    "Service",
    "ServiceAddon",
    "ServiceAddonImageSet",
    "ServiceImageSet",
    "ServiceStreamingOptionTypes",
]


class ServiceAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ServiceAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ServiceAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ServiceStreamingOptionTypes(BaseModel):
    addon: bool
    """Whether there are shows available via an addon/channel subscription."""

    buy: bool
    """Whether there are shows available to buy."""

    free: bool
    """Whether there are free shows to watch."""

    rent: bool
    """Whether there are shows available for rental."""

    subscription: bool
    """Whether there are shows available via a paid subscription plan."""


class Service(BaseModel):
    id: str
    """Id of the service."""

    addons: List[ServiceAddon]
    """Array of the supported addons in the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    streaming_option_types: ServiceStreamingOptionTypes = FieldInfo(alias="streamingOptionTypes")
    """Availability of the streaming option types in the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class CountryRetrieveResponse(BaseModel):
    country_code: str = FieldInfo(alias="countryCode")
    """
    [ISO 3166-1 alpha-2 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of
    the country.
    """

    name: str
    """Name of the country."""

    services: List[Service]
    """Array of the supported services in the country, ordered by popularity."""
