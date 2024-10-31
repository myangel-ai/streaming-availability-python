# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ShowTopResponse",
    "ShowTopResponseItem",
    "ShowTopResponseItemGenre",
    "ShowTopResponseItemImageSet",
    "ShowTopResponseItemImageSetHorizontalPoster",
    "ShowTopResponseItemImageSetVerticalPoster",
    "ShowTopResponseItemImageSetHorizontalBackdrop",
    "ShowTopResponseItemImageSetVerticalBackdrop",
    "ShowTopResponseItemStreamingOption",
    "ShowTopResponseItemStreamingOptionAudio",
    "ShowTopResponseItemStreamingOptionService",
    "ShowTopResponseItemStreamingOptionServiceImageSet",
    "ShowTopResponseItemStreamingOptionSubtitle",
    "ShowTopResponseItemStreamingOptionSubtitleLocale",
    "ShowTopResponseItemStreamingOptionAddon",
    "ShowTopResponseItemStreamingOptionAddonImageSet",
    "ShowTopResponseItemStreamingOptionPrice",
    "ShowTopResponseItemSeason",
    "ShowTopResponseItemSeasonStreamingOption",
    "ShowTopResponseItemSeasonStreamingOptionAudio",
    "ShowTopResponseItemSeasonStreamingOptionService",
    "ShowTopResponseItemSeasonStreamingOptionServiceImageSet",
    "ShowTopResponseItemSeasonStreamingOptionSubtitle",
    "ShowTopResponseItemSeasonStreamingOptionSubtitleLocale",
    "ShowTopResponseItemSeasonStreamingOptionAddon",
    "ShowTopResponseItemSeasonStreamingOptionAddonImageSet",
    "ShowTopResponseItemSeasonStreamingOptionPrice",
    "ShowTopResponseItemSeasonEpisode",
    "ShowTopResponseItemSeasonEpisodeStreamingOption",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionAudio",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionService",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionServiceImageSet",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionSubtitle",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionSubtitleLocale",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionAddon",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionAddonImageSet",
    "ShowTopResponseItemSeasonEpisodeStreamingOptionPrice",
]


class ShowTopResponseItemGenre(BaseModel):
    id: str
    """Id of the genre"""

    name: str
    """Name of the genre"""


class ShowTopResponseItemImageSetHorizontalPoster(BaseModel):
    w1080: str
    """Link to the 1080px wide version of the image."""

    w1440: str
    """Link to the 1440px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ShowTopResponseItemImageSetVerticalPoster(BaseModel):
    w240: str
    """Link to the 240px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w600: str
    """Link to the 600px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ShowTopResponseItemImageSetHorizontalBackdrop(BaseModel):
    w1080: str
    """Link to the 1080px wide version of the image."""

    w1440: str
    """Link to the 1440px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ShowTopResponseItemImageSetVerticalBackdrop(BaseModel):
    w240: str
    """Link to the 240px wide version of the image."""

    w360: str
    """Link to the 360px wide version of the image."""

    w480: str
    """Link to the 480px wide version of the image."""

    w600: str
    """Link to the 600px wide version of the image."""

    w720: str
    """Link to the 720px wide version of the image."""


class ShowTopResponseItemImageSet(BaseModel):
    horizontal_poster: ShowTopResponseItemImageSetHorizontalPoster = FieldInfo(alias="horizontalPoster")
    """Horizontal poster of the show."""

    vertical_poster: ShowTopResponseItemImageSetVerticalPoster = FieldInfo(alias="verticalPoster")
    """Vertical poster of the show."""

    horizontal_backdrop: Optional[ShowTopResponseItemImageSetHorizontalBackdrop] = FieldInfo(
        alias="horizontalBackdrop", default=None
    )
    """Horizontal backdrop of the show."""

    vertical_backdrop: Optional[ShowTopResponseItemImageSetVerticalBackdrop] = FieldInfo(
        alias="verticalBackdrop", default=None
    )
    """Vertical backdrop of the show."""


class ShowTopResponseItemStreamingOptionAudio(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class ShowTopResponseItemStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowTopResponseItemStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowTopResponseItemStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowTopResponseItemStreamingOptionSubtitleLocale(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class ShowTopResponseItemStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowTopResponseItemStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowTopResponseItemStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowTopResponseItemStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowTopResponseItemStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowTopResponseItemStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowTopResponseItemStreamingOption(BaseModel):
    audios: List[ShowTopResponseItemStreamingOptionAudio]
    """Array of the available audios."""

    available_since: int = FieldInfo(alias="availableSince")
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that this
    streaming option was detected.
    """

    expires_soon: bool = FieldInfo(alias="expiresSoon")
    """Whether the streaming option expires within a month."""

    link: str
    """
    Deep link to the streaming option's page in the web app of the streaming
    service. Unlike videoLink, this field is guaranteed to be populated.
    """

    service: ShowTopResponseItemStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowTopResponseItemStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowTopResponseItemStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowTopResponseItemStreamingOptionPrice] = None
    """Price of the renting or buying the item.

    A movie and an episode that is available to buy or rent will always have a
    price.

    A series or a season that is available to buy or rent may have a price or not.
    If the price is available, that means the entire series or the season can be
    bought or rented as a whole for the given price. If the price is null, that
    means sub-items of the series or the season are available to buy or rent, but it
    is not possible to buy or rent the entire series or the season as a whole at
    once. In this case, the price of the sub-items can be found in the episodes or
    seasons array.
    """

    quality: Optional[Literal["sd", "hd", "qhd", "uhd"]] = None
    """Maximum supported video quality of the streaming option."""

    video_link: Optional[str] = FieldInfo(alias="videoLink", default=None)
    """
    Deep link to the video associated with the streaming option. Omitted if there's
    no direct link to the video. Might have the same value as link.
    """


class ShowTopResponseItemSeasonStreamingOptionAudio(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class ShowTopResponseItemSeasonStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowTopResponseItemSeasonStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowTopResponseItemSeasonStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowTopResponseItemSeasonStreamingOptionSubtitleLocale(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class ShowTopResponseItemSeasonStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowTopResponseItemSeasonStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowTopResponseItemSeasonStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowTopResponseItemSeasonStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowTopResponseItemSeasonStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowTopResponseItemSeasonStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowTopResponseItemSeasonStreamingOption(BaseModel):
    audios: List[ShowTopResponseItemSeasonStreamingOptionAudio]
    """Array of the available audios."""

    available_since: int = FieldInfo(alias="availableSince")
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that this
    streaming option was detected.
    """

    expires_soon: bool = FieldInfo(alias="expiresSoon")
    """Whether the streaming option expires within a month."""

    link: str
    """
    Deep link to the streaming option's page in the web app of the streaming
    service. Unlike videoLink, this field is guaranteed to be populated.
    """

    service: ShowTopResponseItemSeasonStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowTopResponseItemSeasonStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowTopResponseItemSeasonStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowTopResponseItemSeasonStreamingOptionPrice] = None
    """Price of the renting or buying the item.

    A movie and an episode that is available to buy or rent will always have a
    price.

    A series or a season that is available to buy or rent may have a price or not.
    If the price is available, that means the entire series or the season can be
    bought or rented as a whole for the given price. If the price is null, that
    means sub-items of the series or the season are available to buy or rent, but it
    is not possible to buy or rent the entire series or the season as a whole at
    once. In this case, the price of the sub-items can be found in the episodes or
    seasons array.
    """

    quality: Optional[Literal["sd", "hd", "qhd", "uhd"]] = None
    """Maximum supported video quality of the streaming option."""

    video_link: Optional[str] = FieldInfo(alias="videoLink", default=None)
    """
    Deep link to the video associated with the streaming option. Omitted if there's
    no direct link to the video. Might have the same value as link.
    """


class ShowTopResponseItemSeasonEpisodeStreamingOptionAudio(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class ShowTopResponseItemSeasonEpisodeStreamingOptionServiceImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowTopResponseItemSeasonEpisodeStreamingOptionService(BaseModel):
    id: str
    """Id of the service."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the service."""

    image_set: ShowTopResponseItemSeasonEpisodeStreamingOptionServiceImageSet = FieldInfo(alias="imageSet")
    """Image set of the service."""

    name: str
    """Name of the service."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the service."""


class ShowTopResponseItemSeasonEpisodeStreamingOptionSubtitleLocale(BaseModel):
    language: str
    """
    [ISO 639-2](https://en.wikipedia.org/wiki/ISO_639-2) code of the associated
    language with the locale.
    """

    region: Optional[str] = None
    """
    [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of
    the country, or [UN M49](https://en.wikipedia.org/wiki/UN_M49) code of the area
    associated with the locale.
    """


class ShowTopResponseItemSeasonEpisodeStreamingOptionSubtitle(BaseModel):
    closed_captions: bool = FieldInfo(alias="closedCaptions")
    """Whether closed captions are available for the subtitle."""

    locale: ShowTopResponseItemSeasonEpisodeStreamingOptionSubtitleLocale
    """A language and optionally an associated region."""


class ShowTopResponseItemSeasonEpisodeStreamingOptionAddonImageSet(BaseModel):
    dark_theme_image: str = FieldInfo(alias="darkThemeImage")
    """Link to the logo suitable for dark themed background."""

    light_theme_image: str = FieldInfo(alias="lightThemeImage")
    """Link to the logo suitable for light themed background."""

    white_image: str = FieldInfo(alias="whiteImage")
    """Link to the logo that is all white."""


class ShowTopResponseItemSeasonEpisodeStreamingOptionAddon(BaseModel):
    id: str
    """Id of the addon."""

    home_page: str = FieldInfo(alias="homePage")
    """Link to the homepage of the addon."""

    image_set: ShowTopResponseItemSeasonEpisodeStreamingOptionAddonImageSet = FieldInfo(alias="imageSet")
    """Image set of the addon."""

    name: str
    """Name of the addon."""

    theme_color_code: str = FieldInfo(alias="themeColorCode")
    """Associated theme color hex code of the addon."""


class ShowTopResponseItemSeasonEpisodeStreamingOptionPrice(BaseModel):
    amount: str
    """Numerical amount of the price."""

    currency: str
    """
    [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) alphabetic code of the
    currency.
    """

    formatted: str
    """Formatted price, including both the amount and the currency."""


class ShowTopResponseItemSeasonEpisodeStreamingOption(BaseModel):
    audios: List[ShowTopResponseItemSeasonEpisodeStreamingOptionAudio]
    """Array of the available audios."""

    available_since: int = FieldInfo(alias="availableSince")
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that this
    streaming option was detected.
    """

    expires_soon: bool = FieldInfo(alias="expiresSoon")
    """Whether the streaming option expires within a month."""

    link: str
    """
    Deep link to the streaming option's page in the web app of the streaming
    service. Unlike videoLink, this field is guaranteed to be populated.
    """

    service: ShowTopResponseItemSeasonEpisodeStreamingOptionService
    """Details of the streaming service localized according to the parent country."""

    subtitles: List[ShowTopResponseItemSeasonEpisodeStreamingOptionSubtitle]
    """Array of the available subtitles."""

    type: Literal["free", "subscription", "buy", "rent", "addon"]
    """Type of the streaming option."""

    addon: Optional[ShowTopResponseItemSeasonEpisodeStreamingOptionAddon] = None
    """
    Addon that the streaming option is available through. Omitted if the streaming
    option is not available through an addon.
    """

    expires_on: Optional[int] = FieldInfo(alias="expiresOn", default=None)
    """
    [Unix Time Stamp](https://www.unixtimestamp.com/) of the date that the streaming
    option is expiring. In other words, last day to watch.
    """

    price: Optional[ShowTopResponseItemSeasonEpisodeStreamingOptionPrice] = None
    """Price of the renting or buying the item.

    A movie and an episode that is available to buy or rent will always have a
    price.

    A series or a season that is available to buy or rent may have a price or not.
    If the price is available, that means the entire series or the season can be
    bought or rented as a whole for the given price. If the price is null, that
    means sub-items of the series or the season are available to buy or rent, but it
    is not possible to buy or rent the entire series or the season as a whole at
    once. In this case, the price of the sub-items can be found in the episodes or
    seasons array.
    """

    quality: Optional[Literal["sd", "hd", "qhd", "uhd"]] = None
    """Maximum supported video quality of the streaming option."""

    video_link: Optional[str] = FieldInfo(alias="videoLink", default=None)
    """
    Deep link to the video associated with the streaming option. Omitted if there's
    no direct link to the video. Might have the same value as link.
    """


class ShowTopResponseItemSeasonEpisode(BaseModel):
    air_year: int = FieldInfo(alias="airYear")
    """The year that the episode aired."""

    item_type: Literal["episode"] = FieldInfo(alias="itemType")
    """Type of the item. Always episode."""

    streaming_options: Dict[str, List[ShowTopResponseItemSeasonEpisodeStreamingOption]] = FieldInfo(
        alias="streamingOptions"
    )
    """Map of the streaming options by the country code."""

    title: str
    """Title of the episode."""

    overview: Optional[str] = None
    """A brief overview of the plot of the episode."""


class ShowTopResponseItemSeason(BaseModel):
    first_air_year: int = FieldInfo(alias="firstAirYear")
    """The first year that the season aired."""

    item_type: Literal["season"] = FieldInfo(alias="itemType")
    """Type of the item. Always season."""

    last_air_year: int = FieldInfo(alias="lastAirYear")
    """The last year that the season aired."""

    streaming_options: Dict[str, List[ShowTopResponseItemSeasonStreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the season."""

    episodes: Optional[List[ShowTopResponseItemSeasonEpisode]] = None
    """Array of the episodes belong to the season."""


class ShowTopResponseItem(BaseModel):
    id: str
    """Id of the show."""

    cast: List[str]
    """Array of the cast of the show."""

    genres: List[ShowTopResponseItemGenre]
    """Array of the genres of the show."""

    image_set: ShowTopResponseItemImageSet = FieldInfo(alias="imageSet")
    """Image set of the show."""

    imdb_id: str = FieldInfo(alias="imdbId")
    """[IMDb](https://www.imdb.com/) id of the show."""

    item_type: Literal["show"] = FieldInfo(alias="itemType")
    """Type of the item. Always show."""

    original_title: str = FieldInfo(alias="originalTitle")
    """Original title of the show."""

    overview: str
    """A brief overview of the overall plot of the show."""

    rating: int
    """Rating of the show.

    This is calculated by taking the average of ratings found online from multiple
    sources.
    """

    show_type: Literal["movie", "series"] = FieldInfo(alias="showType")
    """Type of the show. Based on the type, some properties might be omitted."""

    streaming_options: Dict[str, List[ShowTopResponseItemStreamingOption]] = FieldInfo(alias="streamingOptions")
    """Map of the streaming options by the country code."""

    title: str
    """Title of the show."""

    tmdb_id: str = FieldInfo(alias="tmdbId")
    """[TMDB](https://www.themoviedb.org/) id of the show."""

    creators: Optional[List[str]] = None
    """Array of the creators of the series."""

    directors: Optional[List[str]] = None
    """Array of the directors of the movie."""

    episode_count: Optional[int] = FieldInfo(alias="episodeCount", default=None)
    """Number of episodes that are either aired or announced for a series."""

    first_air_year: Optional[int] = FieldInfo(alias="firstAirYear", default=None)
    """The first year that the series aired."""

    last_air_year: Optional[int] = FieldInfo(alias="lastAirYear", default=None)
    """The last year that the series aired."""

    release_year: Optional[int] = FieldInfo(alias="releaseYear", default=None)
    """The year that the movie was released."""

    runtime: Optional[int] = None
    """Runtime of the movie in minutes."""

    season_count: Optional[int] = FieldInfo(alias="seasonCount", default=None)
    """Number of seasons that are either aired or announced for a series."""

    seasons: Optional[List[ShowTopResponseItemSeason]] = None
    """Array of the seasons belong to the series."""


ShowTopResponse: TypeAlias = List[ShowTopResponseItem]
